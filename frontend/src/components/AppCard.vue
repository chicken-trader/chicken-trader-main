<template>
  <div
    :class="[
      'mario-card',
      color !== 'default' ? `mario-card--${color}` : '',
      clickable ? 'mario-card--clickable' : '',
    ]"
  >
    <slot />
  </div>
</template>

<script setup lang="ts">
withDefaults(
  defineProps<{
    color?: "default" | "yellow" | "red" | "blue" | "green";
    clickable?: boolean;
  }>(),
  { color: "default", clickable: false }
);
</script>
