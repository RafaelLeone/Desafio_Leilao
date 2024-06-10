<template>
    <div>
      <div v-if="vehicle">
        <h1>Veículo {{ vehicle.id }}</h1>
        <p>Nome: {{ vehicle.name }}</p>
        <p>Preço inicial: {{ vehicle.starting_price }}</p>
        <p>Valor de incremento: {{ vehicle.increment_value }}</p>
        <div>
            <h2>Dê o seu lance:</h2>
            <input type="number" v-model="bidValue" required />
            <button @click="confirmBid">Confirmar lance</button>
        </div>
        <div>
            <h3>Histórico de lances:</h3>
            <div v-if="vehicle.bid_history && vehicle.bid_history.length > 0">
                <li v-for="(bid, index) in vehicle.bid_history" :key="index">
                    <p>{{ index }}.: {{ bid }}</p>
                </li>
            </div>
            <div v-else>
                <p>Nenhum lance ainda! Seja o(a) primeiro(a)!</p>
            </div>
        </div>
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
  import { getVehicle, updateVehicle, addVehicleBid } from '@/services/api';
  
  export default {
    data() {
      return {
        vehicle: null,
        bidValue: null,
        editedVehicle: {
          name: '',
          starting_price: '',
          increment_value: '',
          bid_history: ''
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
      async confirmBid() {
        const incrementValue = this.bidValue - this.vehicle.starting_price;
        const remainderValue = incrementValue % this.vehicle.increment_value;
        if (remainderValue === 0 && this.bidValue > this.vehicle.starting_price) {
            try {
                await addVehicleBid(this.vehicle.id, {
                    user: localStorage.username,
                    bid: this.bidValue
                });
                await this.fetchVehicle();
                this.editedVehicle.starting_price = this.bidValue;
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
        this.editedVehicle.name = '';
        this.editedVehicle.starting_price = '';
        this.editedVehicle.increment_value = '';
        this.editedVehicle.bid_history = '';
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
  