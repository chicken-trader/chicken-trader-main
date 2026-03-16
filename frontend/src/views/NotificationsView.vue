<template>
  <section>
    <div style="display:flex; justify-content:space-between; align-items:center;">
      <h2>Notifications Center</h2>
      <button v-if="store.unreadCount > 0" @click="store.markAllRead()">
        Mark all as read ({{ store.unreadCount }})
      </button>
    </div>
    <p v-if="store.items.length === 0 && !store.error">No notifications yet.</p>
    <div
      v-for="n in store.items"
      :key="n.id"
      class="card"
      :style="{ opacity: n.read ? 0.6 : 1, borderLeft: n.read ? '3px solid #ccc' : '3px solid #2563eb' }"
    >
      <div style="display:flex; justify-content:space-between; align-items:flex-start;">
        <h3>{{ n.title }}</h3>
        <button v-if="!n.read" @click="store.markRead(n.id)" style="font-size:0.8rem;">
          Mark as read
        </button>
        <span v-else style="font-size:0.8rem; color:#6b7280;">Read</span>
      </div>
      <p>{{ n.body }}</p>
      <p><strong>Suggested action:</strong> {{ n.recommended_action }}</p>
      <p style="font-size:0.8rem; color:#6b7280;">{{ n.created_at }}</p>
    </div>
    <p v-if="store.error" style="color:red;">{{ store.error }}</p>
  </section>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { useNotificationsStore } from "../stores/notifications";

const store = useNotificationsStore();
onMounted(() => store.load());
</script>
