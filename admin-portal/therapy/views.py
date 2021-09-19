from django.shortcuts import render
from django.http import JsonResponse
from .models import Therapist, TherapySlot
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json


def get_all_therapists(request):
    if request.method == "GET":
        therapists = Therapist.objects.filter()
        therapists_list = []
        for therapist in therapists:
            therapists_list.append({"id": therapist.id, "name": therapist.name})
        return JsonResponse(therapists_list, safe=False)


def get_therapist_slot(request):
    if request.method == "GET":
        therapist_id = request.GET["id"]
        slots = []
        therapistSlots = TherapySlot.objects.filter(therapist=therapist_id).all()
        for therapistSlot in therapistSlots:
            slots.append(
                {
                    "id": therapistSlot.id,
                    "title": therapistSlot.title,
                    "status": therapistSlot.status,
                    "client_id": therapistSlot.client.id
                    if therapistSlot.client
                    else None,
                    "start_time": therapistSlot.start_time,
                    "end_time": therapistSlot.end_time,
                    "date": therapistSlot.date,
                    "type": therapistSlot.therapy_type,
                }
            )

        return JsonResponse({"slots": slots})


@csrf_exempt
def add_therapist_slot(request):
    if request.method == "POST":
        slot_data = json.loads(request.body)

        TherapySlot.objects.create(
            title=slot_data["title"],
            date=slot_data["date"],
            start_time=slot_data["start_time"],
            end_time=slot_data["end_time"],
            therapist_id=slot_data["therapist_id"],
            therapy_type=slot_data["type"],
            client_id=slot_data["client_id"],
            status=slot_data["status"],
        )

        return JsonResponse({"status": "done"})


@csrf_exempt
def update_therapist_slot(request):
    if request.method == "POST":
        slot_data = json.loads(request.body)

        TherapySlot.objects.filter(pk=slot_data["id"]).update(
            title=slot_data["title"],
            date=slot_data["date"],
            start_time=slot_data["start_time"],
            end_time=slot_data["end_time"],
            therapist_id=slot_data["therapist_id"],
            therapy_type=slot_data["type"],
            client_id=slot_data["client_id"],
            status=slot_data["status"],
        )

        return JsonResponse({"status": "done"})


@csrf_exempt
def delete_therapist_slot(request):
    if request.method == "POST":
        slot_data = json.loads(request.body)

        TherapySlot.objects.filter(id=slot_data["id"]).delete()
        return JsonResponse({"status": "done"})
