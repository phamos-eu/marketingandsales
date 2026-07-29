// Rollup config for Frappe build compatibility
// This file is required for Frappe's bench build to work
// The actual frontend is built separately via Vite

import { nodeResolve } from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';

export default {
	input: 'src/index.js',
	output: {
		file: 'dist/bundle.js',
		format: 'iife',
		name: 'MarketingAndSales',
		globals: {
			vue: 'Vue',
			'vue-router': 'VueRouter',
			'frappe-ui': 'FrappeUI',
		},
	},
	plugins: [
		nodeResolve(),
		commonjs(),
	],
	external: ['vue', 'vue-router', 'frappe-ui'],
};
