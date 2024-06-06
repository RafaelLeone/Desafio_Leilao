<template>
    <div>
        <button @click="logout">Logout</button>
        <h1>Items</h1>
        <ul>
            <li v-for="item in items" :key="item.id"> 
                Leilão {{ item.id }}: {{ item.category }}
                {{ item.auction_date }}
                {{ item.city }}, {{ item.state }}
                <button @click="viewItem(item.id)">View Details</button>
                <button v-if="isEditor" @click="deleteItem(item.id)">Delete</button>
            </li>
        </ul>
        <form v-if="isEditor" @submit.prevent="addItem">
            <input v-model="newItem.category" placeholder="Categoria" required />
            <input v-model="newItem.auction_date" placeholder="Data do leilão" required />
            <input v-model="newItem.city" placeholder="Cidade" required />
            <input v-model="newItem.state" placeholder="Estado" required />
            <input v-model="newItem.street" placeholder="Endereço" required />
            <button type="submit">Add Item</button>
        </form>
    </div>
</template>

<script>
import { getItems, createItem, deleteItem } from '@/services/api';

export default {
    data() {
        return {
            items: [],
            isEditor: false,
            newItem: {
                name: '',
                description: '',
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
