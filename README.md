Detailed Documentation of code:-

**have limitations in hosting, vercel dont allow to save file upload as it provides only read access to file system, kindly run local copy of the project to test hackathon creation features.

Note = {

    -> Avoid AI_planet_application it only has html files and views,
    -> All the operations or performed using RESTfull API in API folder
    -> Authentication used = sessionBased Authentication
    
}
 
default credintials:-

user 1:- [ username = admin, password = admin ]
user 2:- [ username = admin2, password = admin ]


API specifications and End points:-

1. http://127.0.0.1:8000/api/hackathons/<str:filterParam>

    A. If filterParam == "available"
        -> List all the available hackathons to enroll
    
    B. If filterParam == "enrolled"
        -> List all the enrolled hackathons of requsted user
    
    C. If filterParam == "submitted"
        -> List all the submissions made by user in the past

    D. If filterParam == "my_hackathons"
        -> List all the hackathons hosted or created by the user

    E. If filterParam == "create"
        -> create new hacakthon from POST data from http request

    
2. http://127.0.0.1:8000/api/hackathon/<str:action_name>/<int:hackathon_id>

    Note:- This end point requires filter parameter and hackathod id

    A. If filterParam == "submissions"
        -> List all the submissions made for that specific hackathon
    
    B. If filterParam == "view"
        -> Get details of specific hackathon

    C. If filterParam == "enroll"
        -> enroll the requsted user to the hackathon

    D. If filterParam == "submit"
        -> submit hackthon with file/image/link



Instructions to run server:-

0. pip install -r requirements.txt

1. python manage.py makemigrations and python manage.py migrate

2. python manage.py createsuperuser

3. python manage.py runserver