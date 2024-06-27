// services/api.js
import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

export const readRoot = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching root data:', error);
    throw error;
  }
};

export const login = async (item) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/login/`, null, {
      params: { item }
    });
    return response.data;
  } catch (error) {
    console.error('Error logging in:', error);
    throw error;
  }
};

export const selectFramework = async (framework) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/backendframework`, null, {
      params: { framework }
    });
    return response.data;
  } catch (error) {
    console.error('Error selecting framework:', error);
    throw error;
  }
};

export const addPage = async (pageDescription, pageName) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/createpage`, null, {
      params: { page_description: pageDescription, page_name: pageName }
    });
    return response.data;
  } catch (error) {
    console.error('Error adding', error);
    throw error;
  }
};

export const viewPage = async (pageName) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/viewpage`, null, {
      params: { page_name: pageName }
    });
    return response.data;
  } catch (error) {
    console.error('Error viewing page:', error);
    throw error;
  }
};
