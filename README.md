# Resume Project
This project created according to web programming courses Master, Mr. Khademi order.

## Run Project
1. clone the project

2. create a virtualenv:

    ```bash
    virtualenv .venv --python=python3
    source .venv/bin/activate
    ```

3. install requirements:
    
    ```bash
    install -r requirements/development.txt
    ```

4. create settings and env file:
    
    ```bash
    make settings
    make env
    ```

5. create database with docker:

    ``` bash
    docker run -d --name resume_db -e POSTGRES_DB=resume_db -e POSTGRES_USER=resume_user -e POSTGRES_PASSWORD=1234 -p 5432:5432 postgres
    ```

    ###### please make sure you change authentication conditions.
6. migrate and collectstatic:

    ```bash
    python3 source/manage.py migrate
    python3 source/manage.py collectstatic
    ```

7. create a superuser:

    ```bash
    python3 source/manage.py createsuperuser
    ```

8. run project:

    ```bash
    python3 source/manage.py runserver
    ```
