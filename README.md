** WEBLY

    Webly is web-application that allows its users to post their best projects. Other users are also in a position to view projects and register in-order to have access other features of the app like posting their own projects.

** AUTHOR
    Leonidah Mwamto

** DESCRIPTION

    Webly is a django based web application that gives its users the ability to view, post and rate projects. User also require to be authenticated in order to create, update or delete their profiles. Also, after authentication the user can post their favorite projects. The rating of projects is based on usability, design, and the content.

** SETUP & INSTALLATION

    To use this application:
    * Clone it from Github under https://github.com/LeoAmby/webly.git

    You'll need the following to be able to work around the project:
        * python3.6 installed
        *Create a virtual environment
            python3 -m venv virtual
        *Activate the virtual environment
            source virtual/bin/activate

        *Install django
            pip install d==1.11.23
        *Install all django dependencies in the requirements.txt
            pip install -r requirements.txt
        *Create a django App.the project is already created for you.
            django-admin startapp <nameOfYourApp>

** USER STORIES

    * Users on visiting the site are in a position to see the purpose of the web app on the landing page. 
    * Users can view projects that have been posted with their details that include, the creator, date posted and the link to the entire project.
    * A user has the chance to register and after authentication, they can post their own projects for others to view.
    * Users also can rate the projects posts on the basis of usability, design and content.

** TECHNOLOGIES USED

    * python3.6
    * django==2.4.6
    * postgresql
    * Bootstrap4
    * Crispy-Forms
    * HTML5
    * Github for task management
    * Heroku for deployment

** LINCENCE
    [MIT]