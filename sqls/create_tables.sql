CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    tag TEXT UNIQUE NOT NULL
);

-- Таблица для связи книг с тегами
CREATE TABLE book_tags (
    id SERIAL PRIMARY KEY,
    book_id INT NOT NULL,
    tag_id INT NOT NULL,
    FOREIGN KEY (tag_id) REFERENCES tags (id)
);