// Login.jsx
import { useState } from 'react';

function Login({ onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    // Simple authentication logic check
    if (username === 'admin' && password === '1234') {
      onLogin({ username });
    } else {
      alert('Invalid credentials');
    }
  };

  return (
    <div className="container mt-5" style={{ maxWidth: 400 }}>
      <h3 className="text-center mb-4">HR Assist Login</h3>
      <form onSubmit={handleSubmit}>
        <div className="form-group mb-3">
          <label>Username</label>
          <input className="form-control"
                 value={username}
                 onChange={(e) => setUsername(e.target.value)}
                 required />
        </div>
        <div className="form-group mb-3">
          <label>Password</label>
          <input type="password"
                 className="form-control"
                 value={password}
                 onChange={(e) => setPassword(e.target.value)}
                 required />
        </div>
        <button type="submit" className="btn btn-primary w-100">Login</button>
      </form>
    </div>
  );
}

export default Login;
