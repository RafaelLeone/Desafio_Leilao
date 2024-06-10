<template>
    <div>
      <div v-if="realEstate">
        <h1>Imóvel {{ realEstate.id }}</h1>
        <p>Nome: {{ realEstate.name }}</p>
        <p>Preço inicial: {{ realEstate.starting_price }}</p>
        <p>Valor de incremento: {{ realEstate.increment_value }}</p>
        <div>
            <h2>Dê o seu lance:</h2>
            <input type="number" v-model="bidValue" required />
            <button @click="confirmBid">Confirmar lance</button>
        </div>
        <div>
            <h3>Histórico de lances:</h3>
            <div v-if="realEstate.bid_history && realEstate.bid_history.length > 0">
                <li v-for="(bid, index) in realEstate.bid_history" :key="index">
                    <p>{{ index }}.: {{ bid }}</p>
                </li>
            </div>
            <div v-else>
                <p>Nenhum lance ainda! Seja o(a) primeiro(a)!</p>
            </div>
        </div>
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
  import { getRealEstate, updateRealEstate, addBid } from '@/services/api';
  
  export default {
    data() {
      return {
        realEstate: null,
        bidValue: null,
        editedRealEstate: {
          name: '',
          starting_price: '',
          increment_value: '',
          bid_history: ''
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
      async confirmBid() {
        const incrementValue = this.bidValue - this.realEstate.starting_price;
        const remainderValue = incrementValue % this.realEstate.increment_value;
        if (remainderValue === 0) {
            try {
                await addBid(this.realEstate.id, {
                    user: localStorage.username,
                    bid: this.bidValue
                });
                await this.fetchRealEstate();
                console.log(this.bidValue);
                console.log(this.realEstate);
                console.log(this.editedRealEstate);
                this.editedRealEstate.starting_price = this.bidValue;
                await this.saveChanges()
                }
            catch (error) {
                console.error('Error adding bid:', error);
                alert('Failed to add bid. Please try again.');
            }
        } else {
            alert('O valor incrementado não é válido. Reveja o valor de incremento.');
        }
        this.bidValue = null;
        this.editedRealEstate.name = '';
        this.editedRealEstate.starting_price = '';
        this.editedRealEstate.increment_value = '';
        this.editedRealEstate.bid_history = '';
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
  