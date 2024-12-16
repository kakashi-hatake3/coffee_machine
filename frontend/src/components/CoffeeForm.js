import React, { useState } from 'react';
import { createCoffee } from '../services/api';
import { Button, TextField, Box, Typography } from '@mui/material';

function CoffeeForm() {
  const [formData, setFormData] = useState({
    coffee_beans: 0,
    water: 0,
    milk: 0,
    coffee_type: ''
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await createCoffee(formData);
      console.log('Кофе создан:', response);
      setFormData({
        coffee_beans: 0,
        water: 0,
        milk: 0,
        coffee_type: ''
      });
    } catch (error) {
      console.error('Ошибка при создании кофе:', error);
    }
  };

  const handleChange = (e) => {
    const value = e.target.type === 'number' ? parseInt(e.target.value) : e.target.value;
    setFormData({
      ...formData,
      [e.target.name]: value
    });
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ maxWidth: 400, mx: 'auto', p: 2 }}>
      <Typography variant="h5" gutterBottom>
        Создать кофе
      </Typography>
      
      <TextField
        fullWidth
        margin="normal"
        label="Тип кофе"
        name="coffee_type"
        value={formData.coffee_type}
        onChange={handleChange}
        required
      />
      
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
        Приготовить кофе
      </Button>
    </Box>
  );
}

export default CoffeeForm; 