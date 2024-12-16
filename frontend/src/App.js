import React, { useState } from 'react';
import { Container, AppBar, Toolbar, Typography, Box, Tab, Tabs, Alert } from '@mui/material';
import InitializeMachine from './components/InitializeMachine';
import MakeCoffee from './components/MakeCoffee';
import CraftCoffee from './components/CraftCoffee';
import MachineStatus from './components/MachineStatus';
import './styles/main.css';

function App() {
  const [currentTab, setCurrentTab] = useState(0);
  const [globalError, setGlobalError] = useState('');
  
  const handleTabChange = (event, newValue) => {
    setCurrentTab(newValue);
    setGlobalError('');
  };

  return (
    <div className="app">
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6">
            Кофе-машина
          </Typography>
        </Toolbar>
      </AppBar>
      
      <Container>
        {globalError && (
          <Alert severity="error" sx={{ mt: 2 }}>
            {globalError}
          </Alert>
        )}

        <Box sx={{ borderBottom: 1, borderColor: 'divider', mt: 3, mb: 3 }}>
          <Tabs value={currentTab} onChange={handleTabChange}>
            <Tab label="Инициализация" />
            <Tab label="Приготовить кофе" />
            <Tab label="Создать свой кофе" />
            <Tab label="Статус и очистка" />
          </Tabs>
        </Box>

        {currentTab === 0 && <InitializeMachine setGlobalError={setGlobalError} />}
        {currentTab === 1 && <MakeCoffee setGlobalError={setGlobalError} />}
        {currentTab === 2 && <CraftCoffee setGlobalError={setGlobalError} />}
        {currentTab === 3 && <MachineStatus setGlobalError={setGlobalError} />}
      </Container>
    </div>
  );
}

export default App; 