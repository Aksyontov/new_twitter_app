"""empty message

Revision ID: c2b9246dc3a6
Revises: 804dc87dd324
Create Date: 2024-07-29 11:13:20.091614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c2b9246dc3a6'
down_revision: Union[str, None] = '804dc87dd324'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('has_image', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'has_image')
    # ### end Alembic commands ###