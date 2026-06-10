import Link from "next/link";

export default function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold tracking-tight lg:text-5xl mb-6">
        FutureReady
      </h1>
      <p className="text-lg text-muted-foreground mb-8 max-w-xl text-center">
        AI-powered full-stack code generation. Describe your idea, and our
        agents build it.
      </p>
      <div className="flex gap-4">
        <Link
          href="/dashboard"
          className="inline-flex items-center justify-center rounded-md bg-primary px-6 py-3 text-sm font-medium text-primary-foreground shadow transition-colors hover:bg-primary/90"
        >
          Get Started
        </Link>
        <Link
          href="/docs"
          className="inline-flex items-center justify-center rounded-md border border-input bg-background px-6 py-3 text-sm font-medium shadow-sm transition-colors hover:bg-accent hover:text-accent-foreground"
        >
          Documentation
        </Link>
      </div>
    </main>
  );
}
