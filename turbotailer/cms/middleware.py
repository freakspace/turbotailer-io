from django.http import HttpResponsePermanentRedirect


class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().partition(":")[0]
        if host.startswith("www."):
            new_host = host[4:]  # Remove "www."
            return HttpResponsePermanentRedirect("https://" + new_host + request.path)
        else:
            return self.get_response(request)
