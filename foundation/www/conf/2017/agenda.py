# -*- coding: utf-8 -*-

from __future__ import unicode_literals

def get_context(context):
	context.agenda = [
		dict(
			title = 'Day 1: Developer Talks',
			items = [
				dict(time='10am-11am',
					title='Welcome',
					description='Discovering how Open Source has evolved over the years.'),
				dict(time='11am-12.30pm',
					title='Developing a feature for EPAAS',
					description='Learn the process of feature development and contribution'),
				dict(time='12.30pm-1.30pm',
					title='Lunch'),
				dict(time='2pm-3pm',
					title='UI Development in Frappé',
					description='Diving deep into the UI of Dataent and build a new barcode control'),
				dict(time='3pm-4pm',
					title='Designing Portals in Frappé',
					description='How to build web views, web forms and other website related topics'),
				dict(time='4pm-5pm',
					title='Deployment and Release',
					description='Understanding the Frappé release process and best practices for deployment and updating'),
			]
		),
		dict(
			title = 'Day 2: EPAAS Roadmap',
			items = [
				dict(time='10am-10.30am',
					title='Introduction to Hub',
					description='Our vision for open marketplace called Hub for an open web.'),
				dict(time='10.30am-11.30am',
					title='Localizations and Contribution Guidelines',
					description='How to design and contribute extensions for legal requirements for different countries.'),
				dict(time='11.30am-12.30pm',
					title='Integrations',
					description='How to build and contribute 3rd party integrations in EPAAS.'),
				dict(time='12.30pm-1.30pm',
					title='Lunch'),
				dict(time='2pm-2.30pm',
					title='EPAAS Roadmap',
					description='Taking a look at the most requested features in EPAAS and how do we prioritize them'),
				dict(time='2.30pm-5pm',
					title='Module Analysis',
					description='In this session will will look at each EPAAS module including Accounting, Manufacturing, CRM etc and discuss what should be the priority development in each of these modules')
			]
		),
		dict(
			title = 'Day 3: Community and User Talks',
			items = [
				dict(time='10am-11am',
					title='Welcome and EPAAS Foundation',
					description='A look back at what we have achieved in the 6 months and what is the vision for the EPAAS Foundation'),
				dict(time='11am-12pm',
					title='Business of EPAAS',
					description='A panel discussion on how to make money on EPAAS and build a sustainable eco-system'),
				dict(time='12pm-1pm',
					title='User Stories',
					description='Three EPAAS Users will share their EPAAS Journeys'),
				dict(time='1pm-2pm',
					title='Lunch'),
				dict(time='2pm-3pm',
					title='Feature Showcase',
					description='Three developers from the community will showcase the extensions they have built on EPAAS'),
				dict(time='3pm-4pm',
					title='The Road Ahead',
					description='Panel Disussion with Gold Members on how do we make EPAAS a mainstream ERP alternative to paid ERPs'),
				dict(time='4pm-5pm',
					title='Lightning Talks and Q&A',
					description='5 min lightning talks by the audience and Q&A with the foundation members'),

			]
		)
	]