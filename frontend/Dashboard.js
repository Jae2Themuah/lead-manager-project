// Inside components/Dashboard.js
import React, { useEffect, useState } from 'react';

const Dashboard = () => {
  const [user, setUser] = useState(null);
  const [stats, setStats] = useState({
    activeLeads: 0,
    pendingTasks: 0,
    totalLeads: 0,
  });

  useEffect(() => {
    // Fetch user data (this could be from your API or mock data)
    const fetchUser = async () => {
      const response = await fetch('/api/user'); // Example API endpoint
      const data = await response.json();
      setUser(data);
    };

    // Fetch dashboard stats
    const fetchStats = async () => {
      // Example API fetch, replace with your actual API call
      const response = await fetch('/api/dashboard-stats');
      const data = await response.json();
      setStats(data);
    };

    fetchUser();
    fetchStats();
  }, []);

  if (!user) {
    return <p>Loading user data...</p>;
  }

  return (
    <div className="dashboard-container">
      <div className="dashboard-header">
        <h2>Welcome back, {user.name}!</h2>
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
        {/* Example of activity feed */}
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
    </div>
  );
};

export default Dashboard;
