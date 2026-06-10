"use client";

import { useState } from "react";
import Link from "next/link";

const DEMO_PROJECTS = [
  {
    id: "1",
    name: "E-Commerce Platform",
    description: "Product catalog, cart, Stripe checkout, admin dashboard",
    status: "complete",
    agents: 6,
    files: 68,
    createdAt: "2026-06-10",
  },
  {
    id: "2",
    name: "Task Management App",
    description: "Kanban board, team assignments, notifications",
    status: "complete",
    agents: 6,
    files: 54,
    createdAt: "2026-06-09",
  },
  {
    id: "3",
    name: "Blog CMS",
    description: "Markdown editor, image uploads, SEO optimization",
    status: "complete",
    agents: 6,
    files: 47,
    createdAt: "2026-06-08",
  },
];

export default function ProjectsPage() {
  const [projects] = useState(DEMO_PROJECTS);

  return (
    <main style={styles.main}>
      <nav style={styles.nav}>
        <Link href="/" style={styles.logo}>FutureReady</Link>
        <div style={styles.navLinks}>
          <Link href="/build" style={styles.cta}>+ New Build</Link>
          <Link href="/" style={styles.link}>Home</Link>
        </div>
      </nav>

      <div style={styles.container}>
        <div style={styles.header}>
          <h1 style={styles.title}>Projects</h1>
          <Link href="/build" style={styles.cta}>+ New Build</Link>
        </div>

        {projects.length === 0 ? (
          <div style={styles.empty}>
            <p>No projects yet.</p>
            <p style={styles.emptySub}>Start your first build to see it here.</p>
            <Link href="/build" style={styles.emptyCta}>Start Building</Link>
          </div>
        ) : (
          <div style={styles.projectList}>
            {projects.map((project) => (
              <div key={project.id} style={styles.projectCard}>
                <div style={styles.projectHeader}>
                  <div>
                    <h3 style={styles.projectName}>{project.name}</h3>
                    <p style={styles.projectDesc}>{project.description}</p>
                  </div>
                  <span style={styles.statusBadge}>{project.status}</span>
                </div>
                <div style={styles.projectMeta}>
                  <span>{project.agents} agents</span>
                  <span>{project.files} files</span>
                  <span>{project.createdAt}</span>
                </div>
                <Link href={`/projects/${project.id}`} style={styles.viewLink}>
                  View Artifacts →
                </Link>
              </div>
            ))}
          </div>
        )}
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
  container: { maxWidth: "1000px", margin: "0 auto", padding: "3rem 2rem" },
  header: { display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "2rem" },
  title: { fontSize: "2rem", fontWeight: 700 },
  empty: { textAlign: "center", padding: "4rem 2rem", color: "#94a3b8" },
  emptySub: { marginTop: "0.5rem", marginBottom: "1.5rem", fontSize: "0.875rem" },
  emptyCta: { padding: "0.75rem 1.5rem", background: "#3b82f6", color: "#fff", borderRadius: "0.5rem", fontWeight: 600, textDecoration: "none" },
  projectList: { display: "flex", flexDirection: "column", gap: "1rem" },
  projectCard: { padding: "1.5rem", background: "rgba(255,255,255,0.03)", borderRadius: "0.75rem", border: "1px solid rgba(255,255,255,0.1)" },
  projectHeader: { display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: "0.75rem" },
  projectName: { fontSize: "1.125rem", fontWeight: 600, marginBottom: "0.25rem" },
  projectDesc: { color: "#94a3b8", fontSize: "0.875rem" },
  statusBadge: { padding: "0.25rem 0.75rem", background: "rgba(52,211,153,0.15)", color: "#34d399", borderRadius: "999px", fontSize: "0.75rem", fontWeight: 600, textTransform: "uppercase" },
  projectMeta: { display: "flex", gap: "1.5rem", color: "#64748b", fontSize: "0.75rem", marginBottom: "1rem" },
  viewLink: { color: "#60a5fa", fontSize: "0.875rem", fontWeight: 500, textDecoration: "none" },
};
