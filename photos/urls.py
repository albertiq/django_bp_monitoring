from django.urls import path
from .views import ArticleView
app_name = "photos"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('photos/', ArticleView.as_view()),
    ]
