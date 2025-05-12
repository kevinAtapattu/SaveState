-- 001_create_games_table.sql
-- Enable the gen_random_uuid() function
create extension if not exists "pgcrypto";

-- Games table
create table if not exists games (
  id uuid primary key default gen_random_uuid(),
  title text not null,
  cover_url text,
  release_date date,
  created_at timestamp with time zone default now()
);
