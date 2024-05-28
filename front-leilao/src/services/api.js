import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

export const getItems = async () => {
    const response = await axios.get(API_URL + 'items/');
    return response.data;
};

export const createItem = async (item) => {
    try {
        const response = await axios.post(`${API_URL}items/`, item);
        return response.data;
    } catch (error) {
        // Handle error
        console.error('Error creating item:', error);
        throw error;
    }
};


export const deleteItem = async (itemId) => {
    try {
        const response = await axios.delete(`${API_URL}items/${itemId}/`);
        return response.data;
    } catch (error) {
        // Handle error
        console.error('Error deleting item:', error);
        throw error;
    }
};
