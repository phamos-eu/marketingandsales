import { createRouter, createWebHistory } from 'vue-router'

const routes = [
	{
		path: '/',
		redirect: '/leads',
	},
	{
		path: '/leads',
		name: 'Leads',
		component: () => import('@/pages/Leads.vue'),
	},
]

const router = createRouter({
	history: createWebHistory('/sales'),
	routes,
})

export default router
