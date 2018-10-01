# -*- coding: utf-8 -*-
# Copyright 2016-2018 Camptocamp
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Stock no extra move",
    "summary": "Prevent creation of extra moves in picking processing",
    "version": "8.0.1.0.0",
    "category": "Logistics",
    "website": "https://camptocamp.com/",
    "author": "Camptocamp SA"
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "data": [
        "views/stock_config_settings.xml"
    ],
    "application": False,
    "installable": True,
    "depends": [
        'specific_stock',
    ],
}
