"""migration

Revision ID: 3ddfe5417d3b
Revises: 
Create Date: 2018-03-25 23:35:58.602504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ddfe5417d3b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('PersonalCollections')
    op.add_column('personalCollections', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'personalCollections', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'personalCollections', type_='foreignkey')
    op.drop_column('personalCollections', 'user_id')
    op.create_table('PersonalCollections',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"PersonalCollections_id_seq"\'::regclass)'), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='PersonalCollections_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='PersonalCollections_pkey')
    )
    # ### end Alembic commands ###
