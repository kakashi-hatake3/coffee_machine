import React, { useState, useEffect } from 'react';
import { getCoffees } from '../services/api';

function CoffeeList() {
  const [coffees, setCoffees] = useState([]);

  useEffect(() => {
    const fetchCoffees = async () => {
      const data = await getCoffees();
      setCoffees(data);
    };
    fetchCoffees();
  }, []);

  return (
    <div className="coffee-list">
      <h2>Наши напитки</h2>
      <div className="coffee-grid">
        {coffees.map((coffee) => (
          <div key={coffee.id} className="coffee-card">
            <h3>{coffee.name}</h3>
            <p>{coffee.description}</p>
            <p>Цена: ${coffee.price}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default CoffeeList; 