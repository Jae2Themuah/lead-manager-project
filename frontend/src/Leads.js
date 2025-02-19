import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Leads = () => {
  const [leads, setLeads] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchLeads = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/leads/');
        setLeads(response.data || []);  // Ensure leads is an array
        setLoading(false);
      } catch (error) {
        console.error('Error fetching leads:', error);
        setLoading(false);
      }
    };

    fetchLeads();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!leads.length) {
    return <div>No leads found.</div>;
  }

  return (
    <div>
      <h2>Leads</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {leads.map((lead) => (
            <tr key={lead.id}>
              <td>{lead.name}</td>
              <td>{lead.email}</td>
              <td>{lead.phone}</td>
              <td>{lead.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Leads;
