
-- Passengers table
-- CREATE TABLE passengers (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR NOT NULL,
--     age INTEGER NOT NULL,
--     gender VARCHAR NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

--psql -U sachin -d train_db



-- CREATE TABLE trains (
--   id SERIAL PRIMARY KEY,
--   train_number VARCHAR UNIQUE NOT NULL,
--   name VARCHAR NOT NULL,
--   start_place VARCHAR NOT NULL,
--   destination_place VARCHAR NOT NULL,
--   stops JSONB  
-- );



CREATE TABLE train_schedules (
  id SERIAL PRIMARY KEY,
  train_id INTEGER NOT NULL REFERENCES trains(id) ON DELETE CASCADE,
  start_place VARCHAR NOT NULL,
  destination_place VARCHAR NOT NULL,
  departure_time TIMESTAMP NOT NULL,
  arrival_time TIMESTAMP NOT NULL
);
