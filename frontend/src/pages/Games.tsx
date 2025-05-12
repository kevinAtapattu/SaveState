// frontend/src/pages/Games.tsx

import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

type Game = {
  id: string
  title: string
  cover_url?: string
  release_date?: string
}

export default function Games() {
  const [games, setGames] = useState<Game[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    axios
      .get<Game[]>('http://127.0.0.1:8000/games')  // ← direct backend URL
      .then(res => setGames(res.data))
      .catch(err => setError(err.message))
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <p style={{ textAlign: 'center' }}>Loading games…</p>
  if (error)   return <p style={{ textAlign: 'center', color: 'red' }}>Error: {error}</p>
  if (games.length === 0) return <p style={{ textAlign: 'center' }}>No games yet.</p>

  return (
    <div style={{ maxWidth: 600, margin: '2rem auto', fontFamily: 'sans-serif' }}>
      <h1>🎮 Games</h1>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {games.map(g => (
          <li key={g.id} style={{ marginBottom: '1.5rem' }}>
            <Link to={`/games/${g.id}`} style={{ fontSize: '1.2rem', fontWeight: 'bold' }}>
              {g.title}
            </Link>
            {g.release_date && (
              <div><small>Released: {new Date(g.release_date).toLocaleDateString()}</small></div>
            )}
          </li>
        ))}
      </ul>
    </div>
  )
}
