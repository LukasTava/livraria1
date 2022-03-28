from django.contrib import admin
from .models import Livro
from .models import Editora


admin.site.register(Editora)
admin.site.register(Livro)
