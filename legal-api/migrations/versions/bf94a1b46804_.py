"""empty message

Revision ID: bf94a1b46804
Revises: ed12492e70f8
Create Date: 2019-07-17 14:37:24.877394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf94a1b46804'
down_revision = 'ed12492e70f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('filings', sa.Column('payment_completion_date', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('filings', 'payment_completion_date')
    # ### end Alembic commands ###
