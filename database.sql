CREATE TABLE IF NOT EXISTS auth (
  id serial NOT NULL,
  username varchar(120) NOT NULL UNIQUE,
  password bytea NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS channel (
  id serial NOT NULL,
  name varchar(50) NOT NULL,
  slug varchar(50) NOT NULL UNIQUE,
  active boolean NOT NULL,
  PRIMARY KEY (id)
);