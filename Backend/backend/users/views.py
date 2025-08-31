from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from pymongo import MongoClient

# connect to MongoDB Atlas
client = MongoClient("mongodb+srv://prasanna:LAkky1221%40@cluster0.egu8ozv.mongodb.net")  # paste from MongoDB Atlas
db = client["login_db"]  # database name
collection = db["login_collection"]  # collection name

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            # check in MongoDB
            user = collection.find_one({"username": username, "password": password})

            if user:
                return JsonResponse({"message": "Login successful"}, status=200)
            else:
                return JsonResponse({"message": "Invalid credentials"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST allowed"}, status=405)
