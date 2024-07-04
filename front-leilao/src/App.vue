<template>
  <div id="app">
    <TopNavBar @dateChange="fetchSchedule" @toggleLive="toggleLiveEvents"/>
    <router-view /> <!-- This is where the components corresponding to the routes will be rendered -->
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
