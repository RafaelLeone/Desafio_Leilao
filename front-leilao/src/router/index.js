import Vue from 'vue';
import VueRouter from 'vue-router';
import ItemList from '@/components/ItemList.vue';
import ItemDetail from '@/components/ItemDetail.vue';
import LoginPage from '@/components/LoginPage.vue';
import RegisterPage from '@/components/RegisterPage.vue';
import { isAuthenticated } from '@/services/auth'; // Implement this function to check if the user is authenticated

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'ItemList',
    component: ItemList,
    meta: { requiresAuth: true },
  },
  {
    path: '/item/:id/',
    name: 'ItemDetail',
    component: ItemDetail,
    meta: { requiresAuth: true },
  },
  {
    path: '/login/',
    name: 'LoginPage',
    component: LoginPage,
  },
  {
    path: '/register/',
    name: 'RegisterPage',
    component: RegisterPage,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isAuthenticated()) {
    next('/login');
  } else {
    next();
  }
});

export default router;
