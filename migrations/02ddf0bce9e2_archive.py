"""add archive comment

Revision ID: 02ddf0bce9e2
Revises: c6b47d9442a9
Create Date: 2018-08-15 14:49:26.964138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02ddf0bce9e2'
down_revision = 'c6b47d9442a9'
branch_labels = ()
depends_on = None


def upgrade():
    op.add_column(
        'todos',
        sa.Column('archived', sa.Boolean)
    )

def downgrade():
    op.drop_column('todos', 'archived')
