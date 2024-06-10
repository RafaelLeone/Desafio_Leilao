import Vue from 'vue';
import VueRouter from 'vue-router';
import ItemList from '@/components/ItemList.vue';
import ItemDetail from '@/components/ItemDetail.vue';
import LoginPage from '@/components/LoginPage.vue';
import RegisterPage from '@/components/RegisterPage.vue';
import VehicleDetail from '@/components/VehicleDetail';
import RealEstateDetail from '@/components/RealEstateDetail';
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
  {
    path: '/vehicle/:id/',
    name: 'VehicleDetail',
    component: VehicleDetail,
    meta: { requiresAuth: true },
  },
  {
    path: '/realestate/:id/',
    name: 'RealEstateDetail',
    component: RealEstateDetail,
    meta: { requiresAuth: true },
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated()) {
    next('/login/');
  } else {
    next();
  }
});

export default router;
