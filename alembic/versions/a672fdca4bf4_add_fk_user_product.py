"""add fk user - product

Revision ID: a672fdca4bf4
Revises: aca64387804c
Create Date: 2024-11-11 18:07:45.664363

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a672fdca4bf4'
down_revision: Union[str, None] = 'aca64387804c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_foreign_key('product_user_fk', source_table="product", referent_table="user",
                          local_cols=["user_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("product_user_fk", table_name="product")
    pass
