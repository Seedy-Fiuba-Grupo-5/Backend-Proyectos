"""Initial migration

Revision ID: 142e9ab35c0b
Revises: 
Create Date: 2021-06-23 13:49:30.912572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '142e9ab35c0b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=128), nullable=False),
                    sa.Column('description', sa.String(
                        length=128), nullable=False),
                    sa.Column('hashtags', sa.String(
                        length=1000), nullable=False),
                    sa.Column('type', sa.String(length=128), nullable=False),
                    sa.Column('goal', sa.Integer(), nullable=False),
                    sa.Column('endDate', sa.String(
                        length=128), nullable=False),
                    sa.Column('location', sa.String(
                        length=128), nullable=False),
                    sa.Column('image', sa.Text(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projects')
    # ### end Alembic commands ###
