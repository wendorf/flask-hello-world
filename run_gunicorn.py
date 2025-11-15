import sys
from gunicorn.app.wsgiapp import run

if __name__ == "__main__":
    # Mimic: gunicorn app:app
    sys.argv = ["gunicorn", "app:app"]
    run()

