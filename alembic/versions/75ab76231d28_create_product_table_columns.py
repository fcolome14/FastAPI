"""create product table columns

Revision ID: 75ab76231d28
Revises: 3da7f62809dd
Create Date: 2024-11-11 16:20:51.856769

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75ab76231d28'
down_revision: Union[str, None] = '3da7f62809dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
    
def upgrade() -> None:
    op.add_column('product', sa.Column('price', sa.Integer(), nullable=False))
    op.add_column('product', sa.Column('id_sale', sa.Boolean(), server_default=sa.text("false")))
    op.add_column('product', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('product', sa.Column('price', sa.Integer(), nullable=False))
    op.drop_column('product', sa.Column('id_sale', sa.Boolean(), server_default=sa.text("false")))
    op.drop_column('product', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass
