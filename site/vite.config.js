import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api/uniswap': {
        target: 'https://trade-api.gateway.uniswap.org',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api\/uniswap/, ''),
      }
    }
  }
})
