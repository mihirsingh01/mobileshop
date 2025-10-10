import React, { useState, useEffect } from 'react';
import { fetchData } from './ApiClient';

function DataDisplay({ endpoint }) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchData(endpoint)
      .then(response => setData(response))
      .catch(err => setError(err.message));
  }, [endpoint]);

  if (error) return <div>Error: {error}</div>;
  if (!data) return <div>Loading {endpoint}...</div>;

  return (
    <div>
      <h2>Data from {endpoint}</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

function App() {
  const endpoints = [
    'logins',
    'super_admin',
    'accessories_staff',
    'repairing_staff',
    'old_mobile_staff',
    'promoter_staff',
    'cashier',
    'sales',
    'customer',
  ];

  return (
    <div>
      <h1>Mobile Shop API Data Viewer</h1>
      {endpoints.map(endpoint => (
        <DataDisplay key={endpoint} endpoint={endpoint} />
      ))}
    </div>
  );
}

export default App;
