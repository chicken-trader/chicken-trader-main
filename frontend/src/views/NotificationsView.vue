<template>
  <section>
    <div class="section-heading" style="justify-content: space-between; flex-wrap: wrap; gap: 0.5rem;">
      <div style="display: flex; align-items: center; gap: 0.75rem;">
        <span style="font-size: 1.5rem;">🔔</span>
        <h2 style="margin: 0;">
          ALERTS
          <AppBadge v-if="store.unreadCount > 0" variant="unread" style="margin-left: 0.5rem;">
            {{ store.unreadCount }}
          </AppBadge>
        </h2>
      </div>
      <AppButton v-if="store.unreadCount > 0" variant="secondary" size="sm" @click="store.markAllRead()">
        MARK ALL READ
      </AppButton>
    </div>

    <div v-if="store.error" class="mario-error">{{ store.error }}</div>

    <div v-if="store.loading" class="mario-empty">
      <ChickenLoader />
    </div>

    <div v-else-if="store.items.length === 0 && !store.error" class="mario-empty">
      <p>NO ALERTS YET</p>
    </div>

    <div
      v-for="n in store.items"
      :key="n.id"
      :class="['notif-item', n.read ? 'notif-item--read' : 'notif-item--unread']"
    >
      <AppCard>
        <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 0.75rem; margin-bottom: 0.75rem;">
          <h3 style="margin: 0; flex: 1;">{{ n.title }}</h3>
          <AppButton v-if="!n.read" variant="secondary" size="sm" @click="store.markRead(n.id)">
            MARK READ
          </AppButton>
          <span v-else class="mario-badge mario-badge--active" style="font-size: 0.4rem;">READ</span>
        </div>
        <p>{{ n.body }}</p>
        <div v-if="n.recommended_action" style="margin-top: 0.5rem;">
          <span class="mario-badge mario-badge--sector" style="margin-bottom: 0.4rem;">Action</span>
          <p style="margin-top: 0.4rem; font-size: 0.85rem;">{{ n.recommended_action }}</p>
        </div>
        <p style="font-size: 0.75rem; color: #888; margin: 0;">{{ n.created_at }}</p>
      </AppCard>
    </div>
  </section>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { useNotificationsStore } from "../stores/notifications";
import AppCard from "../components/AppCard.vue";
import AppBadge from "../components/AppBadge.vue";
import AppButton from "../components/AppButton.vue";
import ChickenLoader from "../components/ChickenLoader.vue";

const store = useNotificationsStore();
onMounted(() => store.load());
</script>
