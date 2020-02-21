DROP TABLE IF EXISTS post;

CREATE TABLE hosts (
  hostname TEXT NOT NULL PRIMARY KEY,
  description TEXT,
  username TEXT NOT NULL,
  passwd TEXT NOT NULL,
  port INTEGER NOT NULL,
  dashboard_url TEXT
);

CREATE TABLE tv (
    tvid INTEGER PRIMARY KEY AUTOINCREMENT,
    hostname TEXT
);

-- 12 tv's
INSERT INTO tv (hostname) VALUES
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