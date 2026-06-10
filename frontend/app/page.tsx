"use client";

import Link from "next/link";

export default function HomePage() {
  return (
    <main style={styles.main}>
      <nav style={styles.nav}>
        <div style={styles.logo}>FutureReady</div>
        <div style={styles.navLinks}>
          <Link href="/dashboard" style={styles.link}>Dashboard</Link>
          <Link href="/login" style={styles.link}>Sign In</Link>
        </div>
      </nav>
      
      <section style={styles.hero}>
        <h1 style={styles.title}>
          AI-Powered<br />Full-Stack Generation
        </h1>
        <p style={styles.subtitle}>
          Describe your idea. Our 6 specialized agents build it.
        </p>
        <Link href="/dashboard" style={styles.cta}>
          Start Building →
        </Link>
      </section>

      <section style={styles.features}>
        <div style={styles.featureCard}>
          <h3>Requirements Analyst</h3>
          <p>Parses briefs into structured specs and user stories</p>
        </div>
        <div style={styles.featureCard}>
          <h3>Backend Developer</h3>
          <p>Generates FastAPI apps with auth, tests, and Docker</p>
        </div>
        <div style={styles.featureCard}>
          <h3>Frontend Developer</h3>
          <p>Builds Next.js apps with TypeScript and Tailwind</p>
        </div>
        <div style={styles.featureCard}>
          <h3>Database Architect</h3>
          <p>Designs PostgreSQL schemas and Alembic migrations</p>
        </div>
        <div style={styles.featureCard}>
          <h3>DevOps Engineer</h3>
          <p>CI/CD pipelines, Terraform, and monitoring</p>
        </div>
        <div style={styles.featureCard}>
          <h3>Report Generator</h3>
          <p>PDF and JSON reports from project artifacts</p>
        </div>
      </section>

      <footer style={styles.footer}>
        <p>© 2026 FutureReady. Built with OpenClaw + Hermes.</p>
      </footer>
    </main>
  );
}

const styles: Record<string, React.CSSProperties> = {
  main: {
    minHeight: "100vh",
    background: "linear-gradient(135deg, #0f172a 0%, #1e293b 100%)",
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
    transition: "color 0.2s",
  },
  hero: {
    textAlign: "center",
    padding: "6rem 2rem",
    maxWidth: "800px",
    margin: "0 auto",
  },
  title: {
    fontSize: "3.5rem",
    fontWeight: 800,
    lineHeight: 1.1,
    marginBottom: "1.5rem",
    background: "linear-gradient(90deg, #60a5fa, #a78bfa)",
    WebkitBackgroundClip: "text",
    WebkitTextFillColor: "transparent",
  },
  subtitle: {
    fontSize: "1.25rem",
    color: "#94a3b8",
    marginBottom: "2.5rem",
    lineHeight: 1.6,
  },
  cta: {
    display: "inline-block",
    padding: "0.875rem 2rem",
    background: "#3b82f6",
    color: "#fff",
    borderRadius: "0.5rem",
    fontWeight: 600,
    fontSize: "1rem",
  },
  features: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
    gap: "1.5rem",
    padding: "0 3rem 4rem",
    maxWidth: "1200px",
    margin: "0 auto",
  },
  featureCard: {
    padding: "1.5rem",
    background: "rgba(255,255,255,0.05)",
    borderRadius: "0.75rem",
    border: "1px solid rgba(255,255,255,0.1)",
  },
  footer: {
    textAlign: "center",
    padding: "2rem",
    borderTop: "1px solid rgba(255,255,255,0.1)",
    color: "#64748b",
    fontSize: "0.875rem",
  },
};
