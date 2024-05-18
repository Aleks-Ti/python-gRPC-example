"""Added account table

Revision ID: a18962a1b0f6
Revises: 
Create Date: 2024-05-18 13:45:59.482471

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a18962a1b0f6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('fullname', sa.String(length=256), nullable=True),
    sa.Column('email', sa.String(length=256), nullable=True),
    sa.Column('password', sa.String(length=512), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_moderator', sa.Boolean(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('date_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('password')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
