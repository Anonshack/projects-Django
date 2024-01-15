# from django.urls import path
# from .views import (
#     ViloyatList,
#     TumanList,
#     StansiyaList,
#     OsimlikList,
#     HashorotList,
#     DataHashorotList
# )
#
# urlpatterns = [
#     path('viloyat/', ViloyatList.as_view(), name='viloyat-list'),
#     path('tuman/', TumanList.as_view(), name='tuman-list'),
#     path('stansiya/', StansiyaList.as_view(), name='stansiya-list'),
#     path('osimlik/', OsimlikList.as_view(), name='osimlik-list'),
#     path('hashorot/', HashorotList.as_view(), name='hashorot-list'),
#     path('datahashorot/', DataHashorotList.as_view(), name='datahashorot-list'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViloyatViewSet, TumanViewSet, StansiyaViewSet, OsimlikViewSet, HashorotViewSet, DataHashorotViewSet

router = DefaultRouter()
router.register(r'viloyat', ViloyatViewSet)
router.register(r'tuman', TumanViewSet)
router.register(r'stansiya', StansiyaViewSet)
router.register(r'osimlik', OsimlikViewSet)
router.register(r'hashorot', HashorotViewSet)
router.register(r'datahashorot', DataHashorotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
