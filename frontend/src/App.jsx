import { useEffect, useState } from "react";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export default function App() {
  const [health, setHealth] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${API_BASE_URL}/health`)
      .then((res) => res.json())
      .then(setHealth)
      .catch((err) => setError(err.message));
  }, []);

  return (
    <div className="app">
      <h1>BHU-SETU</h1>
      <p className="subtitle">Intelligent Land Record Digitization &amp; Validation System</p>
      <div className="status-card">
        <h2>Phase 0 — Environment Smoke Test</h2>
        {error && <p className="error">Could not reach backend: {error}</p>}
        {!error && !health && <p>Checking backend health…</p>}
        {health && (
          <ul>
            <li>Overall: <strong>{health.status}</strong></li>
            <li>Database: {health.database}</li>
            <li>Redis: {health.redis}</li>
          </ul>
        )}
      </div>
    </div>
  );
}
