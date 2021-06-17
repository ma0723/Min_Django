# Django

#### 이민아 



## Project

- Movie

  영화 정보의 CRUD 기능을 구현한 1일 실습 프로젝트입니다.

- Review

  커뮤니티 안에서 리뷰 기능의 CRUD 및 좋아요와 프로필 기능을 구현한 1일 실습 프로젝트입니다. 프로필을 인스타그램 형태와 유사하도록 제작했습니다.

- AJAX 

  커뮤니티 리뷰 기능의 좋아요와 프로필의 팔로우 기능을 AJAX 요청으로 제작한 1일 실습 프로젝트입니다.



## Command



### 1. Django Framework Command

#### (1) pjt

- django-admin startproject pjt .(pjt와 manage.py 바로 생성)
- django-admin startproject pjt (pjt와 pjt/manage.py 생성)

#### (2) app

- python manage.py startapp appname : app 생성 

#### (3) server

- python manage.py runserver : 웹페이지 서버 연결

#### (4) app/migrations

- python manage.py makemigrations : migrations 폴더 아래 하위 파일 생성
- python manage.py migrate : 실행할 때마다 명령어
- python manage.py shell_plus : OOP 입력
- python manage.py seed articles --number=5 : articles의 앱에 5개의 가짜 데이터 생성

#### (5)  app/fixtures

- python manage.py dumpdata articles.article > articles.json : fixtures  폴더 아래 articles.json으로 articles.article 정보 생성
- python manage.py loaddata articles/articles.json : fixtures 폴더 아래 articles/articles.json db에 불러오기

#### (6) app/admin.py

- python manage.py createsuperuser : 관리자 계정 생성

#### (7) app/tests.py

- python manage.py test : 테스트 함수 실행

#### (8) pjt/settings.py

- pip install django : django 설치

- pip install django-extensions : django-extensions 설치 

  - settings.py

    - INSTALLED_APPS

      `'django_extensions',` 

- pip install Pillow : 이미지삽입 

  - models.py

    `models.ImageField(blank=True)` 

  - views.py

    `request.FILES` 

  - templates/html

    `{% load static %}`

    `<form>` `enctype="multipart/form-data"` 

    `<input>` ` accept="image/*"` 

- pip install django-bootstrap-v5 : 부트스트랩 설치 

  - settings.py

    - INSTALLED_APPS

      `'bootstrap5',` 

  - templates/html

    `{% load bootstrap5 %}`

- pip install django-allauth : 소셜 로그인 설치  

  - settings.py

    - INSTALLED_APPS

      `'django.contrib.sites',`

      `  'allauth',`

      `'allauth.account',`

      ` 'allauth.socialaccount',`

      ` 'allauth.socialaccount.providers.google',` 

    - `SITE_ID = 1`

  - urls.py (pjt/urls.py)

    `path('accounts/', include('allauth.urls')),` 

  - templates/html

    `{% load socialaccount %}` 

- pip install django-imagekit : 이미지 리사이즈 

  - settings.py

    - INSTALLED_APPS

      `'imagekit',` 

  - models.py

    - `models.ImageSpecField()` 

      CACHE/images/8k/ 썸네일 새롭게 폴더 생성 후 자동 저장 

      (db에서 확인 불가 원본을 그 순간 규격을 새롭게 보여주기)

    - `models.ProcessedImageField()` 

      media / image 새롭게 폴더 생성 후 자동 저장 

      (db에서 확인 가느) 

- pip install django-bootstrap-pagination : 페이지목록 부트스트랩   

  - settings.py

    - INSTALLED_APPS

      `'bootstrap_pagination',`

  - templates/html

    ` {% load bootstrap_pagination %}` 

    `{% bootstrap_paginate page_obj range=3 %}` 

- pip install django-cors-headers : cors-headers 생성 (django와 vuex)

  - settings.py

    - INSTALLED_APPS

      `'corsheaders',` 

    - `CORS_ALLOW_ALL_ORIGINS` 

      특정 Origin만 선택적으로 허용

      ```python
      # pjt/settings.py
      CORS_ALLOWED_ORIGINS = [
          "https://example.com",
          "https://sub.example.com",
          "http://localhost:8080",
          "http://127.0.0.1:9000"
      ]
      ```

      모든 Origin 허용

      ```python
      # pjt/settings.py
      CORS_ALLOW_ALL_ORIGINS = True
      ```

    - `MIDDLEWARE` 

      ```python
      # pjt/settings.py
      MIDDLEWARE = [
          'corsheaders.middleware.CorsMiddleware',
          'django.middleware.common.CommonMiddleware',
      ]
      ```

- pip install djangorestframework-jwt : 토큰베이스 아이디 로그인

  - urls.py (accounts/urls.py)

    - `from rest_framework_jwt.views import obtain_jwt_token`

    - urlpatterns

      `path('api-token-auth/', obtain_jwt_token),`

  - setting.py

    ```python
    # pjt/settings.py
    import datetime
    
    JWT_AUTH = {
        'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
        # seconds=300
        }
    ```

- pip install Faker django-extensions : DB 더미데이터 

  10개의 리뷰에 10개의 댓글은 Faker (python manage.py shell_plus)

- pip install django-seed : 가짜 데이터 생성 

  - settings.py

    - INSTALLED_APPS

      `'django_seed',`

- pip install djangorestframework : DRF 설치 

  - settings.py

    - INSTALLED_APPS

      `'rest_framework',` 

- pip install -U drf-yasg : Swagger

  - settings.py

    - INSTALLED_APPS

      `'drf_yasg',`

  - views.py

    `from drf_yasg.utils import swagger_auto_schema `

    `@swagger_auto_schema(methods=['POST'], request_body=ArticleSerializer)`

  - urls.py

    - `from rest_framework import permissions` 

    - `from drf_yasg.views import get_schema_view `

    - `from drf_yasg import openapi `

    - urlpatterns

      `path('swagger/', schema_view.with_ui('swagger')),`

    - schema_view 

      ```python
      # urls.py
      schema_view = get_schema_view(
         openapi.Info(
            title="Snippets API",
            default_version='v1',
         )
      )
      ```

- pip install django-debug-toolbar

  - settings.py

    - INSTALLED_APPS

      `'debug_toolbar',`  ( `'django.contrib.staticfiles',`보다 아래에 기입)

    - `MIDDLEWARE` 

      `'debug_toolbar.middleware.DebugToolbarMiddleware',`

    -  `INTERNAL_IPS`

      `'127.0.0.1',`

  - urls.py

    - `import debug_toolbar` 

    - urlpatterns

      `path('__debug__/', include(debug_toolbar.urls)),` 

- humanize

  - settings.py

    - INSTALLED_APPS

      `'django.contrib.humanize',`  

  - templates/html

    `{% load humanize %}` 



### 2. Venv Command

- 버젼 (requirements.txt)
  - pip freeze > requirements.txt : 버젼 저장
  - pip install -r requirements.txt : 버젼 조회 및 다운로드
- 가상환경 (venv)
  - python -m venv venv  :  가상환경 폴더 생성
  - source venv/Scripts/activate : 가상환경 실행
  - deactivate : 가상환경 해제
  - pip list : 가상환경 site-packages 설치된 목록 확인



### 3. VS Code 단축키

- Ctrl + [ or ] -> 들여쓰기, 내어쓰기
- Alt + <방향키> -> 해당 커서에 있는 행 내용을 위아래로 이동
- Ctrl + Alt + 위/아래 화살표 -> 위아래로 커서를 늘려서 동시에 여러줄 수정할 수 있도록 하는 기능
- CTRL + D 해당 단어 동시 수정
- ALT + CLICK  모두 한번에 잡아줘 수정하고싶은 부분들을 한번에 수정
- ALT + Shift + ↓or↑ 현재 커서가 있는 줄을 복사하여 아래에 붙여넣어준다

