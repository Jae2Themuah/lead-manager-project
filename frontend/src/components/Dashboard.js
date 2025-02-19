// src/Dashboard.js
import React, { useState, useEffect } from 'react';
import './Dashboard.css';  // Ensure this is applied for styles

const Dashboard = () => {
  const [userData, setUserData] = useState(null);
  const [stats, setStats] = useState({
    activeLeads: 0,
    pendingTasks: 0,
    totalLeads: 0,
  });

  const fetchData = () => {
    const mockUserData = {
      name: 'John Doe',
      email: 'john@example.com',
      role: 'Admin',
    };

    const mockStatsData = {
      activeLeads: Math.floor(Math.random() * 20),
      pendingTasks: Math.floor(Math.random() * 10),
      totalLeads: Math.floor(Math.random() * 100),
    };

    setUserData(mockUserData);
    setStats(mockStatsData);
  };

  useEffect(() => {
    fetchData();
  }, []);

  if (!userData) {
    return <p>Loading user data...</p>;
  }

  return (
    <div className="dashboard-container">
      <div className="dashboard-header">
        <h2>Welcome back, {userData.name}!</h2>
      </div>

      <div className="stats">
        <div className="stat-item">
          <h3>Active Leads</h3>
          <p>{stats.activeLeads}</p>
        </div>
        <div className="stat-item">
          <h3>Pending Tasks</h3>
          <p>{stats.pendingTasks}</p>
        </div>
        <div className="stat-item">
          <h3>Total Leads</h3>
          <p>{stats.totalLeads}</p>
        </div>
      </div>

      <div className="recent-activity">
        <h3>Recent Activity</h3>
        <ul>
          <li>
            <strong>Lead #123:</strong> New lead created.
          </li>
          <li>
            <strong>Task #45:</strong> Follow up with lead.
          </li>
          <li>
            <strong>Lead #124:</strong> Appointment scheduled.
          </li>
        </ul>
      </div>

      <div className="tasks">
        <h3>Pending Tasks</h3>
        <ul>
          <li>Contact lead #125</li>
          <li>Follow up with lead #126</li>
          <li>Schedule demo for lead #127</li>
        </ul>
      </div>

      <div className="refresh-container">
        <button onClick={fetchData}>Refresh Data</button>
      </div>
    </div>
  );
};

export default Dashboard;
