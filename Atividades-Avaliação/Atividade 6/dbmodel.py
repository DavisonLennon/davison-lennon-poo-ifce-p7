from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'TB_CLIENTE'

    _id = Column(Integer, primary_key=True)
    _nome = Column(String(255), nullable=False)
    _codigo = Column(Integer, nullable=False)
    _cnpjcpf = Column(String(255), nullable=False)
    _tipo = Column(Integer, nullable=False)


class Produto(Base):
    __tablename__ = 'TB_PRODUTO'

    _id = Column(Integer, primary_key=True)
    _codigo = Column(Integer, nullable=False)
    _descricao = Column(String(255), nullable=False)
    _valorUnitario = Column(Numeric, nullable=False)
    _item_nota_fiscal_id = Column(Integer, ForeignKey('TB_ITEM_NF._id'))


class ItemNotaFiscal(Base):
    __tablename__ = 'TB_ITEM_NF'

    _id = Column(Integer, primary_key=True)
    _sequencial = Column(Integer, nullable=False)
    _quantidade = Column(Integer, nullable=False)
    _produto = relationship('Produto')
    _valor = Column(Numeric, nullable=True)
    _nota_fiscal_id = Column(Integer, ForeignKey='TB_NOTA_FISCAL._id')


class NotaFiscal(Base):
    __tablename__ = 'TB_NOTA_FISCAL'

    _id = Column(Integer, primary_key=True)
    _codigo = Column(Integer, nullable=False)
    _data = Column(Data, nullable=False)
    _cliente = relationship()
    _descricao = Column(String(255), nullable=False)
    _items = relationship('ItemNotaFiscal')
    _valorNota = Column(Numeric, nullable=True)



engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
