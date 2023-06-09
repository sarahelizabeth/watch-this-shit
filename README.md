# watch-this-shit
Watch This Shit You Guys: A recommendation platform for People Who Don't Suck

Welcome to my Django + Bulma recommendation-based social media platofrm for People Who Don't Suck. 

If you want to get this running locally, you will need Python, pip, and virtualenv installed.

1. Clone repository
2. Create virtual environment (use whatever name you want as long as it Doesn't Suck)
  `python -m venv social`
3. Start virtual environment
  - Windows: `social\Scripts\activate`
  - Linux & OS X: `source social/Scripts/activate`
4. Install requirements
  `pip install -r requirements.txt`
5. Migrate that DB
  - `python manage.py makemigrations`
  - `python manage.py migrate`
6. Start the server
  `python manage.py runserver`
  
Visit `127.0.0.1:8000` to see the site!
