<template>
    <div>
      <h1>Item Details</h1>
      <div v-if="item">
        <div>
          <label>Name:</label>
          <input v-model="editedItem.name" />
        </div>
        <div>
          <label>Description:</label>
          <textarea v-model="editedItem.description"></textarea>
        </div>
        <button @click="saveChanges">Save Changes</button>
        <button @click="goBack">Back</button>
      </div>
      <div v-else>
        <p>Loading...</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        item: null,
        editedItem: {
          name: '',
          description: ''
        },
        API_URL: 'http://localhost:8000/api/'
      };
    },
    async created() {
      await this.fetchItem();
    },
    methods: {
      async fetchItem() {
        try {
          const response = await axios.get(this.API_URL + `items/${this.$route.params.id}/`);
          this.item = response.data;
          this.editedItem = { ...this.item }; // Make a copy for editing
        } catch (error) {
          console.error('Error fetching item details:', error);
        }
      },
      async saveChanges() {
        try {
          await axios.put(this.API_URL + `items/${this.item.id}/`, this.editedItem);
          alert('Changes saved successfully!');
        } catch (error) {
          console.error('Error saving changes:', error);
          alert('Failed to save changes. Please try again.');
        }
        this.$router.push({ name: 'ItemList'});
      },
      goBack() {
        this.$router.push({ name: 'ItemList'});
      },
    }
  };
  </script>
  