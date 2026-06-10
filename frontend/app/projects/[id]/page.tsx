"use client";

import { useParams } from "next/navigation";
import Link from "next/link";

const PROJECT_ARTIFACTS: Record<string, { name: string; agents: { name: string; files: string[]; output: string }[] }> = {
  "1": {
    name: "E-Commerce Platform",
    agents: [
      { name: "Requirements Analyst", files: ["spec.md", "user-stories.json", "api-contract.yaml"], output: "12 user stories, REST API with 24 endpoints" },
      { name: "Database Architect", files: ["schema.sql", "models/user.py", "models/product.py", "models/order.py", "alembic/001_initial.py"], output: "8 entities, 12 relationships, indexes on search fields" },
      { name: "Backend Developer", files: ["app/main.py", "routers/auth.py", "routers/products.py", "routers/cart.py", "routers/orders.py", "services/stripe.py", "tests/test_orders.py", "Dockerfile"], output: "FastAPI app with JWT auth, Stripe integration, pytest suite" },
      { name: "Frontend Developer", files: ["app/page.tsx", "app/products/page.tsx", "app/product/[id]/page.tsx", "app/cart/page.tsx", "app/checkout/page.tsx", "app/admin/page.tsx", "components/ProductCard.tsx", "lib/api.ts"], output: "Next.js 14 app with 8 pages, cart state, admin dashboard" },
      { name: "DevOps Engineer", files: [".github/workflows/ci.yml", ".github/workflows/deploy.yml", "docker-compose.yml", "infra/terraform/main.tf", "render.yaml"], output: "CI/CD for test/build/deploy, Terraform AWS setup" },
      { name: "Report Generator", files: ["reports/project-summary.pdf", "reports/architecture.svg", "reports/test-coverage.html"], output: "68 total files, 94% test coverage, architecture diagram" },
    ],
  },
  "2": {
    name: "Task Management App",
    agents: [
      { name: "Requirements Analyst", files: ["spec.md", "user-stories.json"], output: "8 user stories, kanban workflow defined" },
      { name: "Database Architect", files: ["schema.sql", "models/user.py", "models/task.py", "models/board.py"], output: "5 entities, team/workspace model" },
      { name: "Backend Developer", files: ["app/main.py", "routers/auth.py", "routers/tasks.py", "routers/boards.py", "services/notifications.py"], output: "WebSocket support for real-time updates" },
      { name: "Frontend Developer", files: ["app/page.tsx", "app/board/page.tsx", "components/Kanban.tsx", "components/TaskCard.tsx"], output: "Drag-and-drop kanban with React DnD" },
      { name: "DevOps Engineer", files: [".github/workflows/ci.yml", "docker-compose.yml"], output: "Dockerized for easy local dev" },
      { name: "Report Generator", files: ["reports/summary.pdf"], output: "54 files generated" },
    ],
  },
  "3": {
    name: "Blog CMS",
    agents: [
      { name: "Requirements Analyst", files: ["spec.md"], output: "Markdown editor, image uploads, SEO" },
      { name: "Database Architect", files: ["schema.sql", "models/post.py", "models/tag.py"], output: "Post/Tag/Author models with full-text search" },
      { name: "Backend Developer", files: ["app/main.py", "routers/posts.py", "routers/upload.py", "services/seo.py"], output: "Image upload to S3, OpenGraph meta generation" },
      { name: "Frontend Developer", files: ["app/page.tsx", "app/blog/page.tsx", "app/blog/[slug]/page.tsx", "components/MarkdownEditor.tsx"], output: "SSR blog with MDX support" },
      { name: "DevOps Engineer", files: [".github/workflows/ci.yml"], output: "Vercel deploy config" },
      { name: "Report Generator", files: ["reports/summary.pdf"], output: "47 files generated" },
    ],
  },
};

