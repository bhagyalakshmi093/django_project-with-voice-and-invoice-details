from django.contrib import admin
from django.urls import path
from invoiceapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/invoice',views.InvoiceList.as_view()),
    path('api/invoiceDetail',views.InvoiceDetailList.as_view()),
    path('api/invoice/<int:id>',views.InvoiceModify.as_view()),
    path('api/invoiceDetail/<int:id>',views.InvoiceDetailModify.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
