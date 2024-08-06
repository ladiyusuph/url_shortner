from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, redirect
from .models import UrlShortner
from .serializers import UrlSerializer


class UrlView(GenericAPIView):
    serializer_class = UrlSerializer
    queryset = UrlShortner.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "Long URL": serializer.data["url"],
                    "Shortened URL": f"https://127.0.0.1:8000/{serializer.data["slug"]}",
                }
            )
        return Response(serializer.errors, status=400)


@api_view(["GET"])
def redirect_to_url(self, slug):
    link = get_object_or_404(UrlShortner, slug=slug)
    url = link.url
    return redirect(url)
