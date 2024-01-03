SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;


-- SQLite schema for simplified book application

-- Create a 'books' table with auto-incrementing id
CREATE TABLE public.books (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL
);


ALTER TABLE public.books OWNER TO postgres;

-- Insert sample data
INSERT INTO public.books (title, author) VALUES ('1984', 'George Orwell');
INSERT INTO public.books (title, author) VALUES ('To Kill a Mockingbird', 'Harper Lee');
