CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created DATETIME NOT NULL,
    order_menu TEXT NOT NULL,
    orderer TEXT NOT NULL,
    order_date TEXT NOT NULL,
    order_time TIME NOT NULL,
    order_status TEXT NOT NUll
);

CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
);