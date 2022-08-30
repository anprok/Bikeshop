from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import redirect
from .models import Bike, Basket, Seat, Tire, Frame, Order


class BikeListView(ListView):
    model = Bike


class BikeDetailView(DetailView):
    model = Bike

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query_set = self.get_queryset()
        bike = self.get_object()
        baskets = Basket.objects.filter(quantity__gt=0)
        show_form = False
        if (context['object'].has_basket == True and len(baskets) > 0) or context['object'].has_basket == False:
            query_results = query_set.filter(
                frame__quantity__gt=0
            ).filter(
                tire__quantity__gt=1
            ).filter(
                seat__quantity__gt=0
            ).filter(
                pk=bike.pk
            )
            if len(query_results) > 0:
                show_form = True

        context['show_form'] = show_form
        return context

    def post(self, request, pk):
        # Getting all the stuff from database
        # query_results = Bike.objects.all()
        bike = self.get_object()
        seat = Seat.objects.get(id=bike.seat.pk)
        seat.quantity -= 1
        seat.save()
        tire = Tire.objects.get(id=bike.tire.pk)
        tire.quantity -= 2
        tire.save()
        frame = Frame.objects.get(id=bike.frame.pk)
        frame.quantity -= 1
        frame.save()
        if bike.has_basket is True:
            basket = Basket.objects.first()
            basket.quantity -= 1
            basket.save()

        name = request.POST['name']
        surname = request.POST['surname']
        phone = request.POST['phone_number']
        order = Order(bike=bike, name=name, surname=surname, phone_number=phone)
        order.save()

        return redirect(f'/order/{order.pk}')


class OrderDetailView(DetailView):
    model = Order
