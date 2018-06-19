import dataent
import foundation

no_cache = 1
def get_context(context):
	if dataent.session.user != 'Guest':
		context.show_sidebar = True
