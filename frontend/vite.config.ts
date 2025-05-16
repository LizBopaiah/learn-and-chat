import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import path from "path";
import { componentTagger } from "lovable-tagger";

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => ({
  server: {
    host: "::",
    port: 8080,
  },
  plugins: [
    react(),
    mode === 'development' &&
    componentTagger(),
  ].filter(Boolean),
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  build: {
    // 🔥 Key changes start here
    outDir: "dist",       // Output built files to Flask's static folder
    assetsDir: ".",                    // Keep assets in the static root, not nested
    emptyOutDir: true,
    rollupOptions: {
      input: "./index.html",          // Use your React HTML entry point
    }
  },
  base: "/", // Ensure assets load correctly from root
}));
