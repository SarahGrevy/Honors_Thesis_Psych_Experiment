from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
#SESSION_CONFIGS = [dict(name='Random_Order_1', num_demo_participants=2, app_sequence=['Shared_reality'], my_key=5, my_key2=0)]
SESSION_CONFIGS = [dict(name='Random_Order_1', num_demo_participants=2, app_sequence=['Welcome', 'Hermione_Test', 'Trials', 'Shared_reality','Context', 'Demographic'], my_key=5, my_key2=0)]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
ROOMS = [dict(name='my_room', display_name='my_room'), dict(name='dyad', display_name='dyad')]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


