"""create user table

Revision ID: 1f8d1e9376ae
Revises: 75ab76231d28
Create Date: 2024-11-11 16:34:34.306982

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f8d1e9376ae'
down_revision: Union[str, None] = '75ab76231d28'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# id = Column(Integer, primary_key=True, nullable=False)
#     email = Column(String, nullable=False, unique=True)
#     password = Column(String, nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
def upgrade() -> None:
    op.create_table('user')
    op.add_column('user', sa.Column('id', sa.Integer(), primary_key=True, nullable=False))
    op.add_column('user', sa.Column('password', sa.String(), nullable=False))
    op.add_column('user', sa.Column('email', sa.String(), nullable=False))
    op.add_column('user', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
 
    pass


def downgrade() -> None:
    op.drop_table('user')
    op.drop_column('user', 'id')
    op.drop_column('user', 'password')
    op.drop_column('user', 'email')
    op.drop_column('user', 'created_at')
 
    pass
