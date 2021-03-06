from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_leave.as_view(), name="create_leave"), # done
    path('list/', views.leave_list.as_view(), name="create_list"), # done
    path('<int:pk>/approval/', views.application_approval.as_view(), name="application_approval"), # done
    path('<slug:leave_type>/list/', views.leave_types.as_view(), name="leave_applications"), # done
    path('<str:employee_id>/records/', views.employee_records.as_view(), name="employee leave records"), # done
    path('<str:employee_id>/details/', views.employee_leave_details.as_view(), name="employee leave details"),
    path('<str:employee_id>/apply/<slug:leave_type>/', views.leave_application.as_view(), name="employee leave records") # done

]