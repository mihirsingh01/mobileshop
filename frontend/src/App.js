import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

function Home() {
  return <h2>Welcome to Mobile Shop Management</h2>;
}

import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { fetchData } from './ApiClient';

function Home() {
  return <h2>Welcome to Mobile Shop Management</h2>;
}

function Logins() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('logins').then(setData);
  }, []);
  return <div><h2>Logins</h2><pre>{JSON.stringify(data, null, 2)}</pre></div>;
}

function SuperAdmin() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('super_admin').then(setData);
  }, []);
  return <div><h2>Super Admin</h2><pre>{JSON.stringify(data, null, 2)}</pre></div>;
}

function AccessoriesStaff() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('accessories_staff').then(setData);
  }, []);
  return <div><h2>Accessories Staff</h2><pre>{JSON.stringify(data, null, 2)}</pre></div>;
}

function RepairingStaff() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('repairing_staff').then(setData);
  }, []);
  return <div><h2>Repairing Staff</h2><pre>{JSON.stringify(data, null, 2)}</pre></div>;
}

function OldMobileStaff() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('old_mobile_staff').then(setData);
  }, []);
  return <div><h2>Old Mobile Staff</h2><pre>{JSON.stringify(data, null, 2)}</pre></div>;
}

function PromoterStaff() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('promoter_staff').then(setData);
  }, []);
  return <div><h2>Promoter Staff</h2><pre>{JSON.stringify(data, null, 2)}</pre></div>;
}

function Cashier() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('cashier').then(setData);
  }, []);
  return <div><h2>Cashier</h2><pre>{JSON.stringify(data, null, 2)}</pre></div>;
}

function Sales() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('sales').then(setData);
  }, []);
  return <div><h2>Sales</h2><pre>{JSON.stringify(data, null, 2)}</pre></div>;
}

function Customer() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('customer').then(setData);
  }, []);
  return <div><h2>Customer</h2><pre>{JSON.stringify(data, null, 2)}</pre></div>;
}

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/logins">Logins</Link></li>
            <li><Link to="/super_admin">Super Admin</Link></li>
            <li><Link to="/accessories_staff">Accessories Staff</Link></li>
            <li><Link to="/repairing_staff">Repairing Staff</Link></li>
            <li><Link to="/old_mobile_staff">Old Mobile Staff</Link></li>
            <li><Link to="/promoter_staff">Promoter Staff</Link></li>
            <li><Link to="/cashier">Cashier</Link></li>
            <li><Link to="/sales">Sales</Link></li>
            <li><Link to="/customer">Customer</Link></li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/logins" element={<Logins />} />
          <Route path="/super_admin" element={<SuperAdmin />} />
          <Route path="/accessories_staff" element={<AccessoriesStaff />} />
          <Route path="/repairing_staff" element={<RepairingStaff />} />
          <Route path="/old_mobile_staff" element={<OldMobileStaff />} />
          <Route path="/promoter_staff" element={<PromoterStaff />} />
          <Route path="/cashier" element={<Cashier />} />
          <Route path="/sales" element={<Sales />} />
          <Route path="/customer" element={<Customer />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
