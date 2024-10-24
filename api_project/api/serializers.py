from rest_framework import serializers
#from .models import Producto
from .models import Reservations
from .models import Clients
from .models import Rooms
from .models import Categories


#class ProductoSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Producto
        #fields = '__all__'

class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = '__all__'

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'