"""First migration

Revision ID: b04450eb6fcb
Revises: 
Create Date: 2024-03-03 16:18:56.047248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b04450eb6fcb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('achievement',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('title', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('admin',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('date_of_request_creation', sa.DateTime(), nullable=False),
    sa.Column('role_assignment_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('moderator',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('date_of_request_creation', sa.DateTime(), nullable=False),
    sa.Column('role_assignment_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=4096), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('date_of_registration', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('username')
    )
    op.create_table('accesses',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('access_to_content_1', sa.Boolean(), nullable=False),
    sa.Column('access_to_content_2', sa.Boolean(), nullable=False),
    sa.Column('access_to_content_3', sa.Boolean(), nullable=False),
    sa.Column('access_to_content_4', sa.Boolean(), nullable=False),
    sa.Column('access_to_content_5', sa.Boolean(), nullable=False),
    sa.Column('access_to_content_6', sa.Boolean(), nullable=False),
    sa.Column('access_to_content_7', sa.Boolean(), nullable=False),
    sa.Column('access_to_content_8', sa.Boolean(), nullable=False),
    sa.Column('access_to_content_9', sa.Boolean(), nullable=False),
    sa.Column('access_to_content_10', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('administrative_rights',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('is_admin_id', sa.BigInteger(), nullable=True),
    sa.Column('is_moderator_id', sa.BigInteger(), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['is_admin_id'], ['admin.id'], ),
    sa.ForeignKeyConstraint(['is_moderator_id'], ['moderator.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('is_admin_id'),
    sa.UniqueConstraint('is_moderator_id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('profile',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('achievement_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['achievement_id'], ['achievement.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    op.drop_table('administrative_rights')
    op.drop_table('accesses')
    op.drop_table('user')
    op.drop_table('moderator')
    op.drop_table('admin')
    op.drop_table('achievement')
    # ### end Alembic commands ###