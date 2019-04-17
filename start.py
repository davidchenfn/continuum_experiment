import sqlalchemy as sa
from fn_pillar_models.base import PG_NOW
from sqlalchemy import create_engine, UniqueConstraint, Column, BigInteger, DateTime
from sqlalchemy import (Column, String, DateTime, BigInteger, UniqueConstraint, Numeric,
                        ForeignKey, Enum, Table, Integer, Date, Boolean, Index)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from versioner import add_versioning

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


# TODO: Postgresql test
# TODO: Foreign keys
# TODO: Test drive usage
class Article(Base):
    __tablename__ = 'article'
    __table_args__ = (
        UniqueConstraint('author'),
    )
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Unicode(255))
    content = sa.Column(sa.UnicodeText)
    author = sa.Column(sa.Unicode(255), nullable=True)



def make_original_tables():
    session = sessionmaker(bind=engine)()
    sa.orm.configure_mappers()
    Base.metadata.create_all(engine)
    article = Article(id=1, name=u'Some article', content='Some content', author='yoohoo')
    session.add(article)
    session.commit()
    session.close()


def update_articles(cls):
    session = sessionmaker(bind=engine)()

    article = session.query(cls).get(1)

    article.name = u'Some cont'
    session.commit()
    article.name = u'Some updated article'
    article.content = "New Content"
    session.commit()
    article.content = "New Content version 2"
    session.commit()
    article.versions[1].name == "Some updated article"
    session.close()

# class Person(Base):
#     """
#     Defines a Person DB object
#     """
#
#     __tablename__ = 'people'
#     __table_args__ = (
#         UniqueConstraint('external_id'),
#     )
#
#     # All fields that correspond to physical columns in this table
#     id = Column(BigInteger, primary_key=True)
#     created_at = Column(DateTime(True), default=PG_NOW, nullable=False)
#     updated_at = Column(DateTime(True), default=PG_NOW, onupdate=PG_NOW, nullable=False)
#     external_id = Column(String, nullable=False)
#
#     name_full = Column(String, nullable=False)
#     name_first = Column(String, nullable=False)
#     name_last = Column(String, nullable=False)
#
#     name_middle = Column(String, nullable=True)
#     name_nick = Column(String, nullable=True)
#     name_prefix = Column(String, nullable=True)
#     name_suffix = Column(String, nullable=True)
#     name_pronunciation = Column(String, nullable=True)
#
#     bio_text = Column(String, nullable=True)
#     bio_date = Column(Date, nullable=True)
#     bio_source = Column(String, nullable=True)
#
#     birth_day = Column(Integer, nullable=True)
#     birth_month = Column(Integer, nullable=True)
#     birth_year = Column(Integer, nullable=True)
#
#     birthplace = Column(String, nullable=True)
#     family = Column(String, nullable=True)
#     photo_url = Column(String, nullable=True)


if __name__ == '__main__':
    make_original_tables()
    cls = add_versioning(Article, engine)
    update_articles(cls)

    # session = sessionmaker(bind=engine)()
    # sa.orm.configure_mappers()
    # Base.metadata.create_all(engine)
    # person_1 = Person(
    #     id=1,
    #     external_id='1',
    #     name_full='Sarah Smith',
    #     name_first='Sarah',
    #     name_last='Smith',
    # )
    # session.add(person_1)
    #
    # session.commit()
    # add_versioning(Person, engine)
    # session.close()
    # session = sessionmaker(bind=engine)()
    # query_person = session.query(Person).get(1)
    # query_person.name_first='Lara'
    # session.commit()
    # print(query_person)
    # assert query_person.versions[0].name_first == 'Sarah'
