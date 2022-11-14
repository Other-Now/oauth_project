# oauth_project
After downloading the zip file:
  Open the folder on vscode and runthe command:
      pip install djangorestframework
      python manage.py startapp name_of_app
  create serialization folder
  set database in setting


#  Now to run our server. Run the following commands – 
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver


# setup google oauth:
  Head over to Google Developer APIs Console and create a new project.


  
  Now, head over to http://127.0.0.1:8000/accounts/login/ to see.
    Then, create a new OAuth client ID under Credentials. Select Web application for the Application type.

  Then, add:

  http://127.0.0.1:8000 under Authorized JavaScript origins.
  http://127.0.0.1:8000/accounts/google/login/callback/ under Authorized redirect URIs.
  
  Open http://127.0.0.1:8000/admin and login to Django Admin. 
  Under Sites click Add and put 127.0.0.1:8000 as both the Domain name and Display name.
  
  Then, under Social Applications click Add and fill in the details as follows:

  Provider: Google
  Name: OAuth App
  Client id: <The client ID you created in step 4>
  Secret key: <The Secret key you created in step 4>
  Sites: 127.0.0.1:8000
  
  #  Now to run our server. Run the following commands – 
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    
    
    # Now, *To run this go to http://127.0.0.1:8000/accounts/login/ to see*.
