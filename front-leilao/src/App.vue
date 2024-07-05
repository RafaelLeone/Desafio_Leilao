<template>
  <div id="app">
    <div class="container">
      <main>
        <TopNavBar @dateChange="fetchSchedule" @toggleLive="toggleLiveEvents"/>
        <router-view /> <!-- This is where the components corresponding to the routes will be rendered -->
      </main>
    </div>
  </div>
</template>

<script>
import TopNavBar from './components/TopNavBar.vue';

export default {
  components: {
    TopNavBar,
  },
  // No need to import any components here since they will be rendered dynamically based on the routes
};
</script>

<style scoped>
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  font-family: Arial, sans-serif;
}

#app {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f8f8f8;
}

.container {
  width: 90%;
  max-width: 800px;
  margin: 0 auto;
  background-color: #fff;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

header {
  text-align: center;
  margin-bottom: 20px;
}

main {
  /* Your main content styles */
}

@media (max-width: 768px) {
  .container {
    width: 95%;
    padding: 10px;
  }
}
</style>
