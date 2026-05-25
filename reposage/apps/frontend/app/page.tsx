import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="min-h-screen p-10">
      <h1 className="text-5xl font-bold text-fuchsia-400">RepoSage</h1>
      <p className="mt-4 max-w-2xl text-cyan-200">Autonomous repository cognition and maintenance platform.</p>
      <div className="mt-8 flex gap-4">
        <Link href="/dashboard" className="rounded border border-cyan-400 px-4 py-2">Dashboard</Link>
        <Link href="/activity" className="rounded border border-fuchsia-400 px-4 py-2">Activity</Link>
      </div>
    </main>
  );
}
