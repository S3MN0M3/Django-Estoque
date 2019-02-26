""" 1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import bebida_novo

urlpatterns = [
    path('', bebida_novo, name='core_lista_bebidas'),
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
]