export default function ProjectDetailPage() {
  const params = useParams();
  const projectId = params.id as string;
  const project = PROJECT_ARTIFACTS[projectId];

  if (!project) {
    return (
      <main style={styles.main}>
        <nav style={styles.nav}>
          <Link href="/" style={styles.logo}>FutureReady</Link>
        </nav>
        <div style={styles.container}>
          <h1>Project not found</h1>
          <Link href="/projects" style={styles.link}>← Back to Projects</Link>
        </div>
      </main>
    );
  }

  const totalFiles = project.agents.reduce((sum, a) => sum + a.files.length, 0);

  return (
    <main style={styles.main}>
      <nav style={styles.nav}>
        <Link href="/" style={styles.logo}>FutureReady</Link>
        <div style={styles.navLinks}>
          <Link href="/projects" style={styles.link}>Projects</Link>
          <Link href="/build" style={styles.cta}>+ New Build</Link>
        </div>
      </nav>

      <div style={styles.container}>
        <Link href="/projects" style={styles.backLink}>← All Projects</Link>

        <h1 style={styles.title}>{project.name}</h1>
        <p style={styles.meta}>
          {project.agents.length} agents · {totalFiles} files · Status: <span style={styles.status}>Complete</span>
        </p>

        <div style={styles.artifacts}>
          {project.agents.map((agent, i) => (
            <div key={agent.name} style={styles.agentSection}>
              <div style={styles.agentHeader}>
                <div style={{ ...styles.agentNum, background: ["#60a5fa", "#a78bfa", "#34d399", "#fbbf24", "#f87171", "#fb923c"][i] }}>
                  {i + 1}
                </div>
                <h3 style={styles.agentName}>{agent.name}</h3>
              </div>
              <p style={styles.agentOutput}>{agent.output}</p>
              <div style={styles.fileGrid}>
                {agent.files.map((f) => (
                  <div key={f} style={styles.fileCard}>{f}</div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}

const styles: Record<string, React.CSSProperties> = {
  main: { minHeight: "100vh", background: "linear-gradient(135deg, #0f172a 0%, #1e293b 100%)", color: "#f8fafc" },
  nav: { display: "flex", justifyContent: "space-between", alignItems: "center", padding: "1.5rem 3rem", borderBottom: "1px solid rgba(255,255,255,0.1)" },
  logo: { fontSize: "1.5rem", fontWeight: 800, background: "linear-gradient(90deg, #60a5fa, #a78bfa)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent", textDecoration: "none" },
  navLinks: { display: "flex", gap: "2rem", alignItems: "center" },
  link: { color: "#94a3b8", fontSize: "0.95rem", textDecoration: "none" },
  cta: { padding: "0.5rem 1rem", background: "#3b82f6", color: "#fff", borderRadius: "0.5rem", fontWeight: 600, fontSize: "0.875rem", textDecoration: "none" },
  container: { maxWidth: "900px", margin: "0 auto", padding: "3rem 2rem" },
  backLink: { display: "inline-block", color: "#94a3b8", marginBottom: "1.5rem", fontSize: "0.875rem", textDecoration: "none" },
  title: { fontSize: "2rem", fontWeight: 700, marginBottom: "0.5rem" },
  meta: { color: "#94a3b8", marginBottom: "2rem", fontSize: "0.875rem" },
  status: { color: "#34d399", fontWeight: 600 },
  artifacts: { display: "flex", flexDirection: "column", gap: "1.5rem" },
  agentSection: { padding: "1.5rem", background: "rgba(255,255,255,0.03)", borderRadius: "0.75rem", border: "1px solid rgba(255,255,255,0.1)" },
  agentHeader: { display: "flex", alignItems: "center", gap: "0.75rem", marginBottom: "0.75rem" },
  agentNum: { width: "28px", height: "28px", borderRadius: "50%", display: "flex", alignItems: "center", justifyContent: "center", fontSize: "0.75rem", fontWeight: 700, color: "#0f172a", flexShrink: 0 },
  agentName: { fontSize: "1rem", fontWeight: 600 },
  agentOutput: { color: "#94a3b8", fontSize: "0.875rem", marginBottom: "1rem" },
  fileGrid: { display: "flex", flexWrap: "wrap", gap: "0.5rem" },
  fileCard: { padding: "0.375rem 0.75rem", background: "rgba(255,255,255,0.05)", borderRadius: "0.375rem", fontSize: "0.75rem", fontFamily: "monospace", color: "#cbd5e1", border: "1px solid rgba(255,255,255,0.05)" },
};
