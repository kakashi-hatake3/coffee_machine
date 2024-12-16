import React, { useState } from 'react';
import { initializeMachine } from '../services/api';
import { Box, TextField, Button, Typography, Alert } from '@mui/material';

function InitializeMachine({ setGlobalError }) {
  const [formData, setFormData] = useState({
    coffee_beans: 0,
    water: 0,
    milk: 0
  });
  const [success, setSuccess] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await initializeMachine(formData);
      setSuccess(response.message);
      setGlobalError('');
    } catch (error) {
      setGlobalError(error.response?.data?.detail || 'Ошибка при инициализации');
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
        Заполнить кофемашину
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
        label="Кол-во зерен (г)"
        name="coffee_beans"
        value={formData.coffee_beans}
        onChange={handleChange}
        required
      />
      
      <TextField
        fullWidth
        margin="normal"
        type="number"
        label="Кол-во воды (мл)"
        name="water"
        value={formData.water}
        onChange={handleChange}
        required
      />
      
      <TextField
        fullWidth
        margin="normal"
        type="number"
        label="Кол-во молока (мл)"
        name="milk"
        value={formData.milk}
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
        Инициализировать
      </Button>
    </Box>
  );
}

export default InitializeMachine; 