import dotenv
from getenv import env

dotenv.read_dotenv()

bind = ['unix:./gunicorn.sock']
workers = env('WEB_CONCURRENCY', 2)
preload_app = True

accesslog = "/home/www-data/logs/{{ cookiecutter.project_name }}_gunicorn.access.log"
errorlog = "/home/www-data/logs/{{ cookiecutter.project_name }}_gunicorn.error.log"

proc_name = "{{ cookiecutter.project_name }}_gunicorn"

secure_scheme_headers = {"X-FORWARDED-PROTO": "https"}
x_forwarded_for_header = "X-FORWARDED-FOR"
