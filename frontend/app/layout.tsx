import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "FutureReady \u2014 AI Build Platform",
  description: "Describe your idea. Our agents build it.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
