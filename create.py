from config import SessionLocal
from models import Prodotto

def create_prodotto(nome, tipo, unita_di_misura, data_di_scadenza):
    session = SessionLocal()
    nuovo_prodotto = Prodotto(
        nome=nome,
        tipo=tipo,
        unita_di_misura=unita_di_misura,
        data_di_scadenza=data_di_scadenza
    )
    session.add(nuovo_prodotto)
    session.commit()
    session.close()
    print(f"Prodotto '{nome}' inserito con successo.")

create_prodotto('ZUCCA', 'VERDURA', 'Kg', '2025-06-30')