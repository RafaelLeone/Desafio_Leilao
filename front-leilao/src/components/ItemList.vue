<template>
    <div>
        <h1>Items</h1>
        <ul>
            <li v-for="item in items" :key="item.id"> 
                {{ item.name }}: {{ item.description }}
                <button @click="viewItem(item.id)">View Details</button>
                <button @click="deleteItem(item.id)">Delete</button>
            </li>
        </ul>
        <form @submit.prevent="addItem">
            <input v-model="newItem.name" placeholder="Name" required />
            <input v-model="newItem.description" placeholder="Description" required />
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
            newItem: {
                name: '',
                description: '',
            },
        };
    },
    async created() {
        this.items = await getItems();
    },
    methods: {
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
    },
};
</script>
