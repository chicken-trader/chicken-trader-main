<!--
  Jumping chicken loading indicator.
  Wraps ChickenLogo with a bounce animation and pulsing shadow.
  Props:
    size  — pixel width of the chicken (height scales proportionally)
    label — text shown below; pass empty string to hide
-->
<template>
  <div class="chicken-loader">
    <div class="chicken-loader__bounce">
      <ChickenLogo :size="size" />
    </div>
    <div
      class="chicken-loader__shadow"
      :style="{ width: `${Math.round(size * 0.56)}px` }"
    />
    <p v-if="label" class="chicken-loader__label">{{ label }}</p>
  </div>
</template>

<script setup lang="ts">
import ChickenLogo from "./ChickenLogo.vue";

withDefaults(defineProps<{ size?: number; label?: string }>(), {
  size: 64,
  label: "LOADING...",
});
</script>

<style scoped>
.chicken-loader {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem 0;
}

.chicken-loader__bounce {
  animation: chicken-bounce 0.55s ease-in-out infinite alternate;
}

.chicken-loader__shadow {
  height: 8px;
  background: rgba(0, 0, 0, 0.45);
  border-radius: 50%;
  margin-top: 4px;
  animation: chicken-shadow 0.55s ease-in-out infinite alternate;
}

.chicken-loader__label {
  font-family: var(--font-heading);
  font-size: 0.45rem;
  color: var(--mario-yellow);
  margin: 0.75rem 0 0;
  letter-spacing: 0.1em;
  animation: chicken-label-blink 1.1s step-start infinite;
}

@keyframes chicken-bounce {
  from { transform: translateY(0px); }
  to   { transform: translateY(-20px); }
}

@keyframes chicken-shadow {
  from { transform: scaleX(1);    opacity: 0.5; }
  to   { transform: scaleX(0.45); opacity: 0.15; }
}

@keyframes chicken-label-blink {
  0%, 49% { opacity: 1; }
  50%, 100% { opacity: 0; }
}
</style>
