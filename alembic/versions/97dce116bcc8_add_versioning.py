"""Add versioning

Revision ID: 97dce116bcc8
Revises: 0f7c1f1359a0
Create Date: 2019-04-12 15:48:53.330708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy_continuum import make_versioned

revision = '97dce116bcc8'
down_revision = '0f7c1f1359a0'
branch_labels = None
depends_on = None


def upgrade():
    make_versioned(user_cls=None)
    pass


def downgrade():
    pass
