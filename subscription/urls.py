from rest_framework import routers

from subscription.views import ArtistSubscriptionViewSet, ChannelSubscriptionViewSet


app_name = "subscription"

router = routers.DefaultRouter()

router.register(
    "artist-subscription", ArtistSubscriptionViewSet, basename="artist-subscription"
)
router.register(
    "channel-subscription", ChannelSubscriptionViewSet, basename="channel-subscription"
)

urlpatterns = router.urls
