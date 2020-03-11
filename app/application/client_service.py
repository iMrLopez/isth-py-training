# Empty
"""Methods for altering the file tables"""
from app.infrastructure import client_repository


def get(cif):
    """Get a client"""
    print("client_service.get")
    return client_repository.get_client(cif)


def post(client):
    """Get a client"""
    print("client_service.post")
    if client.age > 17:
        client.isAdult = True
    else:
        client.isAdult = False
    return client_repository.create_client(client)
