from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Prodotto(Base):
    __tablename__ = 'prodotto'

    id_prodotto = Column(Integer, primary_key=True, index=True)
    nome = Column(String(30), nullable=False)
    tipo = Column(String(30))
    unita_di_misura = Column(String(20))
    data_di_scadenza = Column(Date)

class Ricetta(Base):
    __tablename__ = 'ricetta'

    id_ricetta = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    descrizione = Column(String(255))
    tempo_di_preparazione = Column(Integer)

class ComponenteFamiglia(Base):
    __tablename__ = 'componente_famiglia'

    id_componente = Column(Integer, primary_key=True, index=True)
    nome = Column(String(20), nullable=False)
    allergia = Column(String(50))

class Pasto(Base):
    __tablename__ = 'pasto'

    id_pasto = Column(Integer, primary_key=True, index=True)
    tipo_pasto = Column(String(50))
    ora = Column(String(5))

class Allergia(Base):
    __tablename__ = 'allergie'

    id_allergia = Column(Integer, primary_key=True, index=True)
    tipo_allergia = Column(String(50))

class Negozio(Base):
    __tablename__ = 'negozio'

    id_negozio = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    tipo = Column(String(50))
    indirizzo = Column(String(200))

class Dispensa(Base):
    __tablename__ = 'dispensa'

    id_dispensa = Column(Integer, primary_key=True, index=True)
    nome = Column(String(30), nullable=False)

class Menu(Base):
    __tablename__ = 'menu'

    id_menu = Column(Integer, primary_key=True, index=True)
    nome_menu = Column(String(100), nullable=False)
    tipo_menu = Column(String(50))
    stagionalita = Column(String(50))

class ProdottoNegozio(Base):
    __tablename__ = 'prodotto_negozio'

    id_prodotto = Column(Integer, ForeignKey('prodotto.id_prodotto'), primary_key=True)
    id_negozio = Column(Integer, ForeignKey('negozio.id_negozio'), primary_key=True)
    disponibilita = Column(String(50))
    quantita = Column(Float)

class ProdottoDispensa(Base):
    __tablename__ = 'prodotto_dispensa'

    id_prodotto = Column(Integer, ForeignKey('prodotto.id_prodotto'), primary_key=True)
    id_dispensa = Column(Integer, ForeignKey('dispensa.id_dispensa'), primary_key=True)
    data_di_scadenza = Column(Date)
    quantita = Column(Float)

class ProdottoRicetta(Base):
    __tablename__ = 'prodotto_ricetta'

    id_prodotto = Column(Integer, ForeignKey('prodotto.id_prodotto'), primary_key=True)
    id_ricetta = Column(Integer, ForeignKey('ricetta.id_ricetta'), primary_key=True)
    quantita = Column(Float)
    unita_di_misura = Column(String(20))

class PastoRicetta(Base):
    __tablename__ = 'pasto_ricetta'

    id_pasto = Column(Integer, ForeignKey('pasto.id_pasto'), primary_key=True)
    id_ricetta = Column(Integer, ForeignKey('ricetta.id_ricetta'), primary_key=True)

class ConsumoPasto(Base):
    __tablename__ = 'consumo_pasto'

    id_pasto = Column(Integer, ForeignKey('pasto.id_pasto'), primary_key=True)
    id_componente = Column(Integer, ForeignKey('componente_famiglia.id_componente'), primary_key=True)
    note = Column(String(255))

class AllergieComponenteFamiglia(Base):
    __tablename__ = 'allergie_componente_famiglia'

    id_componente = Column(Integer, ForeignKey('componente_famiglia.id_componente'), primary_key=True)
    id_allergia = Column(Integer, ForeignKey('allergie.id_allergia'), primary_key=True)
    gravita = Column(String(30))

class PreparazioneRicetta(Base):
    __tablename__ = 'preparazione_ricetta'

    id_componente = Column(Integer, ForeignKey('componente_famiglia.id_componente'), primary_key=True)
    id_ricetta = Column(Integer, ForeignKey('ricetta.id_ricetta'), primary_key=True)
    tempo_impiegato = Column(Integer)

class AllergieMenu(Base):
    __tablename__ = 'allergie_menu'

    id_menu = Column(Integer, ForeignKey('menu.id_menu'), primary_key=True)
    id_allergia = Column(Integer, ForeignKey('allergie.id_allergia'), primary_key=True)
    presenza_allergene = Column(String(30))

class MenuRicetta(Base):
    __tablename__ = 'menu_ricetta'

    id_menu = Column(Integer, ForeignKey('menu.id_menu'), primary_key=True)
    id_ricetta = Column(Integer, ForeignKey('ricetta.id_ricetta'), primary_key=True)
    portata = Column(String(30))

class ProdottoMenu(Base):
    __tablename__ = 'prodotto_menu'

    id_prodotto = Column(Integer, ForeignKey('prodotto.id_prodotto'), primary_key=True)
    id_menu = Column(Integer, ForeignKey('menu.id_menu'), primary_key=True)
    quantita = Column(Float)
    unita_di_misura = Column(String(20))        