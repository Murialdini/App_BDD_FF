from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL = 'mysql+pymysql://root:F3d3r1c0@localhost/federico_ferraro'
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

