from .client_events import *
from .server_events import *


ws_event_mapping = {
    "connect": {"handler": client_connected, "namespace": None},
    "disconnect": {"handler": client_disconnected, "namespace": None},
}


