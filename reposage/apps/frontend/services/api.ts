import type { AnalyzeResult } from '../types';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE ?? 'http://localhost:8000';

export async function analyzeRepo(repositoryUrl: string): Promise<AnalyzeResult> {
  const res = await fetch(`${API_BASE}/api/repository/analyze`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ repository_url: repositoryUrl }),
  });
  if (!res.ok) throw new Error('Failed to analyze repository');
  return res.json();
}
