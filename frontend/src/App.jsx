import { useState } from 'react';
import Login from './components/auth/Login';
import Dashboard from './components/dashboard/Dashboard';

function App() {
  const [user, setUser] = useState(null);

  if (!user) {
    return <Login onLogin={setUser} />;
  }

  return <Dashboard user={user} />;
}

export default App;
