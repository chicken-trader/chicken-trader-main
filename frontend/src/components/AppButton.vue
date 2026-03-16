<template>
  <button
    :class="[
      'mario-btn',
      `mario-btn--${variant}`,
      size === 'sm' ? 'mario-btn--sm' : '',
      full ? 'mario-btn--full' : '',
    ]"
    :disabled="disabled"
    @click="$emit('click', $event)"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
withDefaults(
  defineProps<{
    variant?: "primary" | "secondary" | "danger";
    size?: "md" | "sm";
    full?: boolean;
    disabled?: boolean;
  }>(),
  {
    variant: "primary",
    size: "md",
    full: false,
    disabled: false,
  }
);

defineEmits<{ click: [e: MouseEvent] }>();
</script>
