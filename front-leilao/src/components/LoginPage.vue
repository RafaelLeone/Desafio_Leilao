<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <div>
          <label for="username">CPF/CNPJ:</label>
          <input type="text" v-model="username" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" v-model="password" required />
        </div>
        <button type="submit">Login</button>
        <button @click="goToRegister">Register</button>
      </form>
    </div>
  </template>
  
  <script>
  import { login } from '@/services/api';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      async login() {
        try {
          const credentials = {
            username: this.username,
            password: this.password,
          };
          await login(credentials);
          localStorage.setItem('isAuthenticated', 'true');
          localStorage.setItem('username', this.username);
          this.$router.push('/');
        } catch (error) {
          localStorage.setItem('isAuthenticated', 'false');
          localStorage.removeItem('username');
          console.error('Error during login:', error);
        }
      },
      goToRegister() {
        this.$router.push('/register'); // Redirect to the login page
      },
    },
  };
  </script>
  