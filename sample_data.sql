CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    region TEXT NOT NULL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    amount_cents INTEGER NOT NULL CHECK (amount_cents >= 0),
    status TEXT NOT NULL CHECK (status IN ('completed', 'cancelled'))
);

INSERT INTO customers (id, region) VALUES
    (1, 'North'), (2, 'South'), (3, 'North');

INSERT INTO orders (id, customer_id, amount_cents, status) VALUES
    (1, 1, 12500, 'completed'),
    (2, 2,  9000, 'completed'),
    (3, 3,  7500, 'completed'),
    (4, 2,  2500, 'cancelled');
