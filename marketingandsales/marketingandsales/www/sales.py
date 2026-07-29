# Copyright (c) 2026, Phamos EU and contributors
# For license information, see LICENSE or https://www.gnu.org/licenses/agpl-3.0

"""SPA controller for /sales.

Frappe maps the URL from the HTML filename (sales.html -> /sales)
and loads this controller by converting the filename to the module name.
"""

from __future__ import annotations

import frappe

no_cache = 1


def get_context():
	if frappe.session.user == "Guest":
		frappe.local.flags.redirect_location = f"/login?redirect-to={frappe.request.path}"
		raise frappe.Redirect

	frappe.db.commit()
	boot = get_boot()
	context = frappe._dict()
	context.boot = boot
	context.csrf_token = boot.csrf_token
	return context


def get_boot():
	return frappe._dict(
		{
			"frappe_version": frappe.__version__,
			"default_route": "/sales",
			"site_name": frappe.local.site,
			"socketio_port": getattr(frappe.conf, "socketio_port", None),
			"csrf_token": frappe.sessions.get_csrf_token(),
			"setup_complete": frappe.db.get_single_value("System Settings", "setup_complete"),
			"sitename": frappe.local.site,
			"user": {
				"name": frappe.session.user,
				"full_name": frappe.get_value("User", frappe.session.user, "full_name"),
			},
			"timezone": {
				"system": frappe.utils.get_system_timezone(),
				"user": frappe.db.get_value("User", frappe.session.user, "time_zone")
				or frappe.utils.get_system_timezone(),
			},
		}
	)
