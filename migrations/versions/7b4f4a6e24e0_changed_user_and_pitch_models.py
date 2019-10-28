"""changed user and pitch models

Revision ID: 7b4f4a6e24e0
Revises: 421d9d6842bb
Create Date: 2019-10-27 09:18:56.661649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b4f4a6e24e0'
down_revision = '421d9d6842bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pitch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch', sa.String(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('upvote', sa.Integer(), nullable=True),
    sa.Column('downvote', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pitches')
    op.add_column('users', sa.Column('role_id', sa.Integer(), nullable=True))
    op.drop_constraint('users_pitch_id_fkey', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    op.drop_column('users', 'pitch_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_pitch_id_fkey', 'users', 'pitches', ['pitch_id'], ['id'])
    op.drop_column('users', 'role_id')
    op.create_table('pitches',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('content', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('upvote', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('downvote', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pitches_pkey')
    )
    op.drop_table('pitch')
    op.drop_table('roles')
    # ### end Alembic commands ###
