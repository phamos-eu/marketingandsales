# Copyright (c) 2026, Phamos EU and contributors
# For license information, see LICENSE or https://www.gnu.org/licenses/agpl-3.0

"""
Hooks for Marketing and Sales App
"""

from __future__ import unicode_literals
import frappe

app_name = "marketingandsales"
app_title = "Marketing and Sales"
app_publisher = "Phamos EU"
app_description = "A Frappe app for managing marketing and sales workflows."
app_email = "support@phamos.eu"
app_license = "AGPL-3.0"
app_version = "0.0.1"

# Website Route Rules
# -------------------

website_route_rules = [
	{"from_route": "/sales", "to_route": "sales"},
]

# Website Context
# -----------------

website_context = {
	"sales": "marketingandsales/www/sales.py"
}
