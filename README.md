# Changing-environment
A script to be able to switch from say a Flask dev environment to a test environment. It was written with [Flask-playground](https://github.com/pn141/Flask-Playground) in mind but if you have a Flask application that uses a .env file to store Flask configuration variables, you shouldn't have any problems using it.

## Installation instructions
 - Clone the project in a temporary location:

```git clone https://github.com/pn141/Changing-environment```

 - This will create directory "Changing-environment", copy "change_app_context.py" and "helper_func.py" at the root of "Flask-playground" or at the root of your Flask application directory.
 
## Running the script
The script is looking for a couple of files:
 - Your Flask app file which in the case of "Flask-playground" is called "flask-playground.py"
 - A ".env" file which would also be located at the root "Flask-playground"
 
Start your virtual environment and opened up a command line at that location and type the following:

```python change_app_context.py -a flask-playground.py -c development -n testing```

The above command will change your Flask environment from "development" to "testing". You are now ready to start your Flask application. If you wanted to revert the changes and fall back to your "development" environment, stop Flask and run:

```python change_app_context.py -a flask-playground.py -c testing -n development```

## Known limitations:
- The script does not allow to specify a different location for the Flask app file or the .env. If these files are not located in the directory where the script is run, the command will likely fail.
- Apart from checking for IOError, the script does not do any kind of error handling. So if you misspell "development", "testing" or any other type of environment you allow with your application, the ".env" and Flask app files will be changed but Flask will probably not start.
- When the script starts, the .env file is changed first then the Flask app file. If the .env file is present in the current directory but the app file is not, the script will stop with an IOError but the .env file would have already been changed and will no longer be in sync with the Flask app file. This will result in Flask starting but not behaving as expected. In order to fix the issue, you will need to stop Flask and manually change the .env file if entry ```FLASK_ENV = <env>``` no longer matches entry ```app = create_app('<env>')``` in your Flask app file and restart Flask.
