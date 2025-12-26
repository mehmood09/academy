from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    # path('register/patient/', views.register_patient, name='register_patient'),
    # path('register/doctor/', views.register_doctor, name='register_doctor'),
    # path('dashboard/patient/', views.patient_dashboard, name='patient_dashboard'),
    # path('dashboard/doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    # path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    # path('profile/', views.profile_view, name='profile'),
    # path('profile/edit/', views.edit_profile, name='edit_profile'),
    # path('profile/change-password/', views.change_password, name='change_password'),
    
    # # Appointment URLs
    # path('appointments/book/', views.book_appointment, name='book_appointment'),
    # path('appointments/', views.appointment_list, name='appointment_list'),
    # path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    # path('appointments/<int:pk>/update-status/', views.update_appointment_status, name='update_appointment_status'),
    
    # # Medical Records URLs
    # path('medical-records/', views.medical_records_list, name='medical_records_list'),
    # path('medical-records/<int:pk>/', views.medical_record_detail, name='medical_record_detail'),
    # path('medical-records/create/<int:patient_id>/', views.create_medical_record, name='create_medical_record'),

    # # Payment Management URLs (Admin Only)
    # path('payments/', views.payment_management, name='payment_management'),
    # path('payments/collect/<int:pk>/', views.collect_payment, name='collect_payment'),
    # path('payments/receipt/<int:pk>/', views.payment_receipt, name='payment_receipt'),

    # # Doctor Management URLs (Admin Only)
    # path('doctors/toggle-status/<int:pk>/', views.toggle_doctor_status, name='toggle_doctor_status'),
]
