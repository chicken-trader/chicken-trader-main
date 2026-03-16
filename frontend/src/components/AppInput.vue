<template>
  <div class="mario-field">
    <label v-if="label" class="mario-label" :for="inputId">{{ label }}</label>
    <input
      :id="inputId"
      class="mario-input"
      :type="type"
      :value="modelValue"
      :placeholder="placeholder"
      @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
    />
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";

const props = withDefaults(
  defineProps<{
    modelValue?: string;
    type?: string;
    label?: string;
    placeholder?: string;
  }>(),
  { type: "text", modelValue: "" }
);

defineEmits<{ "update:modelValue": [value: string] }>();

const inputId = computed(() => `input-${Math.random().toString(36).slice(2, 9)}`);
</script>
