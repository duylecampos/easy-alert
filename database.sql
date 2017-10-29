CREATE TABLE IF NOT EXISTS auth (
  id serial NOT NULL,
  username varchar(120) NOT NULL UNIQUE,
  password bytea NOT NULL,
  PRIMARY KEY (id)
);