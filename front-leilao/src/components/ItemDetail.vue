<template>
  <div>
    <div v-if="item">
      <h1>Leilão {{ item.id }}</h1>
      <p>Leilão de {{ item.category }}</p>
      <p>Data do leilão: {{ item.auction_date }}</p>
      <p>by {{ item.creator_username }}</p>
      <div v-if="item.category === 'Imóvel'">
          <h2>Lista de imóveis para leilão:</h2>
          <ul>
            <li v-for="estate in item.real_estates" :key="estate.id">{{ estate.name }} - {{ estate.starting_price }}
              <router-link :to="{ name: 'RealEstateDetail', params: { id: estate.id }}">{{ estate.name }}</router-link>
            </li>
          </ul>
        </div>
        <div v-if="item.category === 'Veículo'">
          <h2>Lista de veículos para leilão:</h2>
          <ul>
            <li v-for="vehicle in item.vehicles" :key="vehicle.id">{{ vehicle.name }} - {{ vehicle.starting_price }}
              <router-link :to="{ name: 'VehicleDetail', params: { id: vehicle.id }}">{{ vehicle.name }}</router-link>
            </li>
          </ul>
        </div>
      <div v-if="isEditor">
        <div>
          <h2>Edite este leilão:</h2>
          <label>Categoria:</label>
          <div>
              <input type="radio" id="veiculo" value="Veículo" v-model="editedItem.category">
              <label for="veiculo">Veículo</label>
              <input type="radio" id="imovel" value="Imóvel" v-model="editedItem.category">
              <label for="imovel">Imóvel</label>
          </div>
          <div>
              <label>Data do leilão:</label>
              <datetime v-model="auction_date" format="dd/MM/yyyy" required :useUtc="false"></datetime>
          </div>
          <div>
              <label>Horário do leilão:</label>
              <input type="time" v-model="editedItem.auction_time" required>
          </div>
          <div>
              <label for="city">Cidade</label>
              <input id="city" v-model="editedItem.city" placeholder="Cidade" required />
          </div>
          <div>
              <label for="state">Estado</label>
              <input id="state" v-model="editedItem.state" placeholder="Estado" required />
          </div>
          <div>
              <label for="street">Endereço</label>
              <input id="street" v-model="editedItem.street" placeholder="Endereço" required />
          </div>
          <button @click="saveChanges">Salvar mudanças</button>
        </div>
      </div>
      <button @click="goBack">Voltar</button>
    </div>
  </div>
</template>

<script>
import { getItem, updateItem } from '@/services/api';
import { Datetime } from 'vue-datetime';
import 'vue-datetime/dist/vue-datetime.css';

export default {
  components: {
      Datetime,
  },
  data() {
    return {
      item: null,
      auction_date: '',
      editedItem: {
        creator: localStorage.userId,
        category: '',
        auction_date: '',
        auction_time: '',
        city: '',
        state: '',
        street: ''
      },
      isEditor: false
    };
  },
  async created() {
    await this.fetchItem();
    this.checkRole();
  },
  watch: {
      'auction_date': function(newValue) {
      // Call the formatDate method whenever newItem.auction_date changes
      this.formatDate(newValue);
      },
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
    },
    formatDate(unformattedDate) {
        const formattedDate = new Date(unformattedDate);
        const year = formattedDate.getFullYear();
        const month = String(formattedDate.getMonth() + 1).padStart(2, '0'); // Add 1 to month since it's zero-based
        const day = String(formattedDate.getDate()).padStart(2, '0');

        const formattedDateString = `${year}-${month}-${day}`;
        this.editedItem.auction_date = formattedDateString;
        console.log('1')
        console.log(this.editedItem.auction_date);
    }
  }
};
</script>
