from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from .models import Position
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from .models import Position

@csrf_exempt
def recevoir_position(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            latitude = data.get("latitude")
            longitude = data.get("longitude")
            accuracy = data.get("accuracy")
            timestamp = data.get("timestamp")

            # Validation des données
            if not all([latitude, longitude, accuracy, timestamp]):
                return JsonResponse({"status": "error", "message": "Champs requis manquants"})

            # Conversion du timestamp
            try:
                timestamp = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            except ValueError:
                return JsonResponse({"status": "error", "message": "Format de timestamp invalide"})

            # Enregistrement dans la base
            position = Position.objects.create(
                latitude=float(latitude),
                longitude=float(longitude),
                accuracy=float(accuracy),
                timestamp=timestamp
            )
            return JsonResponse({"status": "ok", "id": position.id})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    return JsonResponse({"message": "Seule la méthode POST est autorisée"})

def home(request):
    return render(request, 'index.html')