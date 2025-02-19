// src/Routes.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './Dashboard';  // Adjust the path if needed
import Leads from './Leads';  // Create a Leads component
import Profile from './Profile';  // Create a Profile component
import Settings from './Settings';  // Create a Settings component

const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/leads" element={<Leads />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;
