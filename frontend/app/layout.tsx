import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "FutureReady — AI-Powered Build Platform",
  description: "Generate production-ready full-stack applications with AI agents.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-background font-sans antialiased">
        {children}
      </body>
    </html>
  );
}
