export const metadata = {
  title: "Dashboard — FutureReady",
};

export default function DashboardPage() {
  return (
    <div className="container mx-auto py-10">
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        <ProjectCard title="New Project" description="Start a new build" href="/projects/new" />
        <ProjectCard title="My Projects" description="View all projects" href="/projects" />
        <ProjectCard title="Reports" description="Generate and download" href="/reports" />
      </div>
    </div>
  );
}

function ProjectCard({ title, description, href }: { title: string; description: string; href: string }) {
  return (
    <a
      href={href}
      className="rounded-lg border bg-card p-6 text-card-foreground shadow-sm transition-colors hover:bg-accent hover:text-accent-foreground"
    >
      <h3 className="text-lg font-semibold">{title}</h3>
      <p className="text-sm text-muted-foreground mt-2">{description}</p>
    </a>
  );
}
