<template>
    <div>
      <h2>Register</h2>
      <form @submit.prevent="register">
        <div>
          <label for="username">CPF/CNPJ:</label>
          <input type="text" v-model="username" required />
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" v-model="email" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" v-model="password" required />
        </div>
        <button type="submit">Register</button>
        <button @click="logout">Back</button>
      </form>
    </div>
  </template>
  
  <script>
  import { register } from '@/services/api';
  
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: '',
      };
    },
    methods: {
      async register() {
        const usernamePattern = /^\d{11}$|^\d{14}$/;
        if (!usernamePattern.test(this.username)) {
          alert('CPF/CNPJ inválido.');
          return;
        }
        
        try {
          await register({ username: this.username, email: this.email, password: this.password });
          alert('Registration successful');
          this.$router.push('/login');
        } catch (error) {
          console.error('Error during registration:', error);
          alert('Registration failed. Please try again.');
        }
      },
      logout() {
        this.$router.push('/login'); // Redirect to the login page
      },
    },
  };
  </script>
  