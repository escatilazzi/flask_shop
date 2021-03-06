"""empty message

Revision ID: 0961ffc974d0
Revises: 6928bd863367
Create Date: 2022-07-04 00:12:52.940367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0961ffc974d0'
down_revision = '6928bd863367'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('prod_id', sa.Integer(), nullable=False),
    sa.Column('prod_name', sa.String(length=3000), nullable=False),
    sa.Column('prod_price', sa.Float(), nullable=False),
    sa.Column('prod_desc', sa.Text(), nullable=False),
    sa.Column('prod_quantity', sa.Integer(), nullable=False),
    sa.Column('prod_category_id', sa.Integer(), nullable=True),
    sa.Column('prod_discounts_id', sa.Integer(), nullable=True),
    sa.Column('prod_created', sa.DateTime(), nullable=True),
    sa.Column('prod_modified', sa.DateTime(), nullable=True),
    sa.Column('prod_deleted', sa.DateTime(), nullable=True),
    sa.Column('prod_brand_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['prod_brand_id'], ['brands.bra_id'], ),
    sa.ForeignKeyConstraint(['prod_category_id'], ['categories.cat_id'], ),
    sa.ForeignKeyConstraint(['prod_discounts_id'], ['discounts.disc_id'], ),
    sa.PrimaryKeyConstraint('prod_id')
    )
    with op.batch_alter_table('brands', schema=None) as batch_op:
        batch_op.alter_column('bra_date',
               existing_type=sa.DATETIME(),
               nullable=True)

    with op.batch_alter_table('discounts', schema=None) as batch_op:
        batch_op.alter_column('disc_created',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('disc_modified',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('disc_deleted',
               existing_type=sa.DATETIME(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('discounts', schema=None) as batch_op:
        batch_op.alter_column('disc_deleted',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('disc_modified',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('disc_created',
               existing_type=sa.DATETIME(),
               nullable=False)

    with op.batch_alter_table('brands', schema=None) as batch_op:
        batch_op.alter_column('bra_date',
               existing_type=sa.DATETIME(),
               nullable=False)

    op.drop_table('product')
    # ### end Alembic commands ###
