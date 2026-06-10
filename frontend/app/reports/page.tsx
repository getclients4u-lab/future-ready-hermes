"use client";

import Link from "next/link";

export default function ReportsPage() {
  return (
    <main style={styles.main}>
      <nav style={styles.nav}>
        <Link href="/" style={styles.logo}>FutureReady</Link>
        <div style={styles.navLinks}>
          <Link href="/dashboard" style={styles.link}>Dashboard</Link>
          <Link href="/projects" style={styles.link}>Projects</Link>
        </div>
      </nav>

      <div style={styles.container}>
        <h1 style={styles.title}>Reports</h1>
        <p style={styles.subtitle}>Generated project summaries and audits</p>

        <div style={styles.empty}>
          <p>No reports yet.</p>
          <p style={styles.emptySub}>Reports are generated after each project build.</p>
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
  title: {
    fontSize: "2rem",
    fontWeight: 700,
    marginBottom: "0.5rem",
  },
  subtitle: {
    color: "#94a3b8",
    marginBottom: "2rem",
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
