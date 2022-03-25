from django.urls import path

#from .views import UserList, CardList, DeckList, DeckDetail, GameList
#CardList.as_view()

from .views import cardView

urlpatterns = [
    path('cards/', cardView),
]