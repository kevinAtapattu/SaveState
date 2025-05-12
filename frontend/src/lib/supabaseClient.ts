// src/lib/supabaseClient.ts
console.log("ENV vars:", import.meta.env)          // optional debug
const url = import.meta.env.VITE_SUPABASE_URL as string
const key = import.meta.env.VITE_SUPABASE_ANON_KEY as string
import { createClient } from '@supabase/supabase-js'
export const supabase = createClient(url, key)
