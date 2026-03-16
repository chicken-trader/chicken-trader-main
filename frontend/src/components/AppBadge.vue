<template>
  <span :class="['mario-badge', `mario-badge--${variant}`]"><slot /></span>
</template>

<script setup lang="ts">
withDefaults(
  defineProps<{
    variant?: "active" | "hold" | "warning" | "sell" | "sector" | "ai" | "unread" | "brown";
  }>(),
  { variant: "sector" }
);
</script>
