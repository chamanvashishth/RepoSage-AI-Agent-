from pathlib import Path


def detect_frameworks(repo_path: Path) -> list[str]:
    frameworks: set[str] = set()
    if (repo_path / 'package.json').exists():
        pkg = (repo_path / 'package.json').read_text(encoding='utf-8', errors='ignore').lower()
        if 'next' in pkg:
            frameworks.add('nextjs')
        if 'react' in pkg:
            frameworks.add('react')
    if (repo_path / 'pyproject.toml').exists() or (repo_path / 'requirements.txt').exists():
        frameworks.add('python')
    return sorted(frameworks)
