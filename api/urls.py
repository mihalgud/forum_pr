from django.urls import path, include
from rest_framework import routers
from api.views import CheckboxViewSet
from api import views

router=routers.DefaultRouter()
router.register('checkbox', CheckboxViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('checkbox_list', views.checkbox_list, name='checkbox_list'),
    # path('checkbox_list/<int:pk>', views.checkbox_detail, name='checkbox_detail'),
    # path('checkbox_create', views.checkbox_create, name='checkbox_create'),
    # path('checkbox_update/<int:pk>', views.checkbox_update, name='checkbox_update'),
    # path('checkbox_delete/<int:pk>', views.checkbox_delete, name='checkbox_delete'),
    # path('checkbox_detailed/<int:pk>', views.CheckboxDetailed.as_view()),
    # path('checkbox_list', views.CheckboxViewSet.as_view()),
    path('data', views.DateView.as_view()),
]