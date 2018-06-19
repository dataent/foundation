import dataent

def execute():
	for job in dataent.get_all("Portal Job"):
		dataent.db.set_value("Portal Job", job.name, "route", "epaas-job/{0}".format(job.name.encode('utf-8')),
			update_modified=False)

