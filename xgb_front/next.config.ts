// next.config.ts
import type { NextConfig } from "next";


// For importing img from localhost:5001 to page.tsx
/** @type {import('next').NextConfig} */
const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: "http",
        hostname: "localhost",
        port: "5001",
        pathname: "**",
      },
    ],
  },
};

export default nextConfig;