
Passengers table
CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    age INTEGER NOT NULL,
    gender VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

psql -U sachin -d train_db



CREATE TABLE trains (
  id SERIAL PRIMARY KEY,
  train_number VARCHAR UNIQUE NOT NULL,
  name VARCHAR NOT NULL,
  start_place VARCHAR NOT NULL,
  destination_place VARCHAR NOT NULL,
  stops JSONB  
);



CREATE TABLE train_schedules (
  id SERIAL PRIMARY KEY,
  train_id INTEGER NOT NULL REFERENCES trains(id) ON DELETE CASCADE,
  start_place VARCHAR NOT NULL,
  destination_place VARCHAR NOT NULL,
  departure_time TIMESTAMP NOT NULL,
  arrival_time TIMESTAMP NOT NULL
);


-- 1. Create ENUM type
DO $$ BEGIN
    CREATE TYPE coach_type_enum AS ENUM ('General', 'Sleeper', 'AC');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

-- 2. Create coaches table
CREATE TABLE coaches (
    id SERIAL PRIMARY KEY,
    train_id INT REFERENCES trains(id) ON DELETE CASCADE,
    coach_type coach_type_enum NOT NULL,
    coach_number VARCHAR NOT NULL
);


DO $$ BEGIN
    CREATE TYPE allocation_status_enum AS ENUM ('Allocated', 'Unallocated');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

CREATE TABLE seats (
    id SERIAL PRIMARY KEY,
    seat_number INT NOT NULL,
    coach_id INT REFERENCES coaches(id) ON DELETE CASCADE,
    allocation_status allocation_status_enum DEFAULT 'Unallocated',
    allocated_to INT REFERENCES passengers(id)
);
