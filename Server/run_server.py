import os

from app import create_app


if __name__ == '__main__':
    app = create_app('prodution')

    if 'SECRET_KEY' not in os.environ:
        print('[WARN] SECRET KEY is not set in the environment variable !!')

    app.run()
