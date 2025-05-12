-- 002_create_user_games_table.sql
-- Tracks “played” vs “wishlist” for each user
create table if not exists user_games (
  user_id uuid references auth.users(id) on delete cascade,
  game_id uuid references games(id) on delete cascade,
  status text not null check (status in ('played','wishlist')),
  added_at timestamp with time zone default now(),
  primary key (user_id, game_id)
);
