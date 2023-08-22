from . import views
from django.urls import path

#import firstapp

app_name='maintool'

urlpatterns = [
    # old old
    # # #/firstapp/
    # # path('',views.index,name="index"),
    # # #/firstapp/<album_id>/
    # # path('<int:album_id>/',views.detail,name="detail"),
    # # #/firstapp/<album_id>/favorite
    # # path('<int:album_id>/favorite/',views.favorite,name="favorite"),
    
    #/maintool/
    path('',views.index,name="index"),
    path('input/', views.take_input, name="take_input"),
    path('NoBook/', views.NoBook, name="noBook"),
    # #/firstapp/<album_id>/
    # path('<pk>/',views.DetailView.as_view(),name="detail"),
    # #firstapp/album/add
    # path('album/add/',views.AlbumCreate.as_view(),name="album-add"),
    # #firstapp/album/<pk>
    # path('album/<pk>',views.AlbumUpdate.as_view(),name="album-update"),
    # #firstapp/album/<pk>/delete
    # path('album/<pk>/delete',views.AlbumDelete.as_view(),name="album-delete"),
]