"""responsible for create table 

Revision ID: a46ab5bac2fa
Revises: 
Create Date: 2022-10-16 16:14:34.981183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a46ab5bac2fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts1',
                    sa.Column('id',sa.Integer(),nullable = False,primary_key= True),
                    sa.Column("title",sa.String(),nullable = False)
                    )
    pass


def downgrade() -> None:
    op.drop_table('posts1')
    pass
