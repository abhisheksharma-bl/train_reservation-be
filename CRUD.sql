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
    train_id INTEGER NOT NULL REFERENCES trains(id),
    start_station VARCHAR NOT NULL,
    destination_station VARCHAR NOT NULL,
    departure_time TIME NOT NULL
);

CREATE TABLE coach_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR UNIQUE NOT NULL,
    seat_capacity INTEGER NOT NULL
);

CREATE TABLE coaches (
    id SERIAL PRIMARY KEY,
    train_id INTEGER NOT NULL REFERENCES trains(id),
    travel_date DATE NOT NULL,
    coach_type_id INTEGER NOT NULL REFERENCES coach_types(id),
    coach_number VARCHAR NOT NULL,
    current_occupancy INTEGER DEFAULT 0,
    UNIQUE (train_id, travel_date, coach_number)
);

CREATE TABLE seats (
    id SERIAL PRIMARY KEY,
    seat_number INTEGER NOT NULL,
    coach_id INTEGER NOT NULL REFERENCES coaches(id),
    is_allocated BOOLEAN DEFAULT FALSE,
    allocated_to INTEGER REFERENCES passengers(id)
);

CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    age INTEGER,
    gender VARCHAR,
    contact_number INTEGER
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    passenger_id INTEGER NOT NULL REFERENCES passengers(id),
    train_id INTEGER NOT NULL REFERENCES trains(id),
    travel_date DATE NOT NULL,
    coach_id INTEGER REFERENCES coaches(id),
    seat_id INTEGER REFERENCES seats(id),
    booking_status VARCHAR NOT NULL, 
    booking_time TIMESTAMP DEFAULT now(),
    boarding_station VARCHAR,
    destination_station VARCHAR,
    boarding_time TIMESTAMP,
    destination_time TIMESTAMP,
    UNIQUE (passenger_id, train_id, travel_date, boarding_station, destination_station)
);

CREATE TABLE rac_queue (
    id SERIAL PRIMARY KEY,
    train_id INTEGER NOT NULL REFERENCES trains(id),
    travel_date DATE NOT NULL,
    passenger_id INTEGER NOT NULL REFERENCES passengers(id),
    booking_id INTEGER NOT NULL REFERENCES bookings(id),
    added_time TIMESTAMP DEFAULT now(),
    expiry_time TIMESTAMP,
    UNIQUE (train_id, travel_date, passenger_id)
);

CREATE TABLE waitlist_queue (
    id SERIAL PRIMARY KEY,
    train_id INTEGER NOT NULL REFERENCES trains(id),
    travel_date DATE NOT NULL,
    passenger_id INTEGER NOT NULL REFERENCES passengers(id),
    booking_id INTEGER NOT NULL REFERENCES bookings(id),
    added_time TIMESTAMP DEFAULT now(),
    UNIQUE (train_id, travel_date, passenger_id)
);

CREATE TABLE booking_history (
    id SERIAL PRIMARY KEY,
    booking_id INTEGER NOT NULL REFERENCES bookings(id),
    status_changed_to VARCHAR NOT NULL,
    change_time TIMESTAMP DEFAULT now()
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    booking_id INTEGER NOT NULL REFERENCES bookings(id),
    transaction_time TIMESTAMP DEFAULT now(),
    status VARCHAR,  
    payment_method VARCHAR,
    amount DECIMAL
);

CREATE TABLE pnr_records (
    id SERIAL PRIMARY KEY,
    booking_id INTEGER NOT NULL REFERENCES bookings(id),
    pnr UUID NOT NULL DEFAULT gen_random_uuid(),
    generated_at TIMESTAMP DEFAULT now(),
    status VARCHAR  
);

CREATE TABLE db_logs (
    id SERIAL PRIMARY KEY,
    log_time TIMESTAMP DEFAULT now(),
    table_name VARCHAR NOT NULL,
    operation VARCHAR NOT NULL,  
    user_id INTEGER REFERENCES passengers(id),
    booking_id INTEGER REFERENCES bookings(id),
    details TEXT
);


INSERT INTO coach_types (name, seat_capacity)
VALUES ('Sleeper', 72);

INSERT INTO trains (train_number, name, start_place, destination_place, stops)
VALUES ('12345', 'Rajdhani Express', 'Delhi', 'Mumbai', '{"Delhi", "Agra", "Bhopal", "Mumbai"}');

INSERT INTO train_schedules (train_id, start_station, destination_station, departure_time)
VALUES (1, 'Delhi', 'Mumbai', '06:00');

INSERT INTO coaches (train_id, travel_date, coach_type_id, coach_number)
VALUES (1, '2025-07-25', 1, 'S1');

INSERT INTO passengers (name, age, gender)
VALUES ('Jane Smith', 28, 'Female');

INSERT INTO seats (seat_number, coach_id)
VALUES (2, 1), (3, 1), (4, 1);

INSERT INTO bookings (
  passenger_id, train_id, travel_date, coach_id, seat_id, booking_status, boarding_station, destination_station)
VALUES (1, 1, '2025-07-25', 1, 1, 'CONFIRMED', 'Delhi', 'Mumbai');

UPDATE seats
SET is_allocated = TRUE, allocated_to = 1
WHERE id = 1;

INSERT INTO rac_queue (train_id, travel_date, passenger_id, booking_id)
VALUES (1, '2025-07-25', 1, 1);

INSERT INTO waitlist_queue (train_id, travel_date, passenger_id, booking_id)
VALUES (1, '2025-07-25', 1, 1);

INSERT INTO transactions (booking_id, status, payment_method, amount)
VALUES (1, 'Success', 'UPI', 850.00);

INSERT INTO pnr_records (booking_id, status)
VALUES (1, 'Active');

INSERT INTO booking_history (booking_id, status_changed_to)
VALUES (1, 'CONFIRMED');

INSERT INTO db_logs (table_name, operation, user_id, booking_id, details)
VALUES ('bookings', 'INSERT', 1, 1, 'Booking confirmed for Jane Smith');
