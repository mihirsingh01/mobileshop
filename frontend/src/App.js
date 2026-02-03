import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { fetchData } from './ApiClient';
import Layout from './layouts/Layout';
import DataTable from './components/DataTable';

function Home() {
  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-white shadow-lg rounded-lg p-8 text-center">
        <h1 className="text-4xl font-bold text-gray-800 mb-4">Welcome to Mobile Shop Management</h1>
        <p className="text-lg text-gray-600">Manage your mobile shop operations efficiently with our comprehensive dashboard.</p>
        <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="bg-blue-100 p-4 rounded-lg">
            <h3 className="text-xl font-semibold text-blue-800">Staff Management</h3>
            <p className="text-blue-600">Oversee all staff roles and activities.</p>
          </div>
          <div className="bg-green-100 p-4 rounded-lg">
            <h3 className="text-xl font-semibold text-green-800">Sales Tracking</h3>
            <p className="text-green-600">Monitor sales and customer data.</p>
          </div>
          <div className="bg-purple-100 p-4 rounded-lg">
            <h3 className="text-xl font-semibold text-purple-800">Admin Controls</h3>
            <p className="text-purple-600">Full administrative access.</p>
          </div>
        </div>
      </div>
    </div>
  );
}

function Logins() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('logins').then(setData);
  }, []);
  return <DataTable data={data} title="Logins" />;
}

function SuperAdmin() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('super_admin').then(setData);
  }, []);
  return <DataTable data={data} title="Super Admin" />;
}

function AccessoriesStaff() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('accessories_staff').then(setData);
  }, []);
  return <DataTable data={data} title="Accessories Staff" />;
}

function RepairingStaff() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('repairing_staff').then(setData);
  }, []);
  return <DataTable data={data} title="Repairing Staff" />;
}

function OldMobileStaff() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('old_mobile_staff').then(setData);
  }, []);
  return <DataTable data={data} title="Old Mobile Staff" />;
}

function PromoterStaff() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('promoter_staff').then(setData);
  }, []);
  return <DataTable data={data} title="Promoter Staff" />;
}

function Cashier() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('cashier').then(setData);
  }, []);
  return <DataTable data={data} title="Cashier" />;
}

function Sales() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('sales').then(setData);
  }, []);
  return <DataTable data={data} title="Sales" />;
}

function Customer() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetchData('customer').then(setData);
  }, []);
  return <DataTable data={data} title="Customer" />;
}

function App() {
  return (
    <Router>
      <Layout>
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
      </Layout>
    </Router>
  );
}

export default App;