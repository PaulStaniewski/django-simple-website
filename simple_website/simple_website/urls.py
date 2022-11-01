from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from website import views

from website.views import (  # import views
    index,
    gallery_retrieve,
    gallery_create,
    gallery_update,
    gallery_delete,
    about,
    contact,
    gallery,
    degree,
    news,
    faq,
)

urlpatterns = [  # url patterns
    path("admin/", admin.site.urls),  # admin
    path("galleries/", gallery),  # gallery
    path("about/", about),  # about
    path("galleries/<pk>/", gallery_retrieve),  # retrieve gallery
    path("galleries/<pk>/edit/", gallery_update),  # update gallery
    path("galleries/<pk>/delete/", gallery_delete),  # delete gallery
    path("add-listing/", gallery_create),  # create gallery
    path("contact/", contact),  # contact
    path('360degree/', degree, name='360degree'),  # 360degree
    path('360degree/<int:image_id>', views.details, name='details'),  # 360degree details
    path('news/', news),  # news
    path('faq/', faq),  # faq
    path('index/', views.PostList.as_view(), name='home'),  # index
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),  # post detail
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # static


