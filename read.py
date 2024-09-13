from config import SessionLocal
from models import Prodotto

def read_prodotti():
    session = SessionLocal()
    prodotti = session.query(Prodotto).all()
    for prodotto in prodotti:
        print(f"ID: {prodotto.id_prodotto}, Nome: {prodotto.nome}, Tipo: {prodotto.tipo}")
    session.close()

read_prodotti()
