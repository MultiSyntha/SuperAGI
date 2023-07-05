"""added_agent_execution_config

Revision ID: 83424de1347e
Revises: c02f3d759bf3
Create Date: 2023-07-03 22:42:50.091762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83424de1347e'
down_revision = 'c02f3d759bf3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agent_execution_configs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('agent_execution_id', sa.Integer(), nullable=True),
    sa.Column('key', sa.String(), nullable=True),
    sa.Column('value', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agent_execution_configs')
    # ### end Alembic commands ###
