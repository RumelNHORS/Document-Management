from django.urls import path
from documents import views

urlpatterns = [
    # Endpoint for user signup
    path('signup/', views.UserSignup.as_view(), name='user-signup'),
    # Endpoint for user login
    path('login/', views.UserLogin.as_view(), name='user-login'),
    # Endpoint for listing and creating documents
    path('documents/', views.DocumentList.as_view(), name='document_list'),
    # Endpoint for retrieving, updating, and deleting documents
    path('documents/<int:pk>/', views.DocumentDetail.as_view(), name='document_detail'),
    # Endpoint for updating document shares
    path('documents/<int:pk>/share/', views.DocumentShareUpdate.as_view(), name='document_share_update'),
]
