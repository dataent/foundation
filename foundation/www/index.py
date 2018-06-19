# See license.txt

from __future__ import unicode_literals
import dataent

def get_context(context):
	out = {
		"events": dataent.get_all("Portal Event", fields=["event_title", "event_date", "details", "route"], filters=[["published", "=", 1]])
		}
	return out
