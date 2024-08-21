from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class GroupSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    
    def get_users(self, obj):
        users = obj.user_set.all()
        return UserSerializer(users, many=True).data
    
    class Meta:
        model = Group
        fields = ['id', 'name', 'users']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'