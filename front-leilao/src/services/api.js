// src/services/api.js
import axios from 'axios';
import { getCookie } from './csrf';

const API_URL = 'http://localhost:8000/api/';

const axiosInstance = axios.create({
  baseURL: API_URL,
});

axiosInstance.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token');
    const csrfToken = getCookie('csrftoken');

    if (token) {
      config.headers['Authorization'] = 'Token ' + token;
    }

    if (csrfToken) {
      config.headers['X-CSRFToken'] = csrfToken;
    }

    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

export default axiosInstance;

export const getItems = async () => {
  const response = await axiosInstance.get('items/');
  return response.data;
};

export const getUserId = async (username) => {
  const response = await axiosInstance.get(`${API_URL}users/${username}/`);
  return response.data.user_id;
};

export const createItem = async (item) => {
  const response = await axiosInstance.post('items/', item);
  return response.data;
};

export const deleteItem = async (itemId) => {
  const response = await axiosInstance.delete(`items/${itemId}/`);
  return response.data;
};

export const getItem = async (itemId) => {
  const response = await axiosInstance.get(`items/${itemId}/`);
  return response.data;
};

export const updateItem = async (itemId, item) => {
  const response = await axiosInstance.put(`items/${itemId}/`, item);
  return response.data;
};

export const login = async (credentials) => {
  const response = await axios.post(`${API_URL}token/`, credentials);
  localStorage.setItem('token', response.data.token);
  return response.data;
};

export const register = async (userData) => {
  const response = await axios.post(`${API_URL}register/`, userData);
  return response.data;
};
