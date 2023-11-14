import asyncio
from time import sleep
import httpx
from django.http import HttpResponse

async def http_call_async():
    for num in range(1,5):
        await asyncio.sleep(1)
        print(num)
        if num == 4:
            print("A requisição Async Funcionou 100%")
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('Non-blocking HTTP request')        





# def api(request):
#     time.sleep(1)
#     payload = {"message": "Hello World Mateus"}

#     if "task_id" in request.GET:
#         payload["task_id"] = request.GET["task_id"]
#     return JsonResponse(payload)