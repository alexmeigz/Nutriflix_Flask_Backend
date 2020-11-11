"""empty message

Revision ID: e032e55126b5
Revises: 4cc1ea620934
Create Date: 2020-11-11 00:55:08.777437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e032e55126b5'
down_revision = '4cc1ea620934'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.Text(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('account_type', sa.Text(), nullable=True),
    sa.Column('vendor_location', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###