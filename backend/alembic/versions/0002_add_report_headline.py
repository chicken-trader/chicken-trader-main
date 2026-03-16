"""add report_headline to followed_theses

Revision ID: 0002_add_report_headline
Revises: 0001_initial
Create Date: 2026-03-16
"""

from alembic import op
import sqlalchemy as sa


revision = "0002_add_report_headline"
down_revision = "0001_initial"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "followed_theses",
        sa.Column("report_headline", sa.Text(), nullable=False, server_default=""),
    )


def downgrade() -> None:
    op.drop_column("followed_theses", "report_headline")
