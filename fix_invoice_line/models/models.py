# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveLineInh(models.Model):
    _inherit = "account.move.line"


    _sql_constraints = [
        (
            "check_credit_debit",
            "CHECK(display_type IN ('line_section', 'line_note') OR credit * debit=0)",
            "Wrong credit or debit value in accounting entry !"
        ),
        (
            "check_amount_currency_balance_sign",
            """CHECK(
                display_type IN ('line_section', 'line_note')
                OR (
                    (balance <= 0 AND amount_currency <= 0)
                    OR
                    (balance >= 0 AND amount_currency >= 0)
                )
            )""",
            "The amount expressed in the secondary currency must be positive when account is debited and negative when "
            "account is credited. If the currency is the same as the one from the company, this amount must strictly "
            "be equal to the balance."
        ),
        # (
        #     "check_accountable_required_fields",
        #     "CHECK(display_type IN ('line_section', 'line_note') OR account_id IS NOT NULL)",
        #     "Missing required account on accountable line."
        # ),
        (
            "check_non_accountable_fields_null",
            "CHECK(display_type NOT IN ('line_section', 'line_note') OR (amount_currency = 0 AND debit = 0 AND credit = 0 AND account_id IS NULL))",
            "Forbidden balance or account on non-accountable line"
    ),
]
