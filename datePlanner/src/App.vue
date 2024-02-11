<script setup>
import HelloWorld from './components/HelloWorld.vue'
import NavBar from './components/NavBar.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <header>
    <NavBar />
  </header>

  <main>
    <TheWelcome />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
  padding: 0;
  margin: 2;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

</style>
