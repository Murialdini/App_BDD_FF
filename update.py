from config import SessionLocal
from models import Prodotto

def update_prodotto(id_prodotto, nuovo_tipo):
    session = SessionLocal()
    prodotto = session.query(Prodotto).filter_by(id_prodotto=id_prodotto).first()
    if prodotto:
        prodotto.tipo = nuovo_tipo
        session.commit()
        print(f"Prodotto ID {id_prodotto} aggiornato con nuovo tipo: {nuovo_tipo}")
    else:
        print("Prodotto non trovato.")
    session.close()

update_prodotto(1, 'PRODOTTO TIPICO')
