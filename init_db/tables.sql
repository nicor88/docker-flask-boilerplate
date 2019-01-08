CREATE EXTENSION "pgcrypto";

CREATE TABLE IF NOT EXISTS users (
	id VARCHAR(36) DEFAULT gen_random_uuid(),
	name VARCHAR(100),
	PRIMARY KEY(id)
);

INSERT INTO users (name) VALUES ('Test User 1');
INSERT INTO users (name) VALUES ('Test User 2');
