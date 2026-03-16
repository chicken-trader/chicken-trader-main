<!--
  Running coin-yellow chicken (side profile, facing right).
  Uses the Mario UI Kit color palette.
  Props:
    size — rendered pixel width (height scales proportionally at 28/48 ratio)
-->
<template>
  <svg
    :width="size"
    :height="Math.round(size * 28 / 48)"
    viewBox="0 0 48 28"
    xmlns="http://www.w3.org/2000/svg"
    shape-rendering="crispEdges"
    aria-label="Chicken Trader logo"
  >
    <!-- Tail feathers (red / orange, left side, pointing upper-left) -->
    <rect x="0" y="6"  width="3" height="9"  fill="#E52521"/>
    <rect x="2" y="4"  width="3" height="11" fill="#FF8C00"/>
    <rect x="4" y="7"  width="3" height="7"  fill="#E52521"/>

    <!-- Body outline -->
    <rect x="5"  y="7"  width="22" height="13" fill="#000000"/>
    <rect x="6"  y="5"  width="20" height="15" fill="#000000"/>
    <rect x="7"  y="4"  width="18" height="17" fill="#000000"/>

    <!-- Body fill (coin yellow) -->
    <rect x="6"  y="8"  width="20" height="11" fill="#FBD000"/>
    <rect x="7"  y="6"  width="18" height="13" fill="#FBD000"/>
    <rect x="8"  y="5"  width="16" height="15" fill="#FBD000"/>

    <!-- Wing detail (darker yellow) -->
    <rect x="8"  y="8"  width="10" height="7"  fill="#D4A017"/>

    <!-- Neck -->
    <rect x="24" y="7"  width="5"  height="10" fill="#FBD000"/>

    <!-- Head outline -->
    <rect x="27" y="3"  width="13" height="14" fill="#000000"/>
    <rect x="28" y="2"  width="11" height="16" fill="#000000"/>

    <!-- Head fill -->
    <rect x="28" y="4"  width="11" height="12" fill="#FBD000"/>
    <rect x="29" y="3"  width="9"  height="14" fill="#FBD000"/>

    <!-- Comb (red, single bump — side view) -->
    <rect x="30" y="0"  width="6"  height="4"  fill="#E52521"/>
    <rect x="29" y="3"  width="9"  height="2"  fill="#E52521"/>

    <!-- Eye (black + white highlight) -->
    <rect x="35" y="6"  width="3"  height="3"  fill="#000000"/>
    <rect x="35" y="6"  width="1"  height="1"  fill="#FFFFFF"/>

    <!-- Beak (orange, pointing right) -->
    <rect x="38" y="8"  width="6"  height="2"  fill="#FF8C00"/>
    <rect x="39" y="10" width="5"  height="2"  fill="#FF8C00"/>
    <rect x="40" y="12" width="4"  height="1"  fill="#FF8C00"/>

    <!-- Wattle (red, under beak) -->
    <rect x="38" y="12" width="3"  height="4"  fill="#E52521"/>

    <!-- Legs — running pose (orange) -->
    <!-- Front leg (forward stride) -->
    <rect x="19" y="20" width="2"  height="5"  fill="#FF8C00"/>
    <rect x="16" y="24" width="5"  height="2"  fill="#FF8C00"/>
    <rect x="15" y="25" width="3"  height="2"  fill="#FF8C00"/>

    <!-- Back leg (kicking back) -->
    <rect x="12" y="19" width="2"  height="4"  fill="#FF8C00"/>
    <rect x="12" y="22" width="5"  height="2"  fill="#FF8C00"/>
    <rect x="9"  y="23" width="5"  height="2"  fill="#FF8C00"/>
  </svg>
</template>

<script setup lang="ts">
withDefaults(defineProps<{ size?: number }>(), { size: 48 });
</script>
