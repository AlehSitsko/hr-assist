//Dashboard.jsx
import React, { useState } from 'react';

function Dashboard({ user }) {
  return (
    <div className="container mt-5">
      <h2>Welcome, {user.username}!</h2>
      <p>Select a module to continue.</p>
    </div>
  );
}

export default Dashboard;
