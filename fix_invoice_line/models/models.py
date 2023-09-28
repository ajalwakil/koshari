from odoo import api, fields, models


class PosSession(models.Model):
    _inherit = 'pos.session'

    def action_pos_session_close(self, balancing_account=False, amount_to_balance=0, bank_payment_method_diffs=None):
        bank_payment_method_diffs = bank_payment_method_diffs or {}

        # Add a condition to forcefully close the session, even if there are errors.
        if self.state == 'closing_control':
            self.state = 'closed'

        # Comment out or remove the following checks to bypass them
        # if any(order.state == 'draft' for order in self.order_ids):
        #     raise UserError(_("You cannot close the POS when orders are still in draft"))

        # if self.cash_register_id and self.cash_register_balance_end_real != amount_to_balance:
        #     raise UserError(_("The cash register is not balanced. Please balance it first."))

        # ... Add any other checks you want to bypass or modify ...

        # Remove the following line to disable the normal session validation
        return self._validate_session(balancing_account, amount_to_balance, bank_payment_method_diffs)
