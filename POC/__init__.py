from sqlalchemy import Column, Integer, String,Table,MetaData
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
Base =declarative_base()

# from database import Base
metadata = MetaData()

# # class LanguageTranslator(BaseModel):
# LanguageTranslator = Table(
#     "language_translator",
#     metadata,
#     Column("id", Integer, primary_key=True,index=True),
#     # id = Column(Integer, primary_key=True, index=True),
#     # src_lang = Column(String, index=False, comment="source language"),
#     # dest_lang = Column(String, index=True, comment="destination language"),
#     # origin = Column(String, index=True),
#     # pronunciation = Column(String, index=False),
#     # translated_text = Column(String, index=False),
#     Column("src_lang", String),
#     Column("dest_lang", String),
#     Column("origin", String),
#     Column("pronunciation", String),
#     Column("translated_text", String),
# )

class LanguageTranslator(Base):
    __tablename__ = "language_translator"

    id = Column(Integer, primary_key=True, index=True)
    src_lang = Column(String, index=False, comment="source language")
    dest_lang = Column(String, index=True, comment="destination language")
    origin = Column(String, index=True)
    pronunciation = Column(String, index=False)
    translated_text = Column(String, index=False)