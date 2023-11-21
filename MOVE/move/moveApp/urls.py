from django.urls import path
from . import views

urlpatterns = [
    path('api/clients/', views.get_liste_clients, name='clients-list'),
    path('api/clients/ordered/', views.get_clients_ordre_par_nom, name='clients-ordered'),
    path('api/grandLivres/', views.get_liste_GL, name='GL-list'),
    path('api/operations/', views.get_liste_operations, name='operations-list'),
    path('api/comptes/', views.get_liste_comptes, name='accounts-list'),
    path('api/mouvements/<int:num_transaction>/', views.get_mouvements_par_numero_transaction, name='movements-by-transaction'),
    path('api/transactions/', views.get_transactions_avec_filtre, name='filtered-transactions'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
