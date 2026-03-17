import sqlite3

def create_table():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather(
        city TEXT,
        temperature REAL,
        humidity INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_weather(city, temp, humidity):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO weather VALUES (?,?,?)",
        (city, temp, humidity)
    )

    conn.commit()
    conn.close()


def show_data():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM weather")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()