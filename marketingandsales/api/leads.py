# Copyright (c) 2026, Phamos EU and contributors
# For license information, see LICENSE or https://www.gnu.org/licenses/agpl-3.0

"""API endpoints for leads."""

from __future__ import annotations

import frappe
from frappe import _


@frappe.whitelist()
def get_leads():
	"""Fetch all leads from ERPNext's Lead DocType.
	
	Returns:
		list: List of leads with 'name' and 'status' fields.
	"""
	if not frappe.has_permission("Lead", "read"):
		frappe.throw(_("Permission denied"), frappe.PermissionError)

	leads = frappe.get_all(
		"Lead",
		fields=["name", "status"],
		order_by="creation desc",
	)
	return leads
