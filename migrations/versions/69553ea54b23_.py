"""empty message

Revision ID: 69553ea54b23
Revises: 7e77aee1acaf
Create Date: 2016-06-13 23:46:27.992887

"""

# revision identifiers, used by Alembic.
revision = '69553ea54b23'
down_revision = '7e77aee1acaf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('created_date', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('updated_date', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'update_name')
    op.drop_column('users', 'created_date')
    ### end Alembic commands ###
