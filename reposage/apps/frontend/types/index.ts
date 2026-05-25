export interface GraphEdge { source: string; target: string }
export interface AnalyzeResult { nodes: string[]; edges: GraphEdge[]; cognition: { module_count: number; edge_count: number; frameworks: string[]; maintainability_score: number } }
