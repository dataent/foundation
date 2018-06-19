# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '0.0.1'

from dataent.utils import getdate
import dataent

def get_last_membership():
	'''Returns last membership if exists'''
	member_id = dataent.db.get_value("Member", {'email': dataent.session.user}, "name")
	last_membership = []
	if member_id:
		last_membership = dataent.get_all('Membership', 'name,to_date,membership_type',
			dict(member=member_id, paid=1), order_by='to_date desc', limit=1)

	return last_membership and last_membership[0]

def get_all_memberships_of_one_member():
	'''Returns all memberships'''
	member_id = dataent.db.get_value("Member", {'email': dataent.session.user}, "name")
	all_memberships = []
	if member_id:
		all_memberships = dataent.get_all('Membership', 'name,from_date,to_date,membership_type,amount,currency',
			dict(member=member_id, paid=1), order_by='to_date desc')

	return all_memberships

def is_member():
	'''Returns true if the user is still a member'''
	last_membership = get_last_membership()
	if last_membership and getdate(last_membership.to_date) > getdate():
		return True
	return False
