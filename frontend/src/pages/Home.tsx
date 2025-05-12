// frontend/src/pages/Home.tsx
import React, { useEffect, useState } from 'react'
import { supabase } from '../lib/supabaseClient'
import { useNavigate } from 'react-router-dom'

type Session = { user: { email: string } }

export default function Home() {
  const [session, setSession] = useState<Session | null>(null)
  const navigate = useNavigate()

  useEffect(() => {
    // initial fetch
    supabase.auth.getSession().then(({ data: { session } }) => {
      setSession(session)
    })

    // subscribe correctly per v2 API
    const { data: { subscription } } = supabase.auth.onAuthStateChange(
      (_event, sess) => {
        setSession(sess)
      }
    )

    return () => {
      subscription.unsubscribe()
    }
  }, [])

  const handleSignOut = async () => {
    await supabase.auth.signOut()
    navigate('/signin')
  }

  return (
    <div style={{ maxWidth: 600, margin: '2rem auto', fontFamily: 'sans-serif' }}>
      <h1>🏠 Home</h1>
      {session ? (
        <>
          <p>Welcome, <strong>{session.user.email}</strong>!</p>
          <button onClick={handleSignOut}>Sign Out</button>
        </>
      ) : (
        <p>Loading session…</p>
      )}
    </div>
  )
}
