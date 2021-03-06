"""empty message

Revision ID: 82a49bad8f59
Revises: 2e307aee9b87
Create Date: 2020-11-09 06:21:53.505134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82a49bad8f59'
down_revision = '2e307aee9b87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('post_type', sa.Text(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('caption', sa.Text(), nullable=True),
    sa.Column('ingredients', sa.Text(), nullable=True),
    sa.Column('instructions', sa.Text(), nullable=True),
    sa.Column('last_edit', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
