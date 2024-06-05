<template>
  <div>
    <div v-if="item">
      <h1>{{ item.name }}</h1>
      <p>{{ item.description }}</p>
      <p>{{ item.creator_username }}</p>
      <div v-if="isEditor">
        <input v-model="editedItem.name" placeholder="Name" />
        <input v-model="editedItem.description" placeholder="Description" />
        <button @click="saveChanges">Save Changes</button>
      </div>
      <button @click="goBack">Back</button>
    </div>
  </div>
</template>

<script>
import { getItem, updateItem } from '@/services/api';

export default {
  data() {
    return {
      item: null,
      editedItem: {
        name: '',
        description: ''
      },
      isEditor: false
    };
  },
  async created() {
    await this.fetchItem();
    this.checkRole();
  },
  methods: {
    async fetchItem() {
      try {
        const response = await getItem(this.$route.params.id);
        this.item = response;
        this.editedItem = { ...this.item };
      } catch (error) {
        console.error('Error fetching item details:', error);
        this.$router.push('/login');
      }
    },
    async saveChanges() {
      try {
        await updateItem(this.item.id, this.editedItem);
        alert('Changes saved successfully!');
      } catch (error) {
        console.error('Error saving changes:', error);
        alert('Failed to save changes. Please try again.');
      }
      this.$router.push({ name: 'ItemList' });
    },
    goBack() {
      this.$router.push({ name: 'ItemList' });
    },
    checkRole() {
      const username = localStorage.getItem('username');
      this.isEditor = username && username.length === 14;
    }
  }
};
</script>
