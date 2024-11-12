"""setting fk columns

Revision ID: 03fcac70ab29
Revises: 1f8d1e9376ae
Create Date: 2024-11-11 16:39:52.698373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03fcac70ab29'
down_revision: Union[str, None] = '1f8d1e9376ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

#user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)


def upgrade() -> None:
    op.create_unique_constraint('uq_user_email', 'user', ['email'])
    op.add_column('product', sa.Column('user_id', sa.Integer(), nullable=False))
    # op.create_foreign_key('product_user_fk', source_table="product", referent_table="user", 
    #                       local_cols=["user_id"], remote_cols=["id"], ondelete="CASCADE")
    
    pass


def downgrade() -> None:
    op.drop_constraint('uq_user_email', 'user', type_='unique')
    op.drop_column('product', 'user_id')
    # op.drop_constraint('product_user_fk', table_name='product')
    pass
