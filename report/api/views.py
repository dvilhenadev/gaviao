from rest_framework import generics, mixins
from report.models import Report
from .serializers import ReportSerializer
from django.db.models import Q



class ReportAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field= 'pk'
    serializer_class = ReportSerializer

    def get_queryset(self):

        qs = Report.objects.all();
        #query = self.request.GET.get("q")
        
        #if query is not None:
        #    qs = qs.filter(Q(author__icontains=query)).distinct()

        author_query = self.request.query_params.get('a', None)
        if author_query is not None:
            qs = qs.filter(author__icontains=author_query).distinct()

        category_query = self.request.query_params.get('c', None)
        if category_query is not None:
            qs = qs.filter(category__icontains=category_query).distinct()

        location_query = self.request.query_params.get('l', None)
        if location_query is not None:
            qs = qs.filter(location__icontains=location_query).distinct()  

        # TODO Location query      
        
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}

# RetrieveUpdateDelete View
# This is a detail view
class ReportRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field= 'pk'
    serializer_class = ReportSerializer

    def get_queryset(self):
        return Report.objects.all();

    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}