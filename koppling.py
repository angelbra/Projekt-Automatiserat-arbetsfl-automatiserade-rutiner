import psycopg2

def connect_to_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            port=5431,
            database="tucdb",
            user="tucgirls",
            password="1234"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print("✅ Ansluten till PostgreSQL-databas!")
        print("📦 Version:", version[0])
    except psycopg2.Error as e:
        print("❌ Fel vid anslutning till PostgreSQL:")
        print(e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()
            print("🔌 Anslutningen har stängts.")

if __name__ == "__main__":
    connect_to_db()


