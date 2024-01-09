# TOTODO
#### Video Demo:  [Link YouTube](https://youtu.be/YCW_RL88TbQ)
#### Description: This is a simple todo web app.

## What is this?

my cs50x final project's repository.

Totodo is a simple todo management web app. Made with Python, Flask, HTML, CSS, and Javascript

With this app, you can:
- Create your own account,
- View all your todos in one page in order of date and time,
- Create todo with deadline (date and/or time) and add tag or tags,
- Create, edit, and delete tags, and view all tags in one page,
- Change status of an entry from TODO to DONE and the opposite, and
- Delete an entry.

## Index

| Filename | Description |
| - | - |
| `static/` | All static files (CSS and Javascript) |
| `templates/` | All html files |
| `app.py` | The Flask app (in Python) |
| `helpers.py` | Some function to make `app.py` clearer (mostly from Problem Set 9) |
| `todo queries.sql` | Queries that I use to fill `todos.db` (SQLite3) |
| `todos.db` | Database for the web app (SQLite3) |

### Libraries

- I use SQL functions from CS50 library,
- I use flask library,
- I use flask_session library for manage cookies, and
- I use werkzeug.security library to create hash for password (security).

### Routes and Functions

| Routes | Functions |
| - | - |
| `/` | `index()` |
| `/login` | `login()` |
| `/logout` | `logout()` |
| `/register` | `register()` |
| `/TODO` | `TODO()` |
| `/DONE` | `DONE()` |
| `/DELETE` | `DELETE()` |
| `/create` | `create()` |
| `/tags` | `tags()` |
| `/tag_edit` | `tag_edit()` |
| `/tag_delete` | `tag_delete()` |

| Functions (in helpers.py) | Description |
| - | - |
| `apology(text, code = 400)` | Handling error |
| `login_required(f)` | Handling flask_session |

### static/

Javascript:
- There are only 2 files (`index.js` and `tags.js`).
- `index.js` is only loaded when in route `/` and used to change DONE and CANCEL buttons and to change table background color according to the status of each entries.
- `tags.js` is only loaded when in route `/tags` and used to handle when editing tags.

CSS:
- I want to learn how to style my own web with CSS, so I decided to write my own CSS (not using Bootstrap).
- I got inspiration from material android apps.
- I only use one media query, which is for mobile device (< 768px).
- I use sticky navigation bar and footer.

### Queries

I use SQLite3 to manage database. It's called `todos.db`:
- There are 4 tables (`users`, `todos`, `tags`, `tagging`)
- I decided to use separate tagging system, so that each entry can have multiple tags and it's going to be easier if user wants to edit tags.

## About Me

I'm Clara Maria Lie. I'm from Cikarang, Indonesia.
