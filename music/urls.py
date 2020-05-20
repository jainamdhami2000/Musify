from django.urls import path, include
from .views import *

app_name = 'music'

urlpatterns = [
    path('', MusicList.as_view(), name = 'music_list'),
    path('year/<int:year>', MusicYear.as_view(), name = 'music_year'),
    path('search/', MusicSearch.as_view(), name = 'music_search'),
    path('language/<str:lang>', MusicLanguage.as_view(), name = 'music_language'),
    path('category/<str:category>', MusicCateory.as_view(), name = 'music_category'),
    path('<slug:slug>', MusicDetail.as_view(), name = 'music_detail'),
]
