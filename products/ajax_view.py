from django.http import JsonResponse
from django.views import View
from .models import Order


class AjaxPayment(View):

    def get(self, request):
        id = request.GET.get('id', None)
        reference_id = request.GET.get('reference', None)
        order_detail = Order.objects.get(id=id)
        data = {}

        order_detail.reference_id = reference_id
        order_detail.paid = True
        order_detail.save()

        if order_detail.paid:
            data['message'] = "Your Payment was successfully received"
        else:
            data['message'] = "Your Payment Failed!!!"
        return JsonResponse(data)


class SaveBilling(View):
    def get(self, request):
        first_name = request.GET.get('first_name', None)
        last_name = request.GET.get('last_name', None)
        email = request.GET.get('email', None)
        phone_number = request.GET.get('phone_number', None)
        address = request.GET.get('address', None)
        city = request.GET.get('city', None)

        order = Order.objects.create(first_name=first_name, last_name=last_name, email=email, address=address, city=city, phone_number=phone_number)
        data = {
            'first_name ': order.first_name,
            'last_name ': order.last_name,
            'email ': order.email,
            'address ': order.address,
            'city ': order.city,
            'phone_number ': order.phone_number,
            'created ': order.created,
            'updated ': order.updated,
            'status': 'Billing Detail Saved Successfully'
        }
        return JsonResponse(data)



