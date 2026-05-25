from __future__ import annotations

import hashlib
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

import networkx as nx
from git import Repo

from app.analysis.dependency.graph_builder import build_python_import_graph
from app.analysis.framework_detection.detector import detect_frameworks
from app.memory.vector_store.chroma_store import ChromaMemoryStore


class RepositoryService:
    def __init__(self) -> None:
        self._issues: list[dict[str, Any]] = []
        self.memory = ChromaMemoryStore()

    async def analyze(self, repository_url: str) -> dict[str, Any]:
        with TemporaryDirectory(prefix='reposage-') as tmp:
            repo_path = Path(tmp) / 'repo'
            Repo.clone_from(repository_url, repo_path, depth=1)
            graph = build_python_import_graph(repo_path)
            issues = self._detect_issues(repo_path, graph)
            frameworks = detect_frameworks(repo_path)
            cognition = {
                'module_count': len(graph.nodes),
                'edge_count': len(graph.edges),
                'frameworks': frameworks,
                'maintainability_score': max(0, 100 - len(issues) * 2),
            }
            self._issues = issues
            self.memory.add(
                doc_id=hashlib.sha1(repository_url.encode()).hexdigest(),
                text=f"{repository_url} frameworks={frameworks} issues={len(issues)}",
                metadata={'repository_url': repository_url, 'issues': len(issues)},
            )
            return {
                'repository_url': repository_url,
                'nodes': list(graph.nodes),
                'edges': [{'source': u, 'target': v} for u, v in graph.edges],
                'issues': issues,
                'topology': self._topology(graph),
                'cognition': cognition,
            }

    def list_issues(self) -> list[dict[str, Any]]:
        return self._issues

    def _detect_issues(self, root: Path, graph: nx.DiGraph) -> list[dict[str, Any]]:
        issues: list[dict[str, Any]] = []
        for file in root.rglob('*'):
            if file.is_file() and file.suffix in {'.py', '.ts', '.tsx', '.js', '.jsx'}:
                content = file.read_text(encoding='utf-8', errors='ignore')
                if 'TODO' in content or 'FIXME' in content:
                    issues.append({'id': hashlib.md5(str(file).encode()).hexdigest(), 'type': 'todo', 'file': str(file.relative_to(root))})
        for cycle in nx.simple_cycles(graph):
            issues.append({'id': hashlib.md5(str(cycle).encode()).hexdigest(), 'type': 'cyclic_dependency', 'cycle': cycle})
        return issues

    def _topology(self, graph: nx.DiGraph) -> dict[str, Any]:
        return {
            'weakly_connected_components': [list(c) for c in nx.weakly_connected_components(graph)] if graph.nodes else [],
            'central_modules': sorted(nx.degree_centrality(graph).items(), key=lambda x: x[1], reverse=True)[:10] if graph.nodes else [],
        }
