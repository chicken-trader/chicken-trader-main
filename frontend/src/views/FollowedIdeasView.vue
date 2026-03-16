<template>
  <section>
    <div class="section-heading">
      <span style="font-size: 1.5rem;">⭐</span>
      <h2>FOLLOWED IDEAS</h2>
    </div>

    <div v-if="store.error" class="mario-error">{{ store.error }}</div>

    <div v-if="store.loading" class="mario-empty">
      <ChickenLoader />
    </div>

    <div v-else-if="store.items.length === 0 && !store.error" class="mario-empty">
      <p>NO IDEAS FOLLOWED YET</p>
      <p style="font-size: 0.45rem;">Head to Market to find investment ideas</p>
    </div>

    <AppCard
      v-for="thesis in store.items"
      :key="thesis.id"
      :color="stateColor(thesis.latest_state)"
      :class="thesis.latest_state?.toLowerCase() === 'sell' ? 'thesis-sell' : ''"
    >
      <div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 0.5rem; margin-bottom: 0.75rem; flex-wrap: wrap;">
        <h3 style="margin: 0;">
          {{ thesis.latest_state?.toLowerCase() === 'warning' ? '⚠️ ' : '' }}
          {{ thesis.latest_state?.toLowerCase() === 'sell' ? '🔴 ' : '' }}
          <router-link :to="'/opportunities/' + thesis.event_id" style="color: inherit; text-decoration: underline;">
            {{ thesis.report_headline || 'Event #' + thesis.event_id }}
          </router-link>
        </h3>
        <AppBadge :variant="stateVariant(thesis.latest_state)">{{ thesis.latest_state }}</AppBadge>
      </div>
      <p>{{ thesis.thesis_summary }}</p>
      <div style="display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 0.75rem; align-items: center;">
        <p style="font-size: 0.75rem; margin: 0; color: #aaa;">
          Followed: {{ formatDate(thesis.followed_at) }}
        </p>
        <p v-if="thesis.closed" style="font-size: 0.75rem; margin: 0; color: #aaa;">
          Closed ✓
        </p>
        <AppButton variant="danger" size="sm" style="margin-left: auto;" @click="unfollow(thesis.id)">
          Unfollow
        </AppButton>
      </div>
      <div v-if="thesis.latest_explanation" style="margin-top: 0.75rem; padding-top: 0.75rem; border-top: 1px solid #444;">
        <p style="font-size: 0.8rem; margin: 0;">{{ thesis.latest_explanation }}</p>
      </div>
    </AppCard>
  </section>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { useThesisStore } from "../stores/theses";
import AppCard from "../components/AppCard.vue";
import AppBadge from "../components/AppBadge.vue";
import AppButton from "../components/AppButton.vue";
import ChickenLoader from "../components/ChickenLoader.vue";

const store = useThesisStore();
onMounted(() => store.load());

function stateColor(state: string): "green" | "yellow" | "red" | "default" {
  const s = state?.toLowerCase();
  if (s === "active") return "green";
  if (s === "hold") return "yellow";
  if (s === "warning" || s === "sell") return "red";
  return "default";
}

function stateVariant(state: string): "active" | "hold" | "warning" | "sell" {
  const s = state?.toLowerCase();
  if (s === "active") return "active";
  if (s === "hold") return "hold";
  if (s === "warning") return "warning";
  if (s === "sell") return "sell";
  return "hold";
}

function formatDate(dateStr: string): string {
  if (!dateStr) return "";
  try {
    return new Date(dateStr).toLocaleDateString();
  } catch {
    return dateStr;
  }
}

async function unfollow(id: number) {
  if (!window.confirm("Unfollow this idea? This will permanently remove it from your followed list.")) return;
  try {
    await store.unfollow(id);
  } catch (e: any) {
    store.error = e.message;
  }
}
</script>
