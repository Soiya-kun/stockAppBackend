"""add saved stock

Revision ID: 24fd94c8d7c9
Revises: 2f1650e30d53
Create Date: 2022-06-17 16:02:30.521492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24fd94c8d7c9'
down_revision = '2f1650e30d53'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('saved_stocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sc', sa.String(length=128), nullable=True),
    sa.Column('b_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_saved_stocks_b_date'), 'saved_stocks', ['b_date'], unique=False)
    op.create_index(op.f('ix_saved_stocks_id'), 'saved_stocks', ['id'], unique=False)
    op.create_index(op.f('ix_saved_stocks_sc'), 'saved_stocks', ['sc'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_saved_stocks_sc'), table_name='saved_stocks')
    op.drop_index(op.f('ix_saved_stocks_id'), table_name='saved_stocks')
    op.drop_index(op.f('ix_saved_stocks_b_date'), table_name='saved_stocks')
    op.drop_table('saved_stocks')
    # ### end Alembic commands ###
