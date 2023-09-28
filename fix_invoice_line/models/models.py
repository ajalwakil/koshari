# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosSessioninkk(models.Model):
    _inherit = 'pos.session'

    def action_pos_session_closing_control(self, balancing_account=False, amount_to_balance=0,
                                           bank_payment_method_diffs=None):
        bank_payment_method_diffs = bank_payment_method_diffs or {}
        for session in self:
            if any(order.state == 'draft' for order in session.order_ids):
                raise UserError(_("You cannot close the POS when orders are still in draft"))
            if session.state == 'closed':
                raise UserError(_('This session is already closed.'))
            session.write({'state': 'closing_control', 'stop_at': fields.Datetime.now()})
            if not session.config_id.cash_control:
                return session.action_pos_session_close(balancing_account, amount_to_balance, bank_payment_method_diffs)
            # If the session is in rescue, we only compute the payments in the cash register
            # It is not yet possible to close a rescue session through the front end, see `close_session_from_ui`
            if session.rescue and session.config_id.cash_control:
                default_cash_payment_method_id = self.payment_method_ids.filtered(lambda pm: pm.type == 'cash')[0]
                orders = self.order_ids.filtered(lambda o: o.state == 'paid' or o.state == 'invoiced')
                total_cash = sum(
                    orders.payment_ids.filtered(lambda p: p.payment_method_id == default_cash_payment_method_id).mapped(
                        'amount')
                ) + self.cash_register_balance_start

                session.cash_register_balance_end_real = total_cash

            return session.action_pos_session_validate(balancing_account, amount_to_balance, bank_payment_method_diffs)


    # Assume you have a POS session object 'pos_session' that you want to close forcefully
    # Call the function with appropriate parameters
            try:
                pos_session.action_pos_session_closing_control(
                    balancing_account=True,  # Set to True if you want to balance accounts
                    amount_to_balance=100.0,  # Specify the amount to balance (if required)
                    bank_payment_method_diffs={}  # Provide any bank payment method differences (if required)
                )
            except UserError as e:
                # Handle any exceptions or errors raised during the closing process
                print(f"Error: {e}")
