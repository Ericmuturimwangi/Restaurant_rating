from typing import Any
from django.http import JsonResponse
from .models import APIKey

class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.headers.get("Authorization")
        if not api_key:
            return JsonResponse({"error": "API key missing"}, status=401)

        try:
            api_key_obj = APIKey.objects.get(key=api_key, is_active=True)
            request.user = api_key_obj.user
        except APIKey.DoesNotExist:
            return JsonResponse({"error":"Invalid API Key"}, status=403)

        response = self.get_response(request)
        return response
            