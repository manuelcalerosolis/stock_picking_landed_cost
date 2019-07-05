# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from collections import defaultdict

from odoo import api, fields, models, tools, _
from odoo.addons import decimal_precision as dp
from odoo.addons.stock_landed_costs.models import product
from odoo.exceptions import UserError

class LandedCost(models.Model):
    _inherit = 'stock.landed.cost'

    @api.model
    def default_get(self,default_fields):
        """ Compute default partner_bank_id field for 'out_invoice' type,
        using the default values computed for the other fields.
        """
        res = super(LandedCost, self).default_get(default_fields)

        logging.getLogger("default_picking_id").warning("*"*80)
        logging.getLogger("default_picking_id").warning(self._context.get('default_picking_id'))

        if self._context.get('default_picking_id') != None:
            res['picking_ids'] = [self._context.get('default_picking_id')]

        return res
