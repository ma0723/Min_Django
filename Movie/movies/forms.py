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