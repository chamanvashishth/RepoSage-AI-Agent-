'use client';

import { useState } from 'react';
import { useRepoStore } from '../../store/useRepoStore';

export function RepoAnalyzer() {
  const [url, setUrl] = useState('https://github.com/psf/requests');
  const { analyze, loading, data, error } = useRepoStore();

  return (
    <section className='rounded-xl border border-cyan-500/30 bg-slate-900/70 p-4'>
      <h2 className='text-xl font-semibold text-cyan-300'>Repository Analyzer</h2>
      <div className='mt-3 flex gap-2'>
        <input value={url} onChange={(e) => setUrl(e.target.value)} className='flex-1 rounded bg-slate-800 px-3 py-2' />
        <button onClick={() => analyze(url)} disabled={loading} className='rounded bg-fuchsia-600 px-4 py-2'>{loading ? 'Analyzing...' : 'Analyze'}</button>
      </div>
      {error && <p className='mt-3 text-red-400'>{error}</p>}
      {data && <p className='mt-3 text-cyan-200'>Modules: {data.cognition.module_count} · Score: {data.cognition.maintainability_score}</p>}
    </section>
  );
}
