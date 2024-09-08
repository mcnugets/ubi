"""Testing if db migration works. Migrate new column for user table

Revision ID: bc4f0db1b1a5
Revises: 
Create Date: 2024-09-01 20:24:08.735896

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc4f0db1b1a5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
