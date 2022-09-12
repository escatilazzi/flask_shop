"""order table

Revision ID: a2e54ff13be4
Revises: 7263e611883d
Create Date: 2022-09-11 15:29:44.281432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2e54ff13be4'
down_revision = '7263e611883d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.Column('cart_product_id', sa.Integer(), nullable=False),
    sa.Column('cart_user_id', sa.Integer(), nullable=False),
    sa.Column('cart_quantity', sa.Integer(), nullable=True),
    sa.Column('cart_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cart_product_id'], ['product.prod_id'], ),
    sa.ForeignKeyConstraint(['cart_user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('cart_id')
    )
    op.create_table('comment',
    sa.Column('com_id', sa.Integer(), nullable=False),
    sa.Column('com_user_id', sa.Integer(), nullable=False),
    sa.Column('com_comment', sa.String(length=5000), nullable=True),
    sa.Column('com_product_id', sa.Integer(), nullable=True),
    sa.Column('com_create_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['com_product_id'], ['product.prod_id'], ),
    sa.ForeignKeyConstraint(['com_user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('com_id')
    )
    op.create_table('order',
    sa.Column('ord_id', sa.Integer(), nullable=False),
    sa.Column('ord_user_id', sa.Integer(), nullable=False),
    sa.Column('ord_product_id', sa.Integer(), nullable=False),
    sa.Column('ord_quantity', sa.Integer(), nullable=False),
    sa.Column('ord_total', sa.Integer(), nullable=True),
    sa.Column('ord_country', sa.String(length=300), nullable=True),
    sa.Column('ord_city', sa.String(length=300), nullable=True),
    sa.Column('ord_address', sa.String(length=300), nullable=True),
    sa.Column('ord_phone', sa.String(length=300), nullable=True),
    sa.Column('ord_email', sa.String(length=300), nullable=True),
    sa.Column('ord_payment_method', sa.String(length=300), nullable=True),
    sa.Column('ord_start_pay_date', sa.DateTime(), nullable=True),
    sa.Column('ord_create_order_date', sa.DateTime(), nullable=True),
    sa.Column('ord_finish_pay_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ord_product_id'], ['product.prod_id'], ),
    sa.ForeignKeyConstraint(['ord_user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('ord_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('comment')
    op.drop_table('cart')
    # ### end Alembic commands ###