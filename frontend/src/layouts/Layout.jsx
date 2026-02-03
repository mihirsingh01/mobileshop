import React from 'react';
import Sidebar from '../components/Sidebar';

const Layout = ({ children }) => {
  return (
    <div className="flex">
      <Sidebar />
      <main className="ml-64 flex-1 p-4 bg-gray-100 min-h-screen">
        {children}
      </main>
    </div>
  );
};

export default Layout;
