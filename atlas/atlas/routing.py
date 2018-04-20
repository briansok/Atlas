from channels.routing import ProtocolTypeRouter, ChannelNameRouter
from .consumers import NotificationConsumer

application = ProtocolTypeRouter({
    "channel": ChannelNameRouter({
        "notifications": NotificationConsumer,
    }),
})
