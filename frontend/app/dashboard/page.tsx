"use client";

import Link from "next/link";

export default function DashboardPage() {
  return (
    <main style={styles.main}>
      <nav style={styles.nav}>
        <Link href="/" style={styles.logo}>FutureReady</Link>
        <div style={styles.navLinks}>
          <Link href="/projects" style={styles.link}>Projects</Link>
          <Link href="/reports" style={styles.link}>Reports</Link>
          <Link href="/" style={styles.link}>Sign Out</Link>
        </div>
      </nav>

      <div style={styles.container}>
        <h1 style={styles.title}>Dashboard</h1>
        <p style={styles.subtitle}>Manage your AI-generated projects</p>

        <div style={styles.grid}>
          <div style={styles.card}>
            <h3 style={styles.cardTitle}>Active Projects</h3>
            <p style={styles.cardValue}>0</p>
          </div>
          <div style={styles.card}>
            <h3 style={styles.cardTitle}>Completed Builds</h3>
            <p style={styles.cardValue}>0</p>
          </div>
          <div style={styles.card}>
            <h3 style={styles.cardTitle}>Reports Generated</h3>
            <p style={styles.cardValue}>0</p>
          </div>
        </div>

        <div style={styles.actionSection}>
          <h2 style={styles.sectionTitle}>Start New Build</h2>
          <p style={styles.sectionDesc}>
            Describe your project idea and our agents will generate a complete full-stack application.
          </p>
          <Link href="/projects/new" style={styles.cta}>
            + New Project
          </Link>
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
    fontSize: "2.5rem",
    fontWeight: 700,
    marginBottom: "0.5rem",
  },
  subtitle: {
    color: "#94a3b8",
    marginBottom: "2rem",
  },
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))",
    gap: "1.5rem",
    marginBottom: "3rem",
  },
  card: {
    padding: "1.5rem",
    background: "rgba(255,255,255,0.05)",
    borderRadius: "0.75rem",
    border: "1px solid rgba(255,255,255,0.1)",
  },
  cardTitle: {
    fontSize: "0.875rem",
    color: "#94a3b8",
    marginBottom: "0.5rem",
  },
  cardValue: {
    fontSize: "2rem",
    fontWeight: 700,
  },
  actionSection: {
    padding: "2rem",
    background: "rgba(255,255,255,0.03)",
    borderRadius: "0.75rem",
    border: "1px solid rgba(255,255,255,0.1)",
    textAlign: "center",
  },
  sectionTitle: {
    fontSize: "1.5rem",
    fontWeight: 600,
    marginBottom: "0.5rem",
  },
  sectionDesc: {
    color: "#94a3b8",
    marginBottom: "1.5rem",
    maxWidth: "600px",
    marginLeft: "auto",
    marginRight: "auto",
  },
  cta: {
    display: "inline-block",
    padding: "0.75rem 1.5rem",
    background: "#3b82f6",
    color: "#fff",
    borderRadius: "0.5rem",
    fontWeight: 600,
  },
};
