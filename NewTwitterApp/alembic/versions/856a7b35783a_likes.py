"""Likes

Revision ID: 856a7b35783a
Revises: 9a933f1d7977
Create Date: 2024-07-26 18:53:09.393138

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '856a7b35783a'
down_revision: Union[str, None] = '9a933f1d7977'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tweets', sa.Column('liked', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tweets', 'liked')
    # ### end Alembic commands ###
