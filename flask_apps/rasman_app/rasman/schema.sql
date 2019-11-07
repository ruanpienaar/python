DROP TABLE IF EXISTS post;

CREATE TABLE hosts (
  hostname TEXT NOT NULL PRIMARY KEY,
  passwd TEXT NOT NULL,
  dashboard_url TEXT
);
