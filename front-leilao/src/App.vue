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
#app {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f8f8f8;
}

.container {
  width: 90%;
  max-width: 800px;
  margin: 0 auto;
  background-color: #fff;
  padding: 0px 20px 20px;
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
