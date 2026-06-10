"use client";

import { useState } from "react";
import Link from "next/link";

export default function NewProjectPage() {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    alert(`Creating project: ${name}`);
  };

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
        <h1 style={styles.title}>New Project</h1>
        <p style={styles.subtitle}>Describe what you want to build</p>

        <form onSubmit={handleSubmit} style={styles.form}>
          <label style={styles.label}>Project Name</label>
          <input
            type="text"
            placeholder="e.g., E-Commerce Platform"
            value={name}
            onChange={(e) => setName(e.target.value)}
            style={styles.input}
            required
          />

          <label style={styles.label}>Description</label>
          <textarea
            placeholder="Describe your project idea, features, and requirements..."
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            style={{ ...styles.input, minHeight: "120px", resize: "vertical" }}
            required
          />

          <button type="submit" style={styles.button}>
            Generate Project
          </button>
        </form>
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
    maxWidth: "600px",
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
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "1rem",
  },
  label: {
    fontSize: "0.875rem",
    fontWeight: 500,
    color: "#cbd5e1",
  },
  input: {
    padding: "0.75rem 1rem",
    background: "rgba(255,255,255,0.05)",
    border: "1px solid rgba(255,255,255,0.1)",
    borderRadius: "0.5rem",
    color: "#f8fafc",
    fontSize: "1rem",
    outline: "none",
  },
  button: {
    marginTop: "1rem",
    padding: "0.75rem 1rem",
    background: "#3b82f6",
    color: "#fff",
    border: "none",
    borderRadius: "0.5rem",
    fontSize: "1rem",
    fontWeight: 600,
    cursor: "pointer",
  },
};
