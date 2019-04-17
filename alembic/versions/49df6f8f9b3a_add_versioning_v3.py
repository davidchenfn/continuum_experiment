"""Add versioning v3

Revision ID: 49df6f8f9b3a
Revises: 075147b0991c
Create Date: 2019-04-12 15:57:01.531820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_continuum import make_versioned

revision = '49df6f8f9b3a'
down_revision = '075147b0991c'
branch_labels = None
depends_on = None

Base = declarative_base()


def upgrade():
    session = sessionmaker(bind=engine)()
    make_versioned(user_cls=None)
    # table_class.__versioned__ = {}
    # table_class.__table_args__ = {'extend_existing': True}
    class Article(Base):
        __versioned__ = {}
        __tablename__ = 'article'
        __table_args__ = {'extend_existing': True}

        id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
        name = sa.Column(sa.Unicode(255))
        content = sa.Column(sa.UnicodeText)
    sa.orm.configure_mappers()
    Base.metadata.create_all(engine)
    session.commit()
    session.close()
    pass


def downgrade():
    pass
