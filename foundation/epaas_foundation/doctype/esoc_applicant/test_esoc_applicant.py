from __future__ import unicode_literals
from dataent import _
import dataent
import unittest

class TestESoCApplicant(unittest.TestCase):
	def validate(self):
		dataent.throw(_("Test Exception"))
