// src/App.js

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';

import LoginPage from './pages/Login';
import DashboardPage from './pages/Dashboard';
import PrivateRoute from './routes/PrivateRoute';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          {/* Public Route */}
          <Route path="/login" element={<LoginPage />} />

          {/* Private Routes: This is the parent for all protected pages */}
          <Route path="/" element={<PrivateRoute />}>
            <Route index element={<DashboardPage />} />
            <Route path="dashboard" element={<DashboardPage />} />
            {/* Add other protected routes here later, e.g., /pos, /inventory */}
          </Route>

        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;