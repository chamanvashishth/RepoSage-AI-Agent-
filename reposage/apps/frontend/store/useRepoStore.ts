import { create } from 'zustand';
import { analyzeRepo } from '../services/api';
import type { AnalyzeResult } from '../types';

interface RepoState {
  loading: boolean;
  data?: AnalyzeResult;
  error?: string;
  analyze: (url: string) => Promise<void>;
}

export const useRepoStore = create<RepoState>((set) => ({
  loading: false,
  analyze: async (url: string) => {
    set({ loading: true, error: undefined });
    try {
      const data = await analyzeRepo(url);
      set({ data, loading: false });
    } catch (e) {
      set({ error: e instanceof Error ? e.message : 'Unknown error', loading: false });
    }
  },
}));
