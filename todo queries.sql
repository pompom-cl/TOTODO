CREATE TABLE users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    hash TEXT NOT NULL
);

CREATE TABLE todos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    todo TEXT NOT NULL,
    date DATE,
    time TIME,
    status TEXT DEFAULT 'TODO',
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE tags (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE tagging (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    tag_id INTEGER,
    todo_id INTEGER,
    FOREIGN KEY (tag_id) REFERENCES tags(id),
    FOREIGN KEY (todo_id) REFERENCES todos(id)
    FOREIGN KEY (user_id) REFERENCES users(id)
);
