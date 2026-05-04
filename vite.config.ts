import { defineConfig } from "vite";

const port = Number(process.env.PORT) || 4173;
const basePath = process.env.BASE_PATH || "/";

export default defineConfig({
  base: basePath,
  build: {
    outDir: "dist",
    emptyOutDir: true,
  },
  server: {
    port,
    strictPort: true,
    host: "0.0.0.0",
    allowedHosts: true,
  },
  preview: {
    port,
    host: "0.0.0.0",
    allowedHosts: true,
  },
});
