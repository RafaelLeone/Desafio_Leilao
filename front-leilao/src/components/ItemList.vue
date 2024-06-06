<template>
    <div>
        <button @click="logout">Logout</button>
        <h1>Items</h1>
        <ul>
            <li v-for="item in items" :key="item.id"> 
                <p>Leilão {{ item.id }}: {{ item.category }}</p>
                <p>{{ item.auction_date }}</p>
                <p>{{ item.auction_time }}</p>
                <p>{{ item.city }}, {{ item.state }}</p>
                <p><button @click="viewItem(item.id)">View Details</button></p>
                <p><button v-if="isEditor" @click="deleteItem(item.id)">Delete</button></p>
            </li>
        </ul>
        <form v-if="isEditor" @submit.prevent="addItem">
            <div>
                <label>Categoria:</label>
                <div>
                    <input type="radio" id="veiculo" value="Veículo" v-model="newItem.category">
                    <label for="veiculo">Veículo</label>
                    <input type="radio" id="imovel" value="Imóvel" v-model="newItem.category">
                    <label for="imovel">Imóvel</label>
                </div>
                <div>
                    <label>Data do leilão:</label>
                    <datetime v-model="newItem.auction_date" :value="newItem.auction_date" format="dd/MM/yyyy" required :useUtc="false"></datetime>
                </div>
                <div>
                    <label>Horário do leilão:</label>
                    <input type="time" v-model="newItem.auction_time" required>
                </div>
                <div>
                    <label for="city">Cidade</label>
                    <input id="city" v-model="newItem.city" placeholder="Cidade" required />
                </div>
                <div>
                    <label for="state">Estado</label>
                    <input id="state" v-model="newItem.state" placeholder="Estado" required />
                </div>
                <div>
                    <label for="street">Endereço</label>
                    <input id="street" v-model="newItem.street" placeholder="Endereço" required />
                </div>
                <button type="submit">Add Item</button>
            </div>
        </form>
    </div>
</template>

<script>
import { getItems, createItem, deleteItem } from '@/services/api';
import { Datetime } from 'vue-datetime';
import 'vue-datetime/dist/vue-datetime.css';

export default {
    components: {
        Datetime,
    },
    data() {
        return {
            items: [],
            isEditor: false,
            newItem: {
                creator: '',
                category: '',
                auction_date: '',
                auction_time: '',
                city: '',
                state: '',
                street: ''
            },
        };
    },
    async created() {
        this.fetchItems();
        this.checkRole();
    },
    methods: {
        async fetchItems() {
            try {
                this.items = await getItems();
            } catch (error) {
                console.error('Error fetching items:', error);
                this.$router.push('/login');
            }
        },
        async addItem() {
            const item = await createItem(this.newItem);
            this.items.push(item);
            this.newItem.name = '';
            this.newItem.description = '';
        },
        async deleteItem(itemId) {
            await deleteItem(itemId);
            this.items = this.items.filter(item => item.id !== itemId);
        },
        viewItem(itemId) {
            this.$router.push({ name: 'ItemDetail', params: { id: itemId } });
        },
        logout() {
            localStorage.setItem('isAuthenticated', 'false');
            localStorage.removeItem('token');
            localStorage.removeItem('username');
            this.$router.push('/login');
        },
        checkRole() {
            const username = localStorage.getItem('username');
            this.isEditor = username && username.length === 14;
        },
    },
};
</script>
