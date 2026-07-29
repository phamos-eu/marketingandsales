<template>
  <div class="flex h-screen w-screen overflow-hidden bg-surface-white">
    <!-- Sidebar -->
    <aside
      class="flex w-[15.5rem] shrink-0 flex-col border-r border-outline-gray-1 bg-surface-gray-1"
    >
      <div class="flex items-center gap-2.5 border-b border-outline-gray-1 px-3 py-3">
        <div
          class="flex h-7 w-7 shrink-0 items-center justify-center rounded bg-ink-gray-9 text-xs font-semibold text-surface-white"
        >
          MS
        </div>
        <div class="min-w-0">
          <div class="truncate text-base font-semibold text-ink-gray-9">Marketing and Sales</div>
          <div class="truncate text-xs text-ink-gray-5">
            Leads Management
          </div>
        </div>
      </div>

      <!-- Navigation -->
      <nav class="flex flex-1 flex-col gap-4 overflow-y-auto p-2">
        <div>
          <div class="px-2 pb-1 text-[11px] font-medium uppercase tracking-wide text-ink-gray-4">
            Sales
          </div>
          <div class="flex flex-col gap-0.5">
            <router-link
              to="/leads"
              class="group flex items-center gap-2 rounded px-2 py-1.5 text-sm text-ink-gray-7 hover:bg-surface-gray-2"
              active-class="!bg-surface-white !text-ink-gray-9 font-medium shadow-sm"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 shrink-0 text-ink-gray-5 group-[.router-link-active]:text-ink-gray-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
              </svg>
              <span class="truncate">Leads</span>
            </router-link>
          </div>
        </div>
      </nav>

      <!-- Bottom Links -->
      <div class="space-y-0.5 border-t border-outline-gray-1 p-2">
        <a
          class="flex items-center gap-2 rounded px-2 py-1.5 text-sm text-ink-gray-6 hover:bg-surface-gray-2 hover:text-ink-gray-8"
          href="/app"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="7" height="7"></rect>
            <rect x="14" y="3" width="7" height="7"></rect>
            <rect x="14" y="14" width="7" height="7"></rect>
            <rect x="3" y="14" width="7" height="7"></rect>
          </svg>
          Desk
        </a>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="flex min-w-0 flex-1 flex-col overflow-hidden bg-surface-white">
      <slot />
    </main>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>
