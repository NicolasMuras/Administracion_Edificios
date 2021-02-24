from apps.base.api import GeneralListAPIView
from apps.expensas.api.serializers.general_serializer import EdificioSerializer, DepartamentoSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from django.views.generic import View
from apps.expensas.utils import render_to_pdf
from apps.expensas.api.serializers.expensas_serializer import ExpensasSerializer
from django.template.loader import get_template


class EdificioSerializerListAPIVIew(GeneralListAPIView):
    serializer_class = EdificioSerializer
    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(status = True)


class DepartamentoSerializerListAPIView(GeneralListAPIView):
    serializer_class = DepartamentoSerializer
    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(status = True)


class GeneratePDF(View):

    serializer_class = ExpensasSerializer
    def get(self, request, pk = None):

        template = get_template('pdf/invoice.html')

        context = (self.serializer_class.Meta.model.objects.filter(status = True).values().filter(id = 7))[0]
        print(context)
        html = template.render(context)
        pdf = render_to_pdf('pdf/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")