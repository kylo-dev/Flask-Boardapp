"""empty message

Revision ID: 0e41fb8ca9de
Revises: 970082d0ee17
Create Date: 2023-01-31 19:26:45.067983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e41fb8ca9de'
down_revision = '970082d0ee17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer_voter', schema=None) as batch_op:
        batch_op.alter_column('answer_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer_voter', schema=None) as batch_op:
        batch_op.alter_column('answer_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
