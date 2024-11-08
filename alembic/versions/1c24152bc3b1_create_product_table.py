"""create product table

Revision ID: 1c24152bc3b1
Revises: 
Create Date: 2024-11-08 14:24:01.470613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c24152bc3b1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('products', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('name', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('products')
    pass
