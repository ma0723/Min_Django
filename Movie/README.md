# Project_Django_Movie

### 서울 3반 이민아 21.03.19



> driver : 서울 3반 정희진
>
> navigator : 서울 3반 이민아



---

## Index



- [Image](#image)
- [pjt05 (Project)](#pjt05)
- [movies (App)](#movies)
- [후기](#후기)



---

## Image

### 1. movies/index (READ)

![image-20210319160615664](README.assets/image-20210319160615664.png)

### 2. movies/detail (READ)

![image-20210319160706899](README.assets/image-20210319160706899.png)

### 3. movies/create (CREATE)

![image-20210319160805252](README.assets/image-20210319160805252.png)

### 4. movies/update (UPDATE)

### ![image-20210319160731769](README.assets/image-20210319160731769.png)

### 5. movies/delete (DELETE)

### 6. pjt05 (project)

![image-20210319160929095](README.assets/image-20210319160929095.png)

### 7. movies (app)

![image-20210319160958533](README.assets/image-20210319160958533.png)



---

## pjt05 



### 1. pjt05/urls.py

- static 
  - `from django.conf import settings
    from django.conf.urls.static import static`
  - ``+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)`

- [urls.py]

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```



### 2. pjt05/settings.py 

- `INSTALLED_APPS`  앱 등록

- `LANGUAGE_CODE` 언어 설정

- `TIME_ZONE` 시간 설정

- `TEMPLATES` templates DIRS 설정

- media

  - `MEDIA_ROOT` BASE_DIR media 설정

  - `MEDIA_URL`

- static

  - `STATIC_URL`
  - ``STATICFILES_DIRS` BASE_DIR static 설정

- [settings.py]

```python
INSTALLED_APPS = [
    'movies',
    'django_extensions',
    'bootstrap5',
    'imagekit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'pjt05' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'pjt05' / 'static',
]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
```



### 3. pjt05/templates/base.html

- CDN : `<link>` `<script>` / `{% load bootstrap5 %}` `{% bootstrap_css %}` `{% bootstrap_javascript %}`

- nav태그 : `<nav></nav>`

- a태그 : Movies(index) 혹은 New 버튼(create) 클릭시 url 이동

- css 상속 : `  {% block css %}{% endblock css %}`

- templates 상속

  - 다른 폴더 templates 상속 (div태그) 

    ` <div class="container"></div>` 

    `{% block content %}{% endblock content %}`

  - 동일 폴더 templates 상속 (include) 

    `{% include 'nav.html' %}` 

    `{% include 'footer.html' %}`

- [base.html]

```python
{% load bootstrap5 %}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% bootstrap_css %}
  {% block css %}
  {% endblock css %}
  <title>Document</title>
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="{% url 'movies:index' %}">Movies</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{% url 'movies:create' %}">NEW</a>
          </li>
        </ul>
      </div>
  </nav>

  <div class="container">
    {% block content %}
    {% endblock content %}
  </div>

  {% bootstrap_javascript %}

</body>
</html>
```



---

##  movies 



### 1. movies/urls.py

- [urls.py]

```python
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```



### 2. movies/fixtures/movies

- [movies.json]

```python
# python manage.py makemigrations
# python manage.py migrate
# python manage.py loaddata movies/movies.json
```



### 3. movies/models.py

- `def __str__(self):` : 제목을 용이하게 보기 위한 함수 추가

- [models.py]

```python
from django.db import models
# from imagekit.models import ImageSpecField
# from imagekit.processors import ResizeToFill
# from imagekit.models import ProcessedImageField
# img 규격화를 위한 import 

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    
# python manage.py makemigrations
# python manage.py migrate
```



### 4. movies/forms.py

- models.py

  `class Movie(models.Model):`

  - `from .models import Movie` 
  - `class MovieForm(forms.ModelForm):` `class Meta:`

- forms.py

  `forms.CharField()`

  - 라벨 : `label`

  - 너비 길이 등 속성 : `widget = forms.TextInput( attrs = {} )`

  - 에러메세지 : `error_messages={'required': '제목은 필수 항목입니다',},`

- [forms.py]

```python
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': 'Enter the Title',
                'maxlength': 100,
            }
        ),
        error_messages={
            'required': '제목은 필수 항목입니다',
        },
    )
    overview = forms.CharField(
        label='줄거리',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': 'Enter the Content',
                'rows': 5,
                'cols': 30,
            }
        ),
        error_messages={
            'required': '줄거리는 필수 항목입니다',
        },
    )
    poster_path = forms.CharField(
        label='포스터 경로',
        widget=forms.TextInput(
            attrs={
                'class': 'my-content form-control',
                'placeholder': 'Enter the Content',
                'maxlength': 500,
            }
        ),
        error_messages={
            'required': '포스터 경로는 필수 항목입니다',
        },
    )

    class Meta:
        model = Movie
        fields = '__all__'
```



### 5. movies/views.py 

- 오류, url 이동, html 이동 : `import render, redirect, get_object_or_404`

- view decorator : `from django.views.decorators.http import require_safe, require_http_methods, require_POST`

- models.py : `from .models import Movie`

- forms.py : `from .forms import MovieForm`

- [views.py]

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Movie
from .forms import MovieForm

@require_safe
# view decorator
def index(request):
# 전체 조회
    movies = Movie.objects.order_by('-pk')
    # 역순
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

@require_http_methods(['GET', 'POST'])
# view decorator list
def create(request):
    if request.method == 'POST':
    # create forms.py form태그 method POST
        form = MovieForm(request.POST, request.FILES)
        # instance 생성
        # form method request.POST
        # static files request.FILES
        if form.is_valid():
        # 유효성 검사
            movie = form.save()
            # 저장
            return redirect('movies:detail', movie.pk)
    else:
    # new index.html a태그 GET 방식
        form = MovieForm()
        # instance 생성
    context = {
        'form': form,
    }
    return render(request, 'movies/form.html', context)
	# form.html로 create.html과 update.html 통합

@require_safe
# view decorator
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    # import get_object_or_404
    # get_object_or_404(Model, pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)
    
@require_POST
# view decorator
def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    # import get_object_or_404
    # get_object_or_404(Model, pk=pk)
    movie.delete()
    return redirect('movies:index')

@require_http_methods(['GET', 'POST'])
# view decorator list
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    # import get_object_or_404
    # get_object_or_404(Model, pk=pk)
    if request.method == 'POST':
    # update forms.py form태그 method POST
        form = MovieForm(request.POST, request.FILES, instance=movie)
        # instance 호출 movie
        # form method request.POST
        # static files request.FILES
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
    # edit detail.html form태그 GET 방식(a태그도 가능)
        form = MovieForm(instance=movie)
        # instance 호출 movie
    context = {
        'form': form,
        'movie': movie,
        # pk를 가져오기 위해 추가 movie
    }
    return render(request, 'movies/form.html', context)
	# form.html로 create.html과 update.html 통합
```



### 6. movies/templates/movies

#### (1) index.html 

- a태그 GET - `new` (CREATE 이전) 
- div태그 READ

- [index.html]

```python
{% extends 'base.html' %}
{% load bootstrap5 %}
# 부트스트랩

{% block content %}

  <h1>INDEX</h1>

  <a href="{% url 'movies:create' %}" class="text-decoration-none">NEW</a>
  # GET 방식 NEW
    
  <div class="row row-cols-1 row-cols-md-3 g-4">
  
  {% for movie in movies %}
    <div class="col">
      <div class="card">
        <img src="{{ movie.poster_path }}" class="card-img-top" alt="{{ movie.title }}">
        # img 경로에서 이미지를 보여주기 위한 img태그
        <div class="card-body">
          <a href="{% url 'movies:detail' movie.pk %}" class="card-title">{{ movie.title }}</a>
          # title을 클릭하면 detail로 이동하는 a태그
        </div>
      </div>
    </div>
  {% endfor %}
      
  </div>
  
{% endblock content %}
```

#### (2) detail.html

- form태그 
  - GET - `edit`  (UPDATE 이전)
  - POST - `delete` DELETE

- [detail.html]

```python
{% extends 'base.html' %}
{% load bootstrap5 %}
# 부트스트랩

{% block content %}

  <h1>{{ movie.title }}</h1>
  <hr>
  <p>{{ movie.overview }}</p>
  <hr>
  <img src="{{ movie.poster_path }}" alt="영화 이미지">
  # img 경로에서 이미지를 보여주기 위한 img태그
  <hr>

  <form action="{% url 'movies:update' movie.pk %}">
    <button class="btn btn-warning">수정</button>
  </form>
  # GET 방식 EDIT
    
  <form action="{% url 'movies:delete' movie.pk %}" method="POST">
    {% csrf_token %}
    <button class="btn btn-danger">삭제</button>
  </form>
  # POST 방식 DELETE

  <a href="{% url 'movies:index' %}" class="text-decoration-none">BACK</a>

{% endblock content %}
```

#### (3) form.html

- form태그 
  - POST - `create` (new 이후)
  - POST - `update` (edit 이후)

- [form.html]

```python
{% extends 'base.html' %}
{% load bootstrap5 %}
# 부트스트랩

{% block content %}
  {% if request.resolver_match.url_name == 'create' %}
  # request.resolver_match의 정보 경로들 중 url_name이 create인 경우
    <div class = "fs-3 text-center bg-info p-3">create</div>
  {% else %}
  # request.resolver_match의 정보 경로들 중 url_name이 update인 경우
	<div class = "fs-3 text-center bg-warning p-3">update</div>
  {% endif %}

  <form action="" method="POST" enctype="multipart/form-data">
  # POST 방식 create update
    {% csrf_token %}
    {% bootstrap_form form layout='horizontal' %}
    <input class="btn btn-primary" type="submit">
  </form>

  <hr>
{% endblock content %}
```



### 7. movies/admin.py

- [admin.py]

```python
from django.contrib import admin
from .models import Movie
 
admin.site.register(Movie)
```



---

## 후기



지난번 첫 페어 프로젝트와 다르게 여성분과 페어하면서 편한 점이 존재했다. 더 섬세한 희진님의 관찰력에 감탄했고, 서로 오타가 없는지 검토하는 과정도 피드백이 잘 되어서 좋았다. 페어 프로젝트는 많은 분량의 코딩을 스스로 검토하기 어려울 때 피드백을 주고 즉석에서 토의하며 코딩을 작성한다는 점이 가장 큰 장점으로 느껴진다. 






