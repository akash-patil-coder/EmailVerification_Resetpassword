from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopModelForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

class AddLaptopView(LoginRequiredMixin,View):

    def get(self,request):
        form = LaptopModelForm()
        context = {'form': form}
        template_name = 'FirstApp/addLaptop.html'
        return render(request, template_name, context)

    def post(self,request):
        print(request.POST)
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
        context = {'form': form}
        template_name = 'FirstApp/addLaptop.html'
        return render(request, template_name, context)


class showlaptopView(View):
    def get(self,request):
        lap_object = Laptop.objects.all()
        template_name = 'FirstApp/showLaptop.html'
        context = {'lap_object':lap_object}
        return render(request,template_name,context)


class updateView(LoginRequiredMixin,View):

    def get(self,request,id):
        lap_object = Laptop.objects.get(lid=id)
        form = LaptopModelForm(instance=lap_object)
        template_name = 'FirstApp/addLaptop.html'
        context = {'form': form}
        return render(request, template_name, context)

    def post(self,request,id):
        lap_object = Laptop.objects.get(lid=id)
        form = LaptopModelForm(request.POST,instance=lap_object)
        if form.is_valid():
            form.save()
            return redirect('show')


class DeleteView(LoginRequiredMixin,View):

    def get(self, request, id):
        lap_objects = Laptop.objects.get(lid=id)
        context = {'lap_objects': lap_objects}
        template_name = 'FirstApp/deletelaptop.html'
        return render(request, template_name, context)

    def post(self, request, id):
        lap_objects = Laptop.objects.get(lid=id)
        if request.method == 'POST':
            lap_objects.delete()
            return redirect('show')


