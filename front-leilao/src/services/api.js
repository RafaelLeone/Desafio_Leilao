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

// Login APIs
export const login = async (credentials) => {
  const response = await axios.post(`${API_URL}token/`, credentials);
  localStorage.setItem('token', response.data.token);
  return response.data;
};

export const register = async (userData) => {
  const response = await axios.post(`${API_URL}register/`, userData);
  return response.data;
};

// Vehicle APIs
export async function createVehicle(vehicle) {
  const response = await axiosInstance.post(`vehicles/`, vehicle);
  return response.data;
}

export async function getVehicle(vehicleId) {
  const response = await axiosInstance.get(`vehicles/${vehicleId}/`);
  return response.data;
}

export async function updateVehicle(vehicleId, vehicle) {
  const response = await axiosInstance.put(`vehicles/${vehicleId}/`, vehicle);
  return response.data;
}

export async function deleteVehicle(vehicleId) {
  await axiosInstance.delete(`vehicles/${vehicleId}/`);
}

// RealEstate APIs
export async function createRealEstate(realEstate) {
  const response = await axiosInstance.post(`realestates/`, realEstate);
  return response.data;
}

export async function getRealEstate(realEstateId) {
  const response = await axiosInstance.get(`realestates/${realEstateId}/`);
  return response.data;
}

export async function updateRealEstate(realEstateId, realEstate) {
  const response = await axiosInstance.put(`realestates/${realEstateId}/`, realEstate);
  return response.data;
}

export async function deleteRealEstate(realEstateId) {
  await axiosInstance.delete(`realestates/${realEstateId}/`);
}

export const addBid = async (realEstateId, bidData) => {
  try {
    const response = await axios.post(`${API_URL}realestates/${realEstateId}/add_bid/`, bidData, {
      headers: {
        'Authorization': `Token ${localStorage.getItem('token')}`
      }
    });
    return response.data;
  } catch (error) {
    console.error('Error adding bid:', error);
    throw error;
  }
};

export const addVehicleBid = async (vehicleId, bidData) => {
  try {
    const response = await axios.post(`${API_URL}vehicles/${vehicleId}/add_bid/`, bidData, {
      headers: {
        'Authorization': `Token ${localStorage.getItem('token')}`
      }
    });
    return response.data;
  } catch (error) {
    console.error('Error adding bid:', error);
    throw error;
  }
};
