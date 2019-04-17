"""Add a column

Revision ID: 0f7c1f1359a0
Revises: 9ea99bb87311
Create Date: 2019-04-12 15:39:15.208630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy_continuum import make_versioned

revision = '0f7c1f1359a0'
down_revision = '9ea99bb87311'
branch_labels = None
depends_on = None


def upgrade():
    make_versioned(user_cls=None)
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade():
    op.drop_column('account', 'last_transaction_date')