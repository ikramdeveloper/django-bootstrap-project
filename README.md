# Django & Bootstrap Project

One page bootstrap template with django user authentication

#### Create virtual environment (On windows):

```
python -m venv <path>
```

#### Activate virtual environment (On windows):

Using bash:

```
source <venv>/Scripts/activate
```

Using CMD:

```
<venv>\Scripts\activate.bat
```

Using Powershell:

```
<venv>\Scripts\Activate.ps1
```

#### Deactivate virtual environment

```
deactivate
```

#### Create text file listing all your project dependencies

```
pip freeze > requirements.txt
```

#### Install all dependencies in requirements.txt file

```
pip install -r requirements.txt
```

#### Start django project

Activate virtual environment and first install django (if not installed with the previous command)

```
pip install django
```

Create django project using django-admin

```
django-admin startproject <project name>
```

#### Create django app

Move to root directory (root directory means the directory that contains manage.py file) and create app using manage.py

```
python manage.py startapp <app name>
```

#### Create django admin

```
python manage.py createsuperuser
```

#### Make migrations

```
python manage.py makemigrations
```

#### Migrate to database

```
python manage.py migrate
```

---

Bootstrap template used in this project: [View on bootstrapmade.com](https://bootstrapmade.com/demo/OnePage/)
