<template>
  <div class="auth-shell">
    <div class="auth-logo">
      <ChickenLogo :size="96" style="margin-bottom:1rem;" />
      <h1>CHICKEN TRADER</h1>
      <p>AI-POWERED DAILY SIGNALS</p>
    </div>
    <div class="auth-card">
      <h2>PLAYER LOGIN</h2>
      <AppInput v-model="email" type="email" label="Email" placeholder="player@example.com" />
      <AppInput v-model="password" type="password" label="Password" placeholder="••••••••" />
      <AppButton variant="primary" :full="true" @click="submit">PRESS START</AppButton>
      <div v-if="store.error" class="mario-error">{{ store.error }}</div>
      <p style="margin-top: 1.25rem; font-size: 0.8rem; text-align: center;">
        New player?
        <RouterLink
          :to="{ path: '/register', query: route.query.redirect ? { redirect: route.query.redirect } : {} }"
        >Register here</RouterLink>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";
import AppInput from "../components/AppInput.vue";
import AppButton from "../components/AppButton.vue";
import ChickenLogo from "../components/ChickenLogo.vue";

const store = useAuthStore();
const route = useRoute();
const router = useRouter();
const email = ref("");
const password = ref("");

async function submit() {
  await store.login(email.value, password.value);
  if (!store.error) {
    const redirect = typeof route.query.redirect === "string" ? route.query.redirect : "/";
    await router.push(redirect);
  }
}
</script>
