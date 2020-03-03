
CREATE TABLE hosts (
    hostname TEXT NOT NULL PRIMARY KEY,
    tvid INTEGER
    description TEXT,
    username TEXT NOT NULL,
    passwd TEXT NOT NULL,
    port INTEGER NOT NULL,
    dashboard_url TEXT,
    tvid INTEGER,
    FOREIGN KEY(tvid) REFERENCES tv(tvid)
);

CREATE TABLE tv (
    tvid INTEGER PRIMARY KEY AUTOINCREMENT,
    tv_position TEXT
);

INSERT INTO tv (tv_position) VALUES
    (NULL),
    (NULL),
    (NULL),
    (NULL),
    (NULL),
    (NULL),
    (NULL),
    (NULL),
    (NULL),
    (NULL),
    (NULL),
    (NULL);