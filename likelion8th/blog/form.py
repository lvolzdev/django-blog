from django import forms
from .models import Blog

class BlogForm(forms.ModelForm): #model 기반으로 받아올거라 ModelForm
    class Meta:
        model = Blog
        fields = ['title', 'body', 'image'] #원하는 값 (여기에 안 쓴 값(pub_data)들은 view에서 처리)

        

