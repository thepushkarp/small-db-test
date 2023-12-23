
-- SQLite schema for simplified book application

-- Create a 'books' table
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL
);

-- Insert sample data
INSERT INTO books (title, author) VALUES ('1984', 'George Orwell');
INSERT INTO books (title, author) VALUES ('To Kill a Mockingbird', 'Harper Lee');
