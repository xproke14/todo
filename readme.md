# About  

For more details about this project see git master branch. This branch is for enabling https. I successfully followed this tutorial to make things work: https://mindsers.blog/post/https-using-nginx-certbot-docker/. Some parts of the code are modified but setup steps remained followed. Files which needs to be customized are .env, specifically ALLOWED_HOSTS variable and web/default.conf where you need to enter your hostname. After running certbot command as per tutorial above, uncomment lines in web/default.conf.

