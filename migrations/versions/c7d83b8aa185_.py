"""empty message

Revision ID: c7d83b8aa185
Revises: 3c5f39cd6f58
Create Date: 2020-11-12 22:40:06.878325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7d83b8aa185'
down_revision = '3c5f39cd6f58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('credits', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'credits')
    # ### end Alembic commands ###
