INSTALLED_APPS = [
    ...
    'main',
    'django.contrib.sites', 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
import environ

env = environ.Env()
environ.Env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}
from django.core.files.storage import FileSystemStorage

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        # Process the file (e.g., save to database)
    return render(request, 'upload.html')
from django import forms

class QueryForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    city = forms.CharField(max_length=100, required=False)

from .models import YourModel
from .forms import QueryForm

def query_builder(request):
    form = QueryForm(request.GET or None)
    results = None
    if form.is_valid():
        results = YourModel.objects.filter(**form.cleaned_data)
    return render(request, 'query_builder.html', {'form': form, 'results': results})


