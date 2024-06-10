<template>
    <div>
        <button @click="logout">Logout</button>
        <h1>Leilões</h1>
        <ul>
            <li v-for="item in items" :key="item.id"> 
                <p>Leilão {{ item.id }}: {{ item.category }}</p>
                <p>{{ item.auction_date_display }}</p>
                <p>{{ item.auction_time }}</p>
                <p>{{ item.city }}, {{ item.state }}</p>
                <p><button @click="viewItem(item.id)">Ver detalhes do leilão</button></p>
                <p><button v-if="isEditor" @click="deleteItem(item.id)">Delete este leilão</button></p>
            </li>
        </ul>
        <form v-if="isEditor" @submit.prevent="addItem">
            <div>
                <h2>Adicione um novo leilão:</h2>
                <label>Categoria:</label>
                <div>
                    <input type="radio" id="veiculo" value="Veículo" v-model="newItem.category">
                    <label for="veiculo">Veículo</label>
                    <input type="radio" id="imovel" value="Imóvel" v-model="newItem.category">
                    <label for="imovel">Imóvel</label>
                </div>
                <div>
                    <label>Data do leilão:</label>
                    <datetime v-model="auction_date" format="dd/MM/yyyy" required :useUtc="false"></datetime>
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
                <button type="submit">Adicionar leilão</button>
            </div>
        </form>
        <form v-if="isEditor" @submit.prevent="addProduct">
            <div>
                <h2>Adicione um novo produto:</h2>
                <label>Categoria:</label>
                <div>
                    <input type="radio" id="veiculo" value="Veículo" v-model="newProductCategory">
                    <label for="veiculo">Veículo</label>
                    <input type="radio" id="imovel" value="Imóvel" v-model="newProductCategory">
                    <label for="imovel">Imóvel</label>
                </div>
                <div>
                    <label>Nome/descrição do produto:</label>
                    <input v-model="newProduct.name" required>
                </div>
                <div>
                    <label>Preço do produto:</label>
                    <input v-model="newProduct.starting_price" required>
                </div>
                <div>
                    <label>Valor do incremento:</label>
                    <input v-model="newProduct.increment_value" required>
                </div>
                <div>
                    <label>Leilão:</label>
                    <input v-model="newProduct.item" required>
                </div>
                <button type="submit">Adicionar produto</button>
            </div>
        </form>
    </div>
</template>

<script>
import { getItems, getUserId, createItem, deleteItem, createVehicle, createRealEstate, getItem } from '@/services/api';
import { Datetime } from 'vue-datetime';
import 'vue-datetime/dist/vue-datetime.css';

export default {
    components: {
        Datetime,
    },
    data() {
        return {
            items: [],
            userId: '',
            auction_date: '',
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
            newProductCategory: '',
            newProduct: {
                item: '',
                name: '',
                starting_price: '',
                increment_value: ''
            },
        };
    },
    async created() {
        this.fetchItems();
        this.checkRole();
    },
    watch: {
        'auction_date': function(newValue) {
        // Call the formatDate method whenever newItem.auction_date changes
        this.formatDate(newValue);
        },
    },
    methods: {
        async fetchItems() {
            try {
                this.items = await getItems();
                this.userId = await getUserId(localStorage.username);
                localStorage.setItem('userId', this.userId);
                this.newItem.creator = localStorage.userId;
            } catch (error) {
                console.error('Error fetching items:', error);
                this.$router.push('/login');
            }
        },
        async addProduct() {
            const auctionData = await getItem(this.newProduct.item);
            const auctionCategory = auctionData.category;
            if (this.newProductCategory === 'Veículo' && this.newProductCategory === auctionCategory) {
                await createVehicle(this.newProduct);
                alert(`Veículo adicionado ao Leilão ${this.newProduct.item}`)
            }
            else if (this.newProductCategory === 'Imóvel' && this.newProductCategory === auctionCategory) {
                await createRealEstate(this.newProduct);
                alert(`Imóvel adicionado ao Leilão ${this.newProduct.item}`)
            }
            else {
                alert(`Falha ao criar produto. Tem certeza de que o leilão escolhido é de ${this.newProductCategory}?`)
            }
            this.newProduct.item = '';
            this.newProduct.name = '';
            this.newProduct.starting_price = '';
            this.newProduct.increment_value = '';
            this.newProductCategory = '';
        },
        async addItem() {
            const item = await createItem(this.newItem);
            this.items.push(item);
            this.newItem.creator = '';
            this.newItem.category = '';
            this.newItem.auction_date = '';
            this.newItem.auction_time = '';
            this.newItem.city = '';
            this.newItem.state = '';
            this.newItem.street = '';
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
            localStorage.removeItem('userId');
            this.$router.push('/login');
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
            this.newItem.auction_date = formattedDateString;
        }
    },
};
</script>
