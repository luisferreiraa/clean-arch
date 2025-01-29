from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Configuração da Base de Dados
SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'

# Cria o engine da Base de Dados
# O engine é o ponto de entrada para a Base de Dados. Gerencia as conexões
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

# Cria uma fábrica de sessões
# Casa requisição terá a sua própria sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos SQLAlchemy
Base = declarative_base()


# Função para obter a sessão da Base de Dados
def get_db() -> Session:
    """
    Gera uma sessão da Base de Dados para cada requisição.
    Fecha a sessão automaticamente após o uso.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
