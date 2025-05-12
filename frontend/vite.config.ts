// frontend/vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: true,   // binds on 0.0.0.0 so localhost/127.0.0.1 and network IP work
    port: 5173,
    proxy: {
      '/reviews': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/games': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
    },
  },
})
