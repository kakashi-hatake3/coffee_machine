import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1/coffee-machine';

export const initializeMachine = async (data) => {
  const response = await axios.post(`${API_URL}/initialize`, data);
  return response.data;
};

export const makeCoffee = async (coffeeType) => {
  const response = await axios.post(`${API_URL}/make/${coffeeType}`);
  return response.data;
};

export const craftCoffee = async (data) => {
  const response = await axios.post(`${API_URL}/craft`, data);
  return response.data;
};

export const cleanMachine = async () => {
  const response = await axios.post(`${API_URL}/clean`);
  return response.data;
};

export const getMachineStatus = async () => {
  const response = await axios.get(`${API_URL}/status`);
  return response.data;
}; 