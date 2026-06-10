"use client";

import Link from "next/link";

export default function ProjectsPage() {
  return (
    <main style={styles.main}>
      <nav style={styles.nav}>
        <Link href="/" style={styles.logo}>FutureReady</Link>
        <div style={styles.navLinks}>
          <Link href="/dashboard" style={styles.link}>Dashboard</Link>
          <Link href="/reports" style={styles.link}>Reports</Link>
        </div>
      </nav>

      <div style={styles.container}>
        <div style={styles.header}>
          <h1 style={styles.title}>Projects</h1>
          <Link href="/projects/new" style={styles.cta}>+ New Project</Link>
        </div>

        <div style={styles.empty}>
          <p>No projects yet.</p>
          <p style={styles.emptySub}>Create your first project to get started.</p>
        </div>
      </div>
    </main>
  );
}

const styles: Record<string, React.CSSProperties> = {
  main: {
    minHeight: "100vh",
    background: "linear-gradient(135deg, #0f172a 0%, #1e293b 100%)",
    color: "#f8fafc",
  },
  nav: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "1.5rem 3rem",
    borderBottom: "1px solid rgba(255,255,255,0.1)",
  },
  logo: {
    fontSize: "1.5rem",
    fontWeight: 800,
    background: "linear-gradient(90deg, #60a5fa, #a78bfa)",
    WebkitBackgroundClip: "text",
    WebkitTextFillColor: "transparent",
  },
  navLinks: {
    display: "flex",
    gap: "2rem",
  },
  link: {
    color: "#94a3b8",
    fontSize: "0.95rem",
  },
  container: {
    maxWidth: "1200px",
    margin: "0 auto",
    padding: "3rem 2rem",
  },
  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: "2rem",
  },
  title: {
    fontSize: "2rem",
    fontWeight: 700,
  },
  cta: {
    padding: "0.5rem 1rem",
    background: "#3b82f6",
    color: "#fff",
    borderRadius: "0.5rem",
    fontWeight: 600,
    fontSize: "0.875rem",
  },
  empty: {
    textAlign: "center",
    padding: "4rem 2rem",
    color: "#94a3b8",
  },
  emptySub: {
    marginTop: "0.5rem",
    fontSize: "0.875rem",
  },
};
