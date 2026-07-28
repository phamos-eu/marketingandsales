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

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/marketing_and_sales/css/marketing_and_sales.css"
# app_include_js = "/assets/marketing_and_sales/js/marketing_and_sales.js"

# include js, css files in header of web template
# web_include_css = "/assets/marketing_and_sales/css/web.css"
# web_include_js = "/assets/marketing_and_sales/js/web.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home" #  for role in ["Role"]
# }

# Website Route Rules
# -------------------

website_route_rules = [
	{"from_route": "/sales", "to_route": "Sales"}
]

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "marketing_and_sales.install.before_install"
# after_install = "marketing_and_sales.install.after_install"

# Desk Notifications
# ------------------

# See frappe.core.notifications.get_notification_config

# notification_config = "marketing_and_sales.notifications.update_notification_config"

# Permissions
# ------------

# permission_query_conditions = {
# 	"Event": frappe.utils.user.get_permission_query_conditions_for_events,
# }

# has_permission = {
# 	"Event": frappe.utils.user.has_permission_for_event,
# }

# DocType Class
# ----------------

# override doctype class
# override_doctype_class = {
# 	"Task": "custom_app.task.doctype.task.task.CustomTask"
# }

# Document Naming Rules
# --------------------

# before_naming = {
# 	"DocType": "custom_app.utils.get_custom_naming_rule"
# }

# force_naming = {
# 	"DocType": "submitter.{{doc.name}}"
# }

# Custom Scripts
# --------------

# custom_scripts = {
# 	"DocType": "public/js/doctype_custom.js"
# }

# Custom CSS
# ----------

# custom_css = {
# 	"DocType": "public/css/doctype_custom.css"
# }

# Fixtures
# --------

# fixtures = [
# 	"Custom Field",
# 	"Custom Script",
# 	"Role",
# 	"Print Format",
# 	"Property Setter",
# 	"Workflow",
# 	"Workflow State",
# 	"Workflow Action"
# ]

# Autopatch
# --------

# auto_patch = [
# 	"marketing_and_sales.patches.update_patch.update_patch"
# ]
