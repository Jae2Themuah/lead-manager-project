import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './styles.css';
import Dashboard from './components/Dashboard';
import Leads from './Leads';
import Profile from './Profile';
import Settings from './Settings';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <h1>Lead Manager</h1>
      </div>
      <div className="navbar-right">
        <ul>
          <li><Link to="/dashboard">Dashboard</Link></li>
          <li><Link to="/leads">Leads</Link></li>
          <li><Link to="/profile">Profile</Link></li>
          <li><Link to="/settings">Settings</Link></li>
        </ul>
      </div>
    </nav>
  );
};

const HomePage = () => {
  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Welcome back, joshadmin!</h1>
      </header>
    </div>
  );
};

const App = () => {
  return (
    <Router>
      <Navbar />  {/* Navbar renders only once at the top */}
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/leads" element={<Leads />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Router>
  );
};

export default App;
