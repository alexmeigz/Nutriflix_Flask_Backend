"""empty message

Revision ID: 989a7d8a8969
Revises: e032e55126b5
Create Date: 2020-11-11 01:03:20.449438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '989a7d8a8969'
down_revision = 'e032e55126b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.Text(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('account_type', sa.Text(), nullable=True),
    sa.Column('vendor_location', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('email', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('account_type', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('vendor_location', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('user_id', name='user_pkey')
    )
    op.drop_table('users')
    # ### end Alembic commands ###
