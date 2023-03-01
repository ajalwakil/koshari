# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import POS Order from CSV File | Import POS Order from Excel file | Import POS Orders from CSV/Excel File",
    "author": "Softhealer Technologies",
    "license": "OPL-1",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Point Of Sale",
    "summary": "Import Point Of Sale Product,Import POS Product,Import POS Order,Import Point Of Sale Order,import multiple pos order,import multiple point of sale order,import pos order lines,import point of sale order lines,import pos,import point of sales import pos order import pos import order point of sale order import point of sale Odoo",
    "description": """Do you want to import Point Of Sale From CSV/Excel? This module is useful to import POS orders from the CSV or Excel files. You can import POS based on name, internal reference number & barcode. Import Point Of Sale Product From CSV/Excel Odoo, Import POS Product From CSV/Excel Odoo Import POS Order Product From CSV,  Import POS Product From Excel,Import POS Product From XLS, Import POS Product From XLSX Moule, Import Point Of Sale Product From Excel, Import Point Of Sale Product From CSV, Import Point Of Sale Product From XLS, Import Point Of Sale Product From XLSX Odoo""",
    "version": "16.0.1",
    "depends": ["base", "sh_message", "point_of_sale"],
    "application": True,
    "data": [
            'security/import_pos_groups.xml',
            'security/ir.model.access.csv',
            'wizard/import_pos_wizard_views.xml',
            'views/pos_views.xml',
    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/4t-PfKOY5o4",
    "auto_install": False,
    "installable": True,
    "price": 35,
    "currency": "EUR"
}
