"""empty message

Revision ID: f4cad5d0722a
Revises: 03eb819ed9ff
Create Date: 2023-12-11 13:13:37.704059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4cad5d0722a'
down_revision = '03eb819ed9ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'created_at')
    # ### end Alembic commands ###
