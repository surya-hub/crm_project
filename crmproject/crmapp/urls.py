from django.urls import path
from crmapp import views
urlpatterns = [
    path('',views.home,name='home'),

    path('home',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('orders/',views.orders,name='orders'),

    path('customer<pk>/',views.customer,name='customer'),
    path('all_customers/',views.all_customers,name='all_customers'),

    path('add_product/',views.add_product,name='add_product'),
    path('update_product/<pk>',views.update_product,name='update_product'),
    path('delete_product/<pk>',views.delete_product, name ='delete_product'),

    path('update_order/<pk>',views.update_order,name='update_order'),

    path('register',views.register_view, name='register'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),

    path('user_page',views.user_page,name='user_page')

]
