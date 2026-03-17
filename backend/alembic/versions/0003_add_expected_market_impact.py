"""add expected_market_impact to events

Revision ID: 0003_add_expected_market_impact
Revises: 0002_add_report_headline
Create Date: 2026-03-17
"""

from alembic import op
import sqlalchemy as sa


revision = "0003_add_expected_market_impact"
down_revision = "0002_add_report_headline"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "events",
        sa.Column("expected_market_impact", sa.String(32), nullable=False, server_default="Medium"),
    )


def downgrade() -> None:
    op.drop_column("events", "expected_market_impact")
