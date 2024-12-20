"""add Department

Revision ID: 1cfb78cc9387
Revises: 3efcfc5b8286
Create Date: 2024-11-28 21:47:07.038248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cfb78cc9387'
down_revision = '3efcfc5b8286'
branch_labels = None
depends_on = None



# 

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###