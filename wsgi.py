# goes in /home/alexhalme/python/<python project>/wsgi.py
# don't forget to change 'test' below for the name of the main 'py' file to import
from videotron import app

if __name__ == "__main__":
    app.run()
