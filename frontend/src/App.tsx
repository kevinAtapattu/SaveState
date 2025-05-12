// frontend/src/App.tsx
import React from 'react'
import { BrowserRouter, Routes, Route, Navigate, Link } from 'react-router-dom'
import SignUp    from './pages/SignUp'
import SignIn    from './pages/SignIn'
import Home      from './pages/Home'
import Games     from './pages/Games'    // ← new

export default function App() {
  return (
    <BrowserRouter>
      <nav style={{ padding: '1rem', textAlign: 'center' }}>
        <Link to="/signup" style={{ margin: '0 1rem' }}>Sign Up</Link>
        <Link to="/signin" style={{ margin: '0 1rem' }}>Sign In</Link>
        <Link to="/home"   style={{ margin: '0 1rem' }}>Home</Link>
        <Link to="/games"  style={{ margin: '0 1rem' }}>Games</Link>  {/* ← new */}
      </nav>

      <Routes>
        <Route path="/"       element={<Navigate to="/signin" replace />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/signin" element={<SignIn />} />
        <Route path="/home"   element={<Home />} />
        <Route path="/games"  element={<Games />} />                {/* ← new */}
        <Route path="*"       element={<Navigate to="/signin" replace />} />
      </Routes>
    </BrowserRouter>
  )
}
