# How to run a project locally.
+ python version – 3.4
+ If you do not have database migrations, then try to create copies of the project and there to carry out database migrations of individual project lists located in the settings.
+ To connect to the database MSSQL, you need to download ODBC and configure it.
# How to run tests.
1) go to folder 'aace-conf/conference'
2) run the 'python manage.py test --settings=conference.test_settings' command
3) see the result of the work
***
You must specify the variables in the settings:
+ CC_API_KEY
+ CC_ACCESS_TOKEN
+ CC_LIST
+ VIDEO_NETWORKS
+ CONFERENCE_TYPES
+ PROCESSORS
***
Required modules:
+ wkhtmltopdf
+ audiotools
