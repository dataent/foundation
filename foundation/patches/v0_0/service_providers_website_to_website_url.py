import dataent

def execute():
	dataent.reload_doc("epaas_foundation", "doctype", "service_provider")
	dataent.db.sql('''
	update `tabService Provider`
	set website_url = website
	''')
