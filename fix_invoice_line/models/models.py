from odoo import api, fields, models

class PosSession(models.Model):
    _inherit = 'pos.session'

    @api.model
    def action_force_close_pos_session(self):
        for session in self:
            # Check if there are any draft orders; if so, raise an error
            if any(order.state == 'draft' for order in session.order_ids):
                raise UserError(_("You cannot close the POS when orders are still in draft"))

            # Check if the session is already closed; if so, raise an error
            if session.state == 'closed':
                raise UserError(_('This session is already closed.'))

            # Update session state to 'closing_control'
            session.write({'state': 'closing_control', 'stop_at': fields.Datetime.now()})

            # Iterate through the orders and transactions to address missing accounts
            for order in session.order_ids:
                for payment in order.payment_ids:
                    # Check if the payment has a valid account; replace 'income_account_id' with the appropriate field
                    if not payment.income_account_id:
                        # You can set a default account or raise an error here based on your requirements
                        # For example, you can set a default income account like this:
                        # payment.write({'income_account_id': default_income_account_id})
                        raise UserError(_("Payment is missing a required income account."))

            # Update session state to 'closed'
            session.write({'state': 'closed'})

        return True
