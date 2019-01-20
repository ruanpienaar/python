DROP TABLE IF EXISTS bootstrap_brokers;

CREATE TABLE bootstrap_brokers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hostname TEXT UNIQUE NOT NULL,
    port INTEGER NOT NULL
);