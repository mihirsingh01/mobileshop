import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => {
  const links = [
    { to: '/', label: 'Home' },
    { to: '/logins', label: 'Logins' },
    { to: '/super_admin', label: 'Super Admin' },
    { to: '/accessories_staff', label: 'Accessories Staff' },
    { to: '/repairing_staff', label: 'Repairing Staff' },
    { to: '/old_mobile_staff', label: 'Old Mobile Staff' },
    { to: '/promoter_staff', label: 'Promoter Staff' },
    { to: '/cashier', label: 'Cashier' },
    { to: '/sales', label: 'Sales' },
    { to: '/customer', label: 'Customer' },
  ];

  return (
    <div className="fixed left-0 top-0 h-full w-64 bg-gray-800 text-white p-4">
      <h2 className="text-xl font-bold mb-4">Mobile Shop</h2>
      <nav>
        <ul className="space-y-2">
          {links.map((link) => (
            <li key={link.to}>
              <Link
                to={link.to}
                className="block py-2 px-4 rounded hover:bg-gray-700 transition-colors"
              >
                {link.label}
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </div>
  );
};

export default Sidebar;
