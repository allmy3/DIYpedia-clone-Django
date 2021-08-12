from django.http import Http404

class CheckAuthorMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.author:
            raise Http404()
        return super().dispatch(request, *args, **kwargs)