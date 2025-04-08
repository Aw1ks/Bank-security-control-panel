# Bank security control panel
This project displays:
- number of active access cards
- the number of users who are currently in storage
- information about the selected user
  
on the web page of the bank's vault.
# How to install
This project uses: 
## Frameworks: 
[django framework](https://proglib.io/p/django-s-nulya-chast-1-pishem-mnogopolzovatelskiy-blog-dlya-kluba-lyubiteley-zadach-python-2022-06-06?ysclid=m98dche8su133012813)
## Libraries: 
[dotenv](https://betterdatascience-page.pages.dev/python-dotenv/), [os](https://docs.python.org/3/library/os.html), [functools](https://docs.python.org/3/library/functools.html)

Python3 should already be installed. Use `pip` (or `pip3`, there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
To save the data from prying eyes, we will create an .env file in which we will place: `ENGINE`, `HOST`, `PORT`, `NAME`, `USER`, `PASSWORD`.
Let's do it this way: 
```
ENGINE=your secret information
HOST=your secret information
PORT=your secret information
NAME=your secret information
USER=your secret information
PASSWORD=your secret information
```
