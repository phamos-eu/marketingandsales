<template>
  <AppShell>
    <div class="flex min-h-0 flex-1 overflow-hidden">
      <!-- Main Content -->
      <section class="flex min-w-0 flex-1 flex-col overflow-hidden">
        <header
          class="flex shrink-0 items-center justify-between gap-3 border-b border-outline-gray-1 px-5 py-3"
        >
          <div>
            <h1 class="text-xl font-semibold text-ink-gray-9">Leads</h1>
            <p class="text-sm text-ink-gray-5">
              List of all leads in the system.
            </p>
          </div>
        </header>

        <!-- Leads Table -->
        <div class="min-h-0 flex-1 overflow-y-auto p-4">
          <div v-if="loading" class="flex items-center justify-center h-full">
            <p class="text-ink-gray-5">Loading leads...</p>
          </div>
          <div v-else-if="error" class="flex flex-col items-center justify-center gap-3 h-full">
            <p class="text-red-500">{{ error }}</p>
            <button
              @click="fetchLeads"
              class="px-4 py-2 bg-ink-gray-9 text-white rounded-md text-sm"
            >
              Retry
            </button>
          </div>
          <div v-else>
            <table class="w-full text-left border-collapse">
              <thead>
                <tr class="border-b border-outline-gray-1">
                  <th class="px-4 py-3 text-sm font-medium text-ink-gray-5 uppercase tracking-wide">
                    Name
                  </th>
                  <th class="px-4 py-3 text-sm font-medium text-ink-gray-5 uppercase tracking-wide">
                    Status
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="lead in leads"
                  :key="lead.name"
                  class="border-b border-outline-gray-1 hover:bg-surface-gray-1"
                >
                  <td class="px-4 py-3 text-sm text-ink-gray-9">
                    {{ lead.name }}
                  </td>
                  <td class="px-4 py-3 text-sm text-ink-gray-7">
                    <span
                      class="px-2 py-1 rounded-full text-xs font-medium"
                      :class="getStatusColor(lead.status)"
                    >
                      {{ lead.status }}
                    </span>
                  </td>
                </tr>
                <tr v-if="leads.length === 0">
                  <td colspan="2" class="px-4 py-6 text-center text-sm text-ink-gray-5">
                    No leads found.
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </div>
  </AppShell>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import AppShell from '@/components/AppShell.vue'

const leads = ref([])
const loading = ref(true)
const error = ref(null)

const fetchLeads = async () => {
  try {
    loading.value = true
    error.value = null
    const response = await window.frappe.call('marketingandsales.api.leads.get_leads')
    leads.value = response.message || []
  } catch (e) {
    error.value = e.message || 'Failed to fetch leads'
    console.error('Error fetching leads:', e)
  } finally {
    loading.value = false
  }
}

const getStatusColor = (status) => {
  const statusColors = {
    'Open': 'bg-blue-100 text-blue-800',
    'Replied': 'bg-yellow-100 text-yellow-800',
    'Interested': 'bg-green-100 text-green-800',
    'Converted': 'bg-purple-100 text-purple-800',
    'Lost': 'bg-red-100 text-red-800',
    'Do Not Contact': 'bg-gray-100 text-gray-800',
  }
  return statusColors[status] || 'bg-gray-100 text-gray-800'
}

onMounted(fetchLeads)
</script>
