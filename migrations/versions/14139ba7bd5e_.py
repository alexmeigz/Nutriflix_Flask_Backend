"""empty message

Revision ID: 14139ba7bd5e
Revises: f6933dc1ffa0
Create Date: 2020-12-03 06:16:16.602203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14139ba7bd5e'
down_revision = 'f6933dc1ffa0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('price', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'price')
    # ### end Alembic commands ###