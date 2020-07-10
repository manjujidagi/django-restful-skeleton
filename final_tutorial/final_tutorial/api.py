from rest_framework import routers

from rental import views as rental_views

router = routers.DefaultRouter()
router.register(r'friends', rental_views.FriendViewset)
router.register(r'belongings', rental_views.BelongingViewset)
router.register(r'borrowings', rental_views.BorrowedViewset)