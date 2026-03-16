<template>
  <section>
    <div class="section-heading">
      <span style="font-size: 1.5rem;">👁</span>
      <h2>WATCHLIST</h2>
    </div>

    <AppCard color="yellow" style="margin-bottom: 1.5rem;">
      <h3 style="color: #000; margin-bottom: 1rem;">ADD SECURITY</h3>
      <AppInput v-model="ticker" label="Ticker Symbol" placeholder="e.g. AAPL" />
      <AppInput v-model="assetName" label="Asset Name" placeholder="e.g. Apple Inc." />
      <AppButton variant="primary" @click="add">+ ADD TO WATCHLIST</AppButton>
      <div v-if="message" :class="message.includes('Error') || message.includes('error') ? 'mario-error' : 'mario-success'" style="margin-top: 0.75rem;">
        {{ message }}
      </div>
    </AppCard>

    <div v-if="loading" class="mario-empty">
      <ChickenLoader />
    </div>

    <div v-else-if="items.length === 0" class="mario-empty">
      <p>WATCHLIST EMPTY</p>
      <p style="font-size: 0.45rem;">Add tickers above to start tracking</p>
    </div>

    <AppCard v-for="w in items" :key="w.id">
      <div style="display: flex; align-items: center; justify-content: space-between; gap: 0.75rem; flex-wrap: wrap;">
        <div style="display: flex; align-items: center; gap: 0.75rem;">
          <span class="ticker-chip">{{ w.ticker }}</span>
          <span style="color: var(--mario-white-dim); font-size: 0.9rem;">{{ w.asset_name }}</span>
        </div>
        <AppButton variant="danger" size="sm" @click="remove(w.id)">REMOVE</AppButton>
      </div>
    </AppCard>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { api } from "../stores/api";
import AppCard from "../components/AppCard.vue";
import AppInput from "../components/AppInput.vue";
import AppButton from "../components/AppButton.vue";
import ChickenLoader from "../components/ChickenLoader.vue";

const items = ref<any[]>([]);
const ticker = ref("");
const assetName = ref("");
const message = ref("");
const loading = ref(false);

async function load() {
  loading.value = true;
  try { items.value = await api("/watchlist"); }
  catch (e: any) { message.value = e.message; }
  finally { loading.value = false; }
}

async function add() {
  try {
    await api("/watchlist", { method: "POST", body: JSON.stringify({ ticker: ticker.value, asset_name: assetName.value }) });
    ticker.value = "";
    assetName.value = "";
    message.value = "";
    await load();
  } catch (e: any) {
    message.value = e.message;
  }
}

async function remove(id: number) {
  await api(`/watchlist/${id}`, { method: "DELETE" });
  await load();
}

onMounted(load);
</script>
