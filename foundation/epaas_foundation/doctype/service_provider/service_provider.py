# -*- coding: utf-8 -*-
# Copyright (c) 2015, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import dataent
from dataent.website.website_generator import WebsiteGenerator
from dataent.utils import get_datetime

class ServiceProvider(WebsiteGenerator):
	website = dataent._dict(
		condition_field = "show_in_website",
	)
	def validate(self):
		if not self.route:
			self.route = 'service-providers/' + self.scrub(self.name)

	def get_context(self, context):
		context.parents = [dict(label='All Service Providers',
			route='service-providers',
			title='All Service Providers')]
		if self.member:
			context.membership_type = dataent.get_value('Member', self.member, 'membership_type')
		if context.website and not context.website.startswith('http'):
			context.website = 'http://' + context.website
		if not context.image:
			if context.membership_type == "Gold":
				context.image = "/assets/foundation/img/gold.png"
			elif context.membership_type == "Silver":
				context.image = "/assets/foundation/img/silver.png"
			else:
				context.image = "/assets/foundation/img/default-membership-logo.png"

def send_alert_to_inactive_service_providers():
	for service_provider in dataent.get_all("Service Provider", fields=['email', 'title']):
		if get_last_login_diff(service_provider.email) == 80:
			send_reminder(service_provider)

def send_reminder(service_provider_details):
	message = dataent.render_template("foundation/templates/emails/inactivity_reminder.md", service_provider_details)
	dataent.sendmail(recipients=service_provider_details.email, subject="About account inactivity", message=message)

def get_last_login_diff(user):
	"""
		Returns difference between todays date and last login date
	"""
	last_login = dataent.db.get_value("User", user, ["last_login"])
	for x in xrange(1,10):
		print((get_datetime() - get_datetime(last_login)).days, user)
	return (get_datetime() - get_datetime(last_login)).days
