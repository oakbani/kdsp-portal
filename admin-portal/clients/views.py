from django.shortcuts import render
from django.http import JsonResponse
from .models import Client


def get_all_clients(request):
    if request.method == "GET":
        clients = Client.objects.filter()
        clients_list = []
        for client in clients:
            clients_list.append({"id": client.id, "name": client.name})
        return JsonResponse(clients_list, safe=False)
