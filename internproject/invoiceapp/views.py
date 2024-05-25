from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer,InvoiceDetailSerializer

# Create your views here.
class InvoiceList(APIView):
    def get(self, request):
        elist=Invoice.objects.all()
        serializer_obj=InvoiceSerializer(elist,many=True)
        return Response(serializer_obj.data)

# to store an object
    def post(self,request):
        sobj=InvoiceSerializer(data=request.data)
        if sobj.is_valid():
            sobj.save()
            return Response(sobj.data,status=status.HTTP_201_CREATED)
        else:
            return Response(sobj.errors, status=status.HTTP_400_BAD_REQUEST)
    def update(self,request):
        elist=Invoice.objects.all()
        serializer_obj=InvoiceSerializer(elist,many=True)
        return Response(serializer_obj.data)

        


class InvoiceModify(APIView):
    def get_object(self,id):
        try:
            return Invoice.objects.get(id=id)
        except Invoice.DoesNotExist:
            return Response({"error":"Invoice does not exist"},status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request,id):
        inv=self.get_object(id)
        sobj=InvoiceSerializer(inv)
        return Response(sobj.data)
    
    def put(self,request,id):
        inv=self.get_object(id)
        sobj=InvoiceSerializer(inv,data=request.data)
        if sobj.is_valid():
            sobj.save()
            return Response(sobj.data,status=status.HTTP_200_OK)
        else:
            return Response(sobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        inv=self.get_object(id)
        inv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class InvoiceDetailList(APIView):
    def get(self, request):
        elist1=InvoiceDetail.objects.all()
        serializer_obj=InvoiceDetailSerializer(elist1, many=True)
        return Response(serializer_obj.data)
    def post(self,request):
        sobj1=InvoiceDetailSerializer(data=request.data)
        if sobj1.is_valid():
            sobj1.save()
            return Response(sobj1.data,status=status.HTTP_201_CREATED)
        else:
            return Response(sobj1.errors, status=status.HTTP_400_BAD_REQUEST)
class InvoiceDetailModify(APIView):
    def get_object(self, id):
        try:
            return InvoiceDetail.objects.get(id=id)
        except InvoiceDetail.DoesNotExist:
            return Response({"error":"Invoice Detail does not exist"},status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        invdetail = self.get_object(id)
        sobj1 = InvoiceDetailSerializer(invdetail)
        return Response(sobj1.data)
    
    def put(self,request, id):
        invdetail = self.get_object(id)
        sobj1 = InvoiceDetailSerializer(invdetail,data=request.data)
        if sobj1.is_valid():
            sobj1.save()
            return Response(sobj1.data,status=status.HTTP_200_OK)
        else:
            return Response(sobj1.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        invdetail = self.get_object(id)
        invdetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)