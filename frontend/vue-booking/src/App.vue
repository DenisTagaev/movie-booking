<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Toast from 'primevue/toast';
</script>

<template>
  <div class="layout">
    <div class="content">
      <header>
        <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
      </header>
      <Toast />
      <RouterView />
    </div>
    <footer>
      <p>&copy; {{ new Date().getFullYear() }} Movie Booking App</p>
    </footer>
  </div>
</template>

<style scoped>

.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.content {
  flex: 1;
}

footer {
  text-align: center;
  padding: 1rem;
  font-size: 0.9rem;
}

header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}


@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
  }

  .logo {
    margin: 0 auto;
    display: block;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
