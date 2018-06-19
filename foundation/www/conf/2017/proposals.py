import dataent
import dataent.www.list

def get_context(context):
	context.update(dataent.www.list.get_context(context,
		doctype='Conference Talk Proposal'))
