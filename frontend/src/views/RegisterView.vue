<template>
  <div class="auth-shell">
    <div class="auth-logo">
      <ChickenLogo :size="96" style="margin-bottom:1rem;" />
      <h1>CHICKEN TRADER</h1>
      <p>AI-POWERED DAILY SIGNALS</p>
    </div>
    <div class="auth-card">
      <h2>CREATE ACCOUNT</h2>
      <AppInput v-model="email" type="email" label="Email" placeholder="player@example.com" />
      <AppInput v-model="password" type="password" label="Password" placeholder="••••••••" />

      <div class="mario-card mario-card--yellow" style="margin-bottom: 1.25rem; font-size: 0.78rem; line-height: 1.6;">
        <p style="margin: 0; color: #FFF;">
          ⚠️ The app provides AI-generated informational content only, not investment advice.
          You are solely responsible for your decisions. Information is as-is with no warranty;
          operator is not liable for trading losses.
        </p>
      </div>

      <div class="mario-checkbox-row">
        <input v-model="accepted" type="checkbox" class="mario-checkbox" id="disclaimer" />
        <label for="disclaimer" class="mario-checkbox-label">
          I accept the disclaimer and limitation of liability.
        </label>
      </div>

      <AppButton variant="primary" :full="true" @click="submit">JOIN THE QUEST</AppButton>
      <div v-if="store.error" class="mario-error">{{ store.error }}</div>
      <div v-if="message" class="mario-success">{{ message }}</div>
      <p style="margin-top: 1.25rem; font-size: 0.8rem; text-align: center;">
        Already a player? <RouterLink to="/login">Login here</RouterLink>
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
const accepted = ref(false);
const message = ref("");

async function submit() {
  await store.register(email.value, password.value, accepted.value);
  if (!store.error) {
    message.value = "Registration successful.";
    const redirect = typeof route.query.redirect === "string" ? route.query.redirect : "/";
    await router.push(redirect);
  }
}
</script>
