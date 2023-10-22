"""Renaming column id to student_id

Revision ID: 18e6b1ead049
Revises: 791279dd0760
Create Date: 2023-10-22 11:45:12.760712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18e6b1ead049'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('id', 'student_id')



def downgrade() -> None:
    op.alter_column('student_id', 'id')
