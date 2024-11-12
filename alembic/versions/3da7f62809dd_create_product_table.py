"""create product table

Revision ID: 3da7f62809dd
Revises: 
Create Date: 2024-11-11 16:11:37.741095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3da7f62809dd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('product', sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True))
    
    pass


def downgrade() -> None:
    op.drop_table('product')
    pass
