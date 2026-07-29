import vue from '@vitejs/plugin-vue'
import frappeui from 'frappe-ui/vite'
import path from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
	define: {
		__VUE_PROD_HYDRATION_MISMATCH_DETAILS__: 'false',
	},
	plugins: [
		vue(),
		frappeui({
			frappeProxy: true,
			lucideIcons: true,
			jinjaBootData: true,
			frontendRoute: '/sales',
			buildConfig: {
				outDir: '../marketingandsales/public/frontend',
				baseUrl: '/assets/marketingandsales/frontend/',
				indexHtmlPath: '../marketingandsales/www/sales.html',
				emptyOutDir: true,
				sourcemap: true,
			},
		}),
	],
	server: {
		allowedHosts: true,
	},
	resolve: {
		alias: {
			'@': path.resolve(__dirname, 'src'),
		},
	},
	optimizeDeps: {
		include: [
			'frappe-ui > feather-icons',
			'showdown',
			'tailwind.config.js',
		],
	},
})
