<template>
  <div class="landing-shell">
    <!-- Nav bar -->
    <nav class="landing-nav">
      <div class="landing-nav__brand">
        <ChickenLogo :size="32" />
        <span class="landing-nav__title">CHICKEN TRADER</span>
      </div>
      <AppButton variant="secondary" size="sm" @click="router.push('/login')">LOG IN</AppButton>
    </nav>

    <!-- Hero section -->
    <section class="landing-hero">
      <ChickenLogo :size="96" class="landing-hero__logo" />
      <h1 class="landing-hero__title">CHICKEN TRADER</h1>
      <p class="landing-hero__slogan">Don't be a chicken,<br>break some eggs!</p>
    </section>

    <!-- About section -->
    <section class="landing-about">
      <div class="landing-about__inner">
        <h2 class="landing-about__heading">WHAT IS THIS?</h2>
        <p class="landing-about__desc">
          Chicken Trader scans the news every day, clusters related events, and uses AI to surface
          structured investment opportunities — complete with suggested securities, thesis tracking,
          and automated re-evaluation so you never miss a signal.
        </p>
        <h3 class="landing-about__features-heading">KEY FEATURES</h3>
        <ul class="landing-features">
          <li class="landing-features__item">
            <span class="landing-features__icon">📰</span>
            <span>AI-driven daily investment opportunity discovery from live news</span>
          </li>
          <li class="landing-features__item">
            <span class="landing-features__icon">🔗</span>
            <span>News ingestion and automatic event clustering</span>
          </li>
          <li class="landing-features__item">
            <span class="landing-features__icon">📊</span>
            <span>Structured investment reports with suggested securities and market impact</span>
          </li>
          <li class="landing-features__item">
            <span class="landing-features__icon">⭐</span>
            <span>Thesis following with lifecycle tracking (Active → Warning → Close Suggested)</span>
          </li>
          <li class="landing-features__item">
            <span class="landing-features__icon">🔔</span>
            <span>Automated AI reevaluation and real-time user notifications</span>
          </li>
        </ul>
      </div>
    </section>

    <!-- Call to action -->
    <section class="landing-cta">
      <p class="landing-cta__prompt">Ready to start trading smarter?</p>
      <AppButton variant="primary" size="md" @click="router.push('/register')">
        REGISTER NOW
      </AppButton>
    </section>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
import AppButton from "../components/AppButton.vue";
import ChickenLogo from "../components/ChickenLogo.vue";

const router = useRouter();
</script>

<style scoped>
.landing-shell {
  min-height: 100vh;
  background: var(--mario-black);
  display: flex;
  flex-direction: column;
  padding-bottom: 0;
}

/* Nav */
.landing-nav {
  background: var(--mario-red);
  border-bottom: var(--pixel-border);
  box-shadow: 0 4px 0 #000;
  padding: 0.875rem 1.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 50;
}

.landing-nav__brand {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.landing-nav__title {
  font-family: var(--font-heading);
  font-size: 0.55rem;
  color: var(--mario-yellow);
  text-shadow: 2px 2px 0 #000;
  letter-spacing: 0.05em;
}

/* Hero */
.landing-hero {
  padding: 3.5rem 1.25rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 1rem;
}

.landing-hero__logo {
  filter: drop-shadow(4px 4px 0 #000);
}

.landing-hero__title {
  font-family: var(--font-heading);
  font-size: clamp(0.9rem, 4vw, 1.4rem);
  color: var(--mario-yellow);
  text-shadow: 3px 3px 0 #000;
  margin: 0;
  line-height: 1.6;
}

.landing-hero__slogan {
  font-family: var(--font-heading);
  font-size: clamp(0.4rem, 2vw, 0.6rem);
  color: var(--mario-white);
  text-shadow: 2px 2px 0 #000;
  margin: 0;
  line-height: 2;
  letter-spacing: 0.05em;
}

/* About */
.landing-about {
  flex: 1;
  padding: 2.5rem 1.25rem;
}

.landing-about__inner {
  max-width: 640px;
  margin: 0 auto;
}

.landing-about__heading {
  color: var(--mario-yellow);
  font-size: 0.65rem;
  margin-bottom: 1rem;
}

.landing-about__desc {
  font-family: var(--font-body);
  font-size: 0.9rem;
  color: var(--mario-white-dim);
  line-height: 1.7;
  margin-bottom: 2rem;
}

.landing-about__features-heading {
  color: var(--mario-yellow);
  font-size: 0.55rem;
  margin-bottom: 1rem;
}

/* Feature list */
.landing-features {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.landing-features__item {
  display: flex;
  align-items: flex-start;
  gap: 0.9rem;
  background: var(--mario-panel);
  border: var(--pixel-border);
  box-shadow: var(--pixel-shadow);
  padding: 0.875rem 1rem;
  font-size: 0.85rem;
  color: var(--mario-white-dim);
  line-height: 1.5;
}

.landing-features__icon {
  font-size: 1.1rem;
  flex-shrink: 0;
  line-height: 1.5;
}

/* CTA */
.landing-cta {
  padding: 3rem 1.25rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.25rem;
  background: var(--mario-panel);
  border-top: var(--pixel-border);
  box-shadow: 0 -4px 0 #000;
  text-align: center;
}

.landing-cta__prompt {
  font-family: var(--font-heading);
  font-size: 0.5rem;
  color: var(--mario-white-dim);
  margin: 0;
  letter-spacing: 0.05em;
  line-height: 2;
}
</style>
