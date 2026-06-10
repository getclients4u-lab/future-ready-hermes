/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true,
  },
  env: {
    API_BASE_URL: process.env.API_BASE_URL || "http://localhost:8000",
  },
  images: {
    domains: ["localhost"],
  },
};

module.exports = nextConfig;
