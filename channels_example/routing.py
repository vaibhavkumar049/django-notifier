from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import notifier.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket':AuthMiddlewareStack(
        URLRouter(
            notifier.routing.websocket_urlpatterns
        )
    ),
})