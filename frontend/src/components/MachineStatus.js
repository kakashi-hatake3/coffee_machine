import React, { useState, useEffect } from 'react';
import { getMachineStatus, cleanMachine } from '../services/api';
import { Box, Button, Typography, Alert, Paper } from '@mui/material';

function MachineStatus({ setGlobalError }) {
  const [status, setStatus] = useState(null);
  const [success, setSuccess] = useState('');

  const fetchStatus = async () => {
    try {
      const data = await getMachineStatus();
      setStatus(data);
      setGlobalError('');
    } catch (error) {
      setGlobalError(error.response?.data?.detail || 'Ошибка при получении статуса');
    }
  };

  const handleClean = async () => {
    try {
      const response = await cleanMachine();
      setSuccess(response.message);
      fetchStatus(); // Обновляем статус после очистки
      setGlobalError('');
    } catch (error) {
      setGlobalError(error.response?.data?.detail || 'Ошибка при очистке');
      setSuccess('');
    }
  };

  useEffect(() => {
    fetchStatus();
  }, []);

  if (!status) return null;

  return (
    <Box sx={{ maxWidth: 400, mx: 'auto' }}>
      <Typography variant="h6" gutterBottom>
        Статус кофемашины
      </Typography>

      {success && (
        <Alert severity="success" sx={{ mb: 2 }}>
          {success}
        </Alert>
      )}

      <Paper sx={{ p: 2, mb: 2 }}>
        <Typography variant="body1">Остаток зерен: {status.coffee_beans} г</Typography>
        <Typography variant="body1">Остаток воды: {status.water} мл</Typography>
        <Typography variant="body1">Остаток молока: {status.milk} мл</Typography>
        <Typography variant="body1">Приготовлено кофе: {status.brewed_coffee_count}</Typography>
        <Typography variant="body1">Осталось приготовлений: {status.remaining_brews}</Typography>
      </Paper>

      <Button 
        variant="contained" 
        color="secondary" 
        onClick={handleClean}
        fullWidth
      >
        Очистить кофемашину
      </Button>
    </Box>
  );
}

export default MachineStatus; 