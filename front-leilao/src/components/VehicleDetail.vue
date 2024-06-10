<template>
    <div>
      <div v-if="vehicle">
        <h1>Veículo {{ vehicle.id }}</h1>
        <p>Nome: {{ vehicle.name }}</p>
        <p>Preço inicial: {{ vehicle.starting_price }}</p>
        <p>Valor de incremento: {{ vehicle.increment_value }}</p>
        <div v-if="isEditor">
          <h2>Edite este veículo:</h2>
          <div>
            <label>Nome:</label>
            <input v-model="editedVehicle.name" required />
          </div>
          <div>
            <label>Preço inicial:</label>
            <input type="number" v-model="editedVehicle.starting_price" required />
          </div>
          <div>
            <label>Valor de incremento:</label>
            <input type="number" v-model="editedVehicle.increment_value" required />
          </div>
          <button @click="saveChanges">Salvar mudanças</button>
        </div>
        <button @click="goBack">Voltar</button>
      </div>
    </div>
  </template>
  
  <script>
  import { getVehicle, updateVehicle } from '@/services/api';
  
  export default {
    data() {
      return {
        vehicle: null,
        editedVehicle: {
          name: '',
          starting_price: '',
          increment_value: ''
        },
        isEditor: false
      };
    },
    async created() {
      await this.fetchVehicle();
      this.checkRole();
    },
    methods: {
      async fetchVehicle() {
        try {
          const response = await getVehicle(this.$route.params.id);
          this.vehicle = response;
          this.editedVehicle = { ...this.vehicle };
        } catch (error) {
          console.error('Error fetching vehicle details:', error);
          this.$router.push('/login');
        }
      },
      async saveChanges() {
        try {
          await updateVehicle(this.vehicle.id, this.editedVehicle);
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
  