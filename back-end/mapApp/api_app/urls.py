from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'incidents', views.IncidentsViewSet)

router.register(r'comments', views.CommentCreateView)
router.register(r'viewcomments', views.CommentGetView)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("incident/<int:pk>/", views.IncidentDetailView),
    path("comments/view/", views.CommentGetView),


]