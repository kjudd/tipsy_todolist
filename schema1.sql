CREATE TABLE Users (
	id INTEGER PRIMARY KEY, 
	name VARCHAR(100),
	password VARCHAR(100), 
	email VARCHAR(100)
);

CREATE TABLE Tasks (
    id INTEGER PRIMARY KEY,
    title VARCHAR(100),
    created_at DATETIME,
    completed_at DATETIME
);