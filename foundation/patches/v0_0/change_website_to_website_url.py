import dataent

def execute():
    dataent.db.sql('''
        ALTER TABLE `tabFoundation Fellowship` CHANGE `website` `website_url` varchar(140);
    ''', ignore_ddl = True)
