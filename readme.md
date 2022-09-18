
# About

This is a dockerized Django applicatition which enables registered and signed users to create and maintain their tasks listed in various categories.  
This project is split into 3 apps. User section provides means for user registration, login and profile maintenace including selection of predefined profile pictures. Default user model is modified so that email field is used as a username.  
Category and Task sections contain code to create tasks and categorize them.  
Frotend utilizes Bootstrap in Django template files. There is not a separate frontend application built in JS.  
In order to stick closely with a real-world higher-scale setup, Django generic views which are similar to DRF generic views are used.  
Celery with Redis is used to send welcome emails but only in a dev compose file (not daemonized) in a block which is commented out (alongside with celery task in singnals.py under users app)

# Run code

Probably the easiest way how to run this code is to create .env file from .env.sample file. Enter your public IP into ALLOWED_HOSTS. You can keep other fields as they are as emailing is not in production version (it is a Celery task which is only in dev - as described above).