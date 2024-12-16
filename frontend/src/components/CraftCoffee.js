import React, { useState } from 'react';
import { craftCoffee } from '../services/api';
import { Box, TextField, Button, Typography, Alert } from '@mui/material';

function CraftCoffee({ setGlobalError }) {
  const [formData, setFormData] = useState({
    coffee_portions: 0,
    water_portions: 0,
    milk_portions: 0
  });
  const [success, setSuccess] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await craftCoffee(formData);
      setSuccess(response.message);
      setGlobalError('');
    } catch (error) {
      setGlobalError(error.response?.data?.detail || 'Ошибка при создании крафтового кофе');
      setSuccess('');
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: parseInt(e.target.value) || 0
    });
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ maxWidth: 400, mx: 'auto' }}>
      <Typography variant="h6" gutterBottom>
        Создать свой кофе
      </Typography>

      {success && (
        <Alert severity="success" sx={{ mb: 2 }}>
          {success}
        </Alert>
      )}

      <TextField
        fullWidth
        margin="normal"
        type="number"
        label="Порции кофе"
        name="coffee_portions"
        value={formData.coffee_portions}
        onChange={handleChange}
        required
      />
      
      <TextField
        fullWidth
        margin="normal"
        type="number"
        label="Порции воды"
        name="water_portions"
        value={formData.water_portions}
        onChange={handleChange}
        required
      />
      
      <TextField
        fullWidth
        margin="normal"
        type="number"
        label="Порции молока"
        name="milk_portions"
        value={formData.milk_portions}
        onChange={handleChange}
        required
      />
      
      <Button 
        variant="contained" 
        color="primary" 
        type="submit" 
        fullWidth 
        sx={{ mt: 2 }}
      >
        Создать
      </Button>
    </Box>
  );
}

export default CraftCoffee; 