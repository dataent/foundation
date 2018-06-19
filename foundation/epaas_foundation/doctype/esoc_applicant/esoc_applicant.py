# -*- coding: utf-8 -*-
# Copyright (c) 2018, EOSSF and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from dataent import _
import dataent
from dataent.model.document import Document

class ESoCApplicant(Document):
	def validate(self):
		self.validate_dob()
		self.validate_email_type(self.email_id)
		self.validate_agreement_check()

	def validate_email_type(self, email):
		from dataent.utils import validate_email_add
		validate_email_add(email.strip(), True)

	def validate_dob(self):
		from dataent.utils import now_datetime, getdate
		today = now_datetime().date()
		if getdate(self.date_of_birth) >= today:
			dataent.throw(_("Invalid Date of Birth."))

	def validate_agreement_check(self):
		from dataent.utils import cint
		if not cint(self.terms_and_conditions):
			dataent.throw(_("You must agree to the terms and consitions."))
