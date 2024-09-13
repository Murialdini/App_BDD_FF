from sqlalchemy import create_engine, text
from config import DATABASE_URL
engine = create_engine(DATABASE_URL, echo=True)
try:
    with engine.connect() as connection:
        result = connection.execute(text("SHOW TABLES;"))
        tables = result.fetchall()
        print("Tabelle esistenti nel database:")
        for table in tables:
            print(table[0])
except Exception as e:
    print("Errore di connessione al database:", e)

