from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('user', views.UserView.as_view(), name = 'user'),
    path('update', views.UserView.as_view(), name = 'update_user'),
    path('create', views.UserView.as_view(), name = 'create_user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('conditions', views.ConditionListView.as_view(), name='conditions'),
    path('conditionsmixin', views.ConditionViewMixin.as_view(), name='conditionsmixin'),
    path('create_condition', views.ConditionView.as_view(), name='create_condition'),
    path('edit_condition/<int:id>', views.ConditionView.as_view(), name='update_condition'),
    path('condition_retrieve/<int:pk>', views.ConditionRetrieveView.as_view(), name='condition_retrieve'),
    path('condition_retrieve_destroy/<int:pk>', views.ConditionRetrieveDestroyView.as_view(), name='condition_retrieve_destroy'),
    path('edit_retrieve_condition/<int:pk>', views.ConditionRetrieveUpdate.as_view(), name='update_retrieve_condition'),


]