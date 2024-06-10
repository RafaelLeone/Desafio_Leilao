<template>
    <div>
      <div v-if="realEstate">
        <h1>Imóvel {{ realEstate.id }}</h1>
        <p>Nome: {{ realEstate.name }}</p>
        <p>Preço inicial: {{ realEstate.starting_price }}</p>
        <p>Valor de incremento: {{ realEstate.increment_value }}</p>
        <div v-if="isEditor">
          <h2>Edite este imóvel:</h2>
          <div>
            <label>Nome:</label>
            <input v-model="editedRealEstate.name" required />
          </div>
          <div>
            <label>Preço inicial:</label>
            <input type="number" v-model="editedRealEstate.starting_price" required />
          </div>
          <div>
            <label>Valor de incremento:</label>
            <input type="number" v-model="editedRealEstate.increment_value" required />
          </div>
          <button @click="saveChanges">Salvar mudanças</button>
        </div>
        <button @click="goBack">Voltar</button>
      </div>
    </div>
  </template>
  
  <script>
  import { getRealEstate, updateRealEstate } from '@/services/api';
  
  export default {
    data() {
      return {
        realEstate: null,
        editedRealEstate: {
          name: '',
          starting_price: '',
          increment_value: ''
        },
        isEditor: false
      };
    },
    async created() {
      await this.fetchRealEstate();
      this.checkRole();
    },
    methods: {
      async fetchRealEstate() {
        try {
          const response = await getRealEstate(this.$route.params.id);
          this.realEstate = response;
          this.editedRealEstate = { ...this.realEstate };
        } catch (error) {
          console.error('Error fetching real estate details:', error);
          this.$router.push('/login');
        }
      },
      async saveChanges() {
        try {
          await updateRealEstate(this.realEstate.id, this.editedRealEstate);
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
  