# Copyright (c) 2026, Phamos EU and contributors
# For license information, see LICENSE or https://www.gnu.org/licenses/agpl-3.0

from setuptools import setup, find_packages

with open("marketingandsales/version.txt", "r") as version_file:
	version = version_file.read().strip()

setup(
	name="marketingandsales",
	version=version,
	description="A Frappe app for managing marketing and sales workflows.",
	author="Phamos EU",
	author_email="support@phamos.eu",
	url="https://github.com/phamos-eu/marketingandsales",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=(
		"frappe>=16.0.0",
	),
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"Programming Language :: Python :: 3.11",
		"Framework :: Frappe",
		"Topic :: Office/Business",
	],
)
