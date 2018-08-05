# Cloud Authentication Server

This is the simplicitist's authentication server you can host on amazon aws or any other cloud platform

## What it does:
One simple thing: check if user has right key/secret pair.

## How to run:
Server startup: python manage.py runserver  
Client check key: http://<server_ip>:8000/auth/chkkey?key=blah&secret=blah  
Client generate key: http://<server_ip>:8000/auth/genkey  

## How to implement:
No fancy Stuff but Python Django framework

## What to do next:
Apache SSL, Support AnyDB, Data Customization, Administration Tools, etc...

