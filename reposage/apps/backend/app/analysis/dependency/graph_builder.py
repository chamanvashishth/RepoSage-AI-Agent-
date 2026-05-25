import ast
from pathlib import Path
import networkx as nx


def build_python_import_graph(root: Path) -> nx.DiGraph:
    graph = nx.DiGraph()
    for file in root.rglob('*.py'):
        rel = str(file.relative_to(root))
        graph.add_node(rel)
        try:
            tree = ast.parse(file.read_text(encoding='utf-8'))
        except Exception:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    graph.add_edge(rel, alias.name)
            elif isinstance(node, ast.ImportFrom) and node.module:
                graph.add_edge(rel, node.module)
    return graph
