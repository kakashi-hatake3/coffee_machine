import React, { useState } from 'react';
import { makeCoffee } from '../services/api';
import { Box, Button, Typography, Alert, TextField } from '@mui/material';

function MakeCoffee({ setGlobalError }) {
  const [coffeeType, setCoffeeType] = useState('');
  const [success, setSuccess] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await makeCoffee(coffeeType);
      setSuccess(response.message);
      setGlobalError('');
    } catch (error) {
      setGlobalError(error.response?.data?.detail || 'Ошибка при приготовлении кофе');
      setSuccess('');
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ maxWidth: 400, mx: 'auto' }}>
      <Typography variant="h6" gutterBottom>
        Приготовить кофе
      </Typography>

      {success && (
        <Alert severity="success" sx={{ mb: 2 }}>
          {success}
        </Alert>
      )}

      <TextField
        fullWidth
        margin="normal"
        label="Тип кофе"
        value={coffeeType}
        onChange={(e) => setCoffeeType(e.target.value)}
        required
        helperText="Например: americano, espresso, cappuccino"
      />
      
      <Button 
        variant="contained" 
        color="primary" 
        type="submit" 
        fullWidth 
        sx={{ mt: 2 }}
      >
        Приготовить
      </Button>
    </Box>
  );
}

export default MakeCoffee; 