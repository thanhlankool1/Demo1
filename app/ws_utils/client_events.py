from app.ws import sio

# -*- coding: utf-8 -*-
async def client_connected(sid, *args, **kwargs):
    print(f'--> ws get event=client_connected {sid=} ')
    await sio.emit('Wellcome', to=sid)


async def client_disconnected(sid,*args, **kwargs):
    print(f'--> ws get event=client_disconnected {sid=} ')