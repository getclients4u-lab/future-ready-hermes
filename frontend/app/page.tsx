"use client";

import Link from "next/link";

export default function HomePage() {
  return (
    <main style={styles.main}>
      <nav style={styles.nav}>
        <div style={styles.logo}>FutureReady</div>
        <div style={styles.navLinks}>
          <Link href="/projects" style={styles.link}>Projects</Link>
          <Link href="/build" style={styles.ctaNav}>Start Building</Link>
        </div>
      </nav>

      <section style={styles.hero}>
        <h1 style={styles.title}>
          AI Agents That<br />Build Full-Stack Apps
        </h1>
        <p style={styles.subtitle}>
          Describe your idea. Our 6 specialized agents generate
          production-ready code in minutes.
        </p>
        <Link href="/build" style={styles.cta}>
          Start Building →
        </Link>
      </section>

      <section style={styles.pipelineSection}>
        <h2 style={styles.sectionTitle}>The Pipeline</h2>
        <div style={styles.pipeline}>
          {[
            { name: "Requirements Analyst", color: "#60a5fa", desc: "Parses brief into specs" },
            { name: "Database Architect", color: "#a78bfa", desc: "Designs schema & migrations" },
            { name: "Backend Developer", color: "#34d399", desc: "Generates FastAPI code" },
            { name: "Frontend Developer", color: "#fbbf24", desc: "Generates Next.js code" },
            { name: "DevOps Engineer", color: "#f87171", desc: "CI/CD & infrastructure" },
            { name: "Report Generator", color: "#fb923c", desc: "PDF & JSON summaries" },
          ].map((agent, i) => (
            <div key={agent.name} style={styles.pipelineStep}>
              <div style={{ ...styles.stepDot, background: agent.color }}>{i + 1}</div>
              <div style={styles.stepContent}>
                <strong>{agent.name}</strong>
                <span style={styles.stepDesc}>{agent.desc}</span>
              </div>
              {i < 5 && <div style={styles.stepArrow}>→</div>}
            </div>
          ))}
        </div>
      </section>

      <section style={styles.features}>
        <h2 style={styles.sectionTitle}>What You Get</h2>
        <div style={styles.featureGrid}>
          {[
            { title: "Complete Repo", desc: "50+ files with full project structure" },
            { title: "Working Backend", desc: "FastAPI with auth, CRUD, tests" },
            { title: "Working Frontend", desc: "Next.js with routing, forms, API calls" },
            { title: "Database Schema", desc: "PostgreSQL + Alembic migrations" },
            { title: "CI/CD Pipeline", desc: "GitHub Actions for deploy" },
            { title: "PDF Report", desc: "Project summary & architecture" },
          ].map((f) => (
            <div key={f.title} style={styles.featureCard}>
              <h3>{f.title}</h3>
              <p>{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      <footer style={styles.footer}>
        <p>© 2026 FutureReady. OpenClaw + Hermes.</p>
      </footer>
    </main>
  );
}

const styles: Record<string, React.CSSProperties> = {
  main: { minHeight: "100vh", background: "linear-gradient(135deg, #0f172a 0%, #1e293b 100%)", color: "#f8fafc" },
  nav: { display: "flex", justifyContent: "space-between", alignItems: "center", padding: "1.5rem 3rem", borderBottom: "1px solid rgba(255,255,255,0.1)" },
  logo: { fontSize: "1.5rem", fontWeight: 800, background: "linear-gradient(90deg, #60a5fa, #a78bfa)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" },
  navLinks: { display: "flex", gap: "2rem", alignItems: "center" },
  link: { color: "#94a3b8", fontSize: "0.95rem" },
  ctaNav: { padding: "0.5rem 1rem", background: "#3b82f6", color: "#fff", borderRadius: "0.5rem", fontWeight: 600, fontSize: "0.875rem" },
  hero: { textAlign: "center", padding: "6rem 2rem", maxWidth: "800px", margin: "0 auto" },
  title: { fontSize: "3.5rem", fontWeight: 800, lineHeight: 1.1, marginBottom: "1.5rem", background: "linear-gradient(90deg, #60a5fa, #a78bfa)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" },
  subtitle: { fontSize: "1.25rem", color: "#94a3b8", marginBottom: "2.5rem", lineHeight: 1.6 },
  cta: { display: "inline-block", padding: "1rem 2.5rem", background: "#3b82f6", color: "#fff", textDecoration: "none", borderRadius: "0.5rem", fontWeight: 600, fontSize: "1.1rem" },
  pipelineSection: { padding: "4rem 2rem", maxWidth: "1200px", margin: "0 auto" },
  sectionTitle: { fontSize: "1.75rem", fontWeight: 700, textAlign: "center", marginBottom: "2rem" },
  pipeline: { display: "flex", flexWrap: "wrap", justifyContent: "center", gap: "1rem", alignItems: "center" },
  pipelineStep: { display: "flex", alignItems: "center", gap: "0.75rem", padding: "1rem", background: "rgba(255,255,255,0.05)", borderRadius: "0.75rem", border: "1px solid rgba(255,255,255,0.1)", minWidth: "200px" },
  stepDot: { width: "28px", height: "28px", borderRadius: "50%", display: "flex", alignItems: "center", justifyContent: "center", fontSize: "0.75rem", fontWeight: 700, color: "#0f172a", flexShrink: 0 },
  stepContent: { display: "flex", flexDirection: "column", fontSize: "0.875rem" },
  stepDesc: { color: "#94a3b8", fontSize: "0.75rem" },
  stepArrow: { color: "#64748b", fontSize: "1.25rem", fontWeight: 700 },
  features: { padding: "4rem 2rem", maxWidth: "1200px", margin: "0 auto" },
  featureGrid: { display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))", gap: "1.5rem" },
  featureCard: { padding: "1.5rem", background: "rgba(255,255,255,0.05)", borderRadius: "0.75rem", border: "1px solid rgba(255,255,255,0.1)" },
  footer: { textAlign: "center", padding: "2rem", borderTop: "1px solid rgba(255,255,255,0.1)", color: "#64748b", fontSize: "0.875rem" },
};