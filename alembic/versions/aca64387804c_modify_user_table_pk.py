"""modify user table pk

Revision ID: aca64387804c
Revises: 03fcac70ab29
Create Date: 2024-11-11 18:04:17.990986

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aca64387804c'
down_revision: Union[str, None] = '03fcac70ab29'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("user")
    op.create_table("user", sa.Column('id', sa.Integer(), primary_key=True, nullable=False, autoincrement=True))
    op.add_column('user', sa.Column('password', sa.String(), nullable=False))
    op.add_column('user', sa.Column('email', sa.String(), nullable=False))
    op.add_column('user', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.create_table('user')
    op.add_column('user', sa.Column('id', sa.Integer(), primary_key=True, nullable=False))
    op.add_column('user', sa.Column('password', sa.String(), nullable=False))
    op.add_column('user', sa.Column('email', sa.String(), nullable=False))
    op.add_column('user', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass
