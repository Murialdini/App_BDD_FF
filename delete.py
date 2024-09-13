from config import SessionLocal
from models import Prodotto

def delete_prodotto(id_prodotto):
    session = SessionLocal()
    prodotto = session.query(Prodotto).filter_by(id_prodotto=id_prodotto).first()
    if prodotto:
        session.delete(prodotto)
        session.commit()
        print(f"Prodotto ID {id_prodotto} cancellato con successo.")
    else:
        print("Prodotto non trovato.")
    session.close()

delete_prodotto(24)
