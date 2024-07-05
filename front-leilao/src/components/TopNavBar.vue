<template>
    <div class="top-nav">
      <div class="date-selector">
        <label for="date">Select Date: </label>
        <input type="date" v-model="selectedDate" @change="fetchSchedule"/>
      </div>
      <div class="toggle-options">
        <label>
          <input type="checkbox" v-model="showLiveEventsOnly" @change="toggleLiveEvents"/>
          Show Live Events Only
        </label>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        selectedDate: new Date().toISOString().substr(0, 10),
        showLiveEventsOnly: false,
      };
    },
    methods: {
      fetchSchedule() {
        // Fetch schedule for selected date
      },
      toggleLiveEvents() {
        // Toggle the live events filter
      },
    },
  };
  </script>
  
  <style>
  .top-nav {
    display: flex;
    justify-content: space-between;
    padding: 20px;
    background: #333;
    color: #fff;
  }
  </style>
  