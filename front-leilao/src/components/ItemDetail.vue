<template>
    <div>
      <button @click="logout">Logout</button>
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
import axiosInstance from '@/services/api';

export default {
  data() {
    return {
      item: null,
      editedItem: {
        name: '',
        description: ''
      }
    };
  },
  async created() {
    await this.fetchItem();
  },
  methods: {
    async fetchItem() {
      try {
        const response = await axiosInstance.get(`items/${this.$route.params.id}/`);
        this.item = response.data;
        this.editedItem = { ...this.item }; // Make a copy for editing
      } catch (error) {
        console.error('Error fetching item details:', error);
      }
    },
    async saveChanges() {
      try {
        await axiosInstance.put(`items/${this.item.id}/`, this.editedItem);
        alert('Changes saved successfully!');
        this.$router.push({ name: 'ItemList'});
      } catch (error) {
        console.error('Error saving changes:', error);
        alert('Failed to save changes. Please try again.');
      }
    },
    goBack() {
      this.$router.push({ name: 'ItemList'});
    },
    logout() {
      localStorage.removeItem('token'); // Remove the token from local storage
      this.$router.push('/login'); // Redirect to the login page
    },
  }
};
</script>
  