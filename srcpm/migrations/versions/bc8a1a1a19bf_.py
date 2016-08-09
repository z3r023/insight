"""empty message

Revision ID: bc8a1a1a19bf
Revises: 6e6dcb77d916
Create Date: 2016-07-04 11:30:20.591590

"""

# revision identifiers, used by Alembic.
revision = 'bc8a1a1a19bf'
down_revision = '6e6dcb77d916'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assets', sa.Column('chkdate', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('assets', 'chkdate')
    ### end Alembic commands ###