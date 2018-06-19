# -*- coding: utf-8 -*-
# Copyright (c) 2015, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import dataent
from dataent import _
from dataent.website.website_generator import WebsiteGenerator
import foundation

class PortalJob(WebsiteGenerator):
	def get_context(self, context):
		context.no_cache = True
		context.parents = [dict(label='View All Jobs',
			route='epaas-jobs', title='View All Jobs')]
		context.is_member = foundation.is_member()

	def validate(self):
		if not self.route:
			self.route = 'epaas-jobs/' + self.scrub(self.title)
		if not self.title:
			dataent.throw(_("Job Title is Mandatory for posting a job"))


def get_list_context(context):
	context.allow_guest = True
	context.no_cache = True
	context.title = 'EPAAS Jobs'
	context.no_breadcrumbs = True
	context.order_by = 'creation desc'
	context.introduction = '<div>Jobs for EPAAS Service Providers</div><br><a class="btn btn-primary" href="/my-jobs?new=1">Post A Job</a>'
