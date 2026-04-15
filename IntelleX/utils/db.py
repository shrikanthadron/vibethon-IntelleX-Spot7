# File: IntelleX/utils/db.py

import sqlite3
from contextlib import closing

DB_NAME = "database.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def init_db():
    with closing(get_connection()) as conn:
        cur = conn.cursor()

        # Users table
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Progress table
        cur.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            user_id INTEGER PRIMARY KEY,
            modules_completed INTEGER DEFAULT 0,
            score INTEGER DEFAULT 0,
            streak INTEGER DEFAULT 0,
            last_active TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """)

        # Quiz attempts
        cur.execute("""
        CREATE TABLE IF NOT EXISTS quiz_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            quiz_name TEXT,
            score INTEGER,
            total INTEGER,
            attempted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """)

        conn.commit()


# ---------------- USERS ----------------

def create_user(email, password_hash):
    with closing(get_connection()) as conn:
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO users(email, password_hash) VALUES (?, ?)",
            (email, password_hash)
        )
        user_id = cur.lastrowid

        cur.execute(
            "INSERT INTO progress(user_id) VALUES (?)",
            (user_id,)
        )

        conn.commit()


def get_user_by_email(email):
    with closing(get_connection()) as conn:
        cur = conn.cursor()

        cur.execute(
            "SELECT id, email, password_hash FROM users WHERE email=?",
            (email,)
        )

        return cur.fetchone()


# ---------------- PROGRESS ----------------

def get_progress(user_id):
    with closing(get_connection()) as conn:
        cur = conn.cursor()

        cur.execute("""
        SELECT modules_completed, score, streak, last_active
        FROM progress
        WHERE user_id=?
        """, (user_id,))

        return cur.fetchone()


def add_score(user_id, points):
    with closing(get_connection()) as conn:
        cur = conn.cursor()

        cur.execute("""
        UPDATE progress
        SET score = score + ?
        WHERE user_id=?
        """, (points, user_id))

        conn.commit()


def complete_module(user_id):
    with closing(get_connection()) as conn:
        cur = conn.cursor()

        cur.execute("""
        UPDATE progress
        SET modules_completed = modules_completed + 1
        WHERE user_id=?
        """, (user_id,))

        conn.commit()


def update_streak(user_id, today):
    with closing(get_connection()) as conn:
        cur = conn.cursor()

        cur.execute(
            "SELECT streak, last_active FROM progress WHERE user_id=?",
            (user_id,)
        )
        row = cur.fetchone()

        if row:
            streak, last_active = row

            if last_active != today:
                new_streak = streak + 1
                cur.execute("""
                UPDATE progress
                SET streak=?, last_active=?
                WHERE user_id=?
                """, (new_streak, today, user_id))

                conn.commit()


# ---------------- QUIZ ----------------

def save_quiz_attempt(user_id, quiz_name, score, total):
    with closing(get_connection()) as conn:
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO quiz_attempts(user_id, quiz_name, score, total)
        VALUES (?, ?, ?, ?)
        """, (user_id, quiz_name, score, total))

        conn.commit()


def get_leaderboard():
    with closing(get_connection()) as conn:
        cur = conn.cursor()

        cur.execute("""
        SELECT users.email, progress.score, progress.modules_completed, progress.streak
        FROM users
        JOIN progress ON users.id = progress.user_id
        ORDER BY progress.score DESC
        LIMIT 20
        """)

        return cur.fetchall()