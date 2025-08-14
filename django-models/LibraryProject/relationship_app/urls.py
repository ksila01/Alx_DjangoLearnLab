from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path("register/", views.register, name="register"),  # Register view
]

urlpatterns = [
    path("books/", views.list_books, name="list_books"),  # Function-based view
    path(
        "library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"
    ),  # Class-based view
]


from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),  # Function-based view
    path(
        "library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"
    ),  # Class-based view
    path("login/", views.user_login, name="login"),  # Login URL
    path("logout/", views.user_logout, name="logout"),  # Logout URL
    path("register/", views.user_register, name="register"),  # Register URL
]

from django.urls import path
from . import views

urlpatterns = [
    path("admin/", views.admin_view, name="admin_view"),
    path("librarian/", views.librarian_view, name="librarian_view"),
    path("member/", views.member_view, name="member_view"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),  # Existing books list view
    path("book/add/", views.add_book, name="add_book"),  # Add book view (secured)
    path(
        "book/edit/<int:book_id>/", views.edit_book, name="edit_book"
    ),  # Edit book view (secured)
    path(
        "book/delete/<int:book_id>/", views.delete_book, name="delete_book"
    ),  # Delete book view (secured)
]
