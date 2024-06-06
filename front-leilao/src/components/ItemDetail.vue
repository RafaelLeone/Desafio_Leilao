<template>
  <div>
    <div v-if="item">
      <h1>Leilão {{ item.id }}</h1>
      <p>{{ item.category }} auction</p>
      <p>Auction Date: {{ item.auction_date }}</p>
      <p>by {{ item.creator_username }}</p>
      <div v-if="item.category === 'Real Estate'">
        <h2>Real Estates</h2>
        <ul>
          <li v-for="estate in item.real_estates" :key="estate.id">{{ estate.field_name }}</li>
        </ul>
      </div>
      <div v-if="item.category === 'Vehicle'">
        <h2>Vehicles</h2>
        <ul>
          <li v-for="vehicle in item.vehicles" :key="vehicle.id">{{ vehicle.field_name }}</li>
        </ul>
      </div>
      <div v-if="isEditor">
        <input v-model="editedItem.auction_date" placeholder="Name" />
        <input v-model="editedItem.category" placeholder="Description" />
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
