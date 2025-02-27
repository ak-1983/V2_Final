# Import necessary modules
from django.contrib import admin  # Django admin module
from django.urls import path       # URL routing
from .views import *  # Import views from the authentication app
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving
from django.conf.urls.static import static  # Import static function

# Define URL patterns
urlpatterns = [
    path('', home),
    path('AdminHome/', AdminDashboard, name="recipes"),      # Home page
    path('login/', login_page, name='login'),    # Login page
    path('register/', register_page, name='register'),  # Registration page
    path('logout/', logout_user, name='logout'),  # Logout page
    path('docs/', evaluationList),
    path('uploadCSV/', uploadCSV),  # Django admin page
    path('uploadcsv/', uploadFile),
    path('change_role/', change_role),  # Django admin page
    path('questionNumbers/', questionNumbers),
    path('changePassword/', changePassword),
    path('forgetPassword/', forgetPassword),
    path('TAHome/', TAHome),
    path('TeacherHome/', TeacherHome),
    path('StudentHome/', studentHome),
    path('DeleteDocs/', deleteDocs),
    path('studentEval/<str:doc_id>/<str:eval_id>/', studentEval, name='studentEval'),
    path('send_email/', send_reminder_mail, name='send_reminder_mail'),
    path('raiseTicket/<int:doc_id>', raise_ticket, name='peerEval'),
    path('doc/<str:file_name>', fetch_document, name='fetch_document'),
    path('export-evaluations/', export_evaluations_to_csv, name='export_evaluations'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve media files if DEBUG is True (development mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
