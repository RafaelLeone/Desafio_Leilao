import Vue from 'vue';
import VueRouter from 'vue-router';
import ItemList from '@/components/ItemList.vue'; // Adjust the path if needed
import ItemDetail from '@/components/ItemDetail.vue'; 

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'ItemList',
    component: ItemList, // Replace 'Home' with the component you want to use as the homepage
  },
  {
    path: '/item/:id/', // Define dynamic route parameter
    name: 'ItemDetail',
    component: ItemDetail, // Replace 'ItemDetail' with the component you want to use for item detail
  },
  // Other routes...
];

const router = new VueRouter({
  mode: 'history', // Optional: Use 'history' mode for clean URLs
  base: process.env.BASE_URL,
  routes,
});

export default router;
