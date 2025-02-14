from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page
from .tasks import sendEmail
import time
import requests


def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending<h1>")


@cache_page(60 * 10)  # کش کردن خروجی این ویو به مدت ۱۰ دقیقه
def test(request):
    try:
        time.sleep(5)  # تأخیر ۵ ثانیه‌ای برای تست
        response = requests.get("http://localhost:8000/blog/api/v1/post/")

        if response.status_code == 200:
            return JsonResponse(response.json())  # داده رو برمی‌گردونه و کش می‌شه
        else:
            return JsonResponse({"error": "Failed to fetch data"}, status=500)

    except requests.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)
