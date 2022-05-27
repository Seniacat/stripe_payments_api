from django.urls import path

from .views import (CreateSessionCheckoutView, ItemDetailsView,
                    SuccessView, CancelView)


urlpatterns = [
    path('item/<int:pk>/', ItemDetailsView.as_view(), name='item_details'),
    path(
        'buy/<int:pk>/',
        CreateSessionCheckoutView.as_view(),
        name='buy_item'
    ),
    path('success/', SuccessView.as_view()),
    path('cancel/', CancelView.as_view())
]
