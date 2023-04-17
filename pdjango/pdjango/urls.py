from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from boards import views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('boards/<int:pk>/', views.board_topics, name='board_topics'),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
