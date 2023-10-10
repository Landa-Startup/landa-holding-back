from django.urls import path
from .views import VacationCreateForm,VacationDeleteForm,VacationEditForm,VacationGetAllForm,VacationViewForm,VacationViewStaffForm,approve,decline
app_name = "panel"

urlpatterns = [
    path('get-vacation-forms',VacationGetAllForm.as_view(),name='get-vacation-forms'),
    path('my-vacation-form',VacationViewForm.as_view(),name='my-vacation-form'),
    path('edit-vacation-form/<int:pk>/',VacationEditForm.as_view(),name='edit-vacation-form'),
    path('staff-vacation-form',VacationViewStaffForm.as_view(),name='staff-vacation-form'),
    path('create-vacation-form',VacationCreateForm.as_view(),name='create-vacation-form'), 
    path('delete-vacation-form/<int:pk>',VacationDeleteForm.as_view(),name='delete-vacation-form'), 
    

    path('approve/<str:uuid_value>/',approve,name='approve'),
    path('decline/<str:uuid_value>/',decline,name='decline'),
]
