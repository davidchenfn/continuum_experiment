"""Add versioning v2

Revision ID: 075147b0991c
Revises: 97dce116bcc8
Create Date: 2019-04-12 15:50:15.320928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy_continuum import make_versioned

revision = '075147b0991c'
down_revision = '97dce116bcc8'
branch_labels = None
depends_on = None


def upgrade():
    make_versioned(user_cls=None)
    op.drop_column('account', 'last_transaction_date')


def downgrade():
    pass
