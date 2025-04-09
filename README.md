# Bank security control panel
This project displays:
- number of active access cards
- the number of users who are currently in storage
- information about the selected user
  
on the web page of the bank's vault.
## How to install
This project uses: 
### Frameworks: 
[django framework](https://proglib.io/p/django-s-nulya-chast-1-pishem-mnogopolzovatelskiy-blog-dlya-kluba-lyubiteley-zadach-python-2022-06-06?ysclid=m98dche8su133012813)
### Libraries: 
[dotenv](https://betterdatascience-page.pages.dev/python-dotenv/), [os](https://docs.python.org/3/library/os.html), [functools](https://docs.python.org/3/library/functools.html)

Create and activate a virtual environment
```
python -m venv venv
source ./venv/Scripts/activate # for Windows
source ./venv/bin/activate #for Linux and macOS
```
Python3 should already be installed. Use `pip` (or `pip3`, there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
To save the data from prying eyes, we will create an .env file in which we will place: `ENGINE`, `HOST`, `PORT`, `NAME`, `USER`, `PASSWORD`.
Let's do it this way: 
```
DB_ENGINE=your secret information
DB_HOST=your secret information
DB_PORT=your secret information
DB_NAME=your secret information
DB_USER=your secret information
DB_PASSWORD=your secret information
DB_SECRET_KEY=your secret information
DB_DEBUG=your secret information
```
## How to launch
To launch the project, you need to enter this command in the console:
```
python manage.py runserver 0.0.0.0:8000
```

