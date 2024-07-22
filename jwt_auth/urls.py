from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views
from django.urls import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()

router.register('studentapi',views.StudentModelViewSet,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_view'),
     path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
      path('verifytoken/',TokenVerifyView.as_view(),name='token_verify')
]
