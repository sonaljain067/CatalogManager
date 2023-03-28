from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APITestCase
from .models import *
from .serializers import * 
from .views import *
from django.contrib.auth.models import User 
import os
from catalog import settings
from django.core.files.uploadedfile import SimpleUploadedFile


class ProductListAPIViewTestCase(APITestCase):
    url = reverse('product_list_view')
    def setUp(self):
        self.user = User.objects.create_user(
            username = 'test-username', email = 'test-email@gmail.com', password = 'test-password'
        )
        self.client.login(username = 'test-username', password = 'test-password')
        
        self.product1 = Product.objects.create(name = 'Product1',category = 'Category1', brand_name = 'Brand1', image = 'product_images/product1.jpeg')
        self.product2 = Product.objects.create(name = 'Product2',category = 'Category2', brand_name = 'Brand2', image = 'product_images/product2.jpeg')
        self.product3 = Product.objects.create(name = 'Product3',category = 'Category3', brand_name = 'Brand3', image = 'product_images/product3.jpeg')
        self.product4 = Product.objects.create(name = 'Product4',category = 'Category4', brand_name = 'Brand4', image = 'product_images/product4.jpeg')
        
    def test_product_list_view(self):
        response = self.client.get(self.url, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = ProductSerializer([self.product1, self.product2, self.product3, self.product4],many = True).data
        self.assertEqual(response.data, serialized_data)

    def test_product_list_view_with_search_params(self):
        response = self.client.get(self.url + '?search=1', format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = ProductSerializer([self.product1],many=True).data
        self.assertEqual(response.data, serialized_data)
    
    def test_product_list_view_with_search_params_not_found(self):
        response = self.client.get(self.url + '?search=158957', format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = ProductSerializer([self.product1],many=True).data
        self.assertEqual(response.data, [])


class ProductCreateAPIViewTestCase(APITestCase): 
    def setUp(self):
        self.url = reverse('product_create_view') 
        self.image_path = SimpleUploadedFile(
            name = 'product10.jpeg',
            content = open('product_images/product10.jpeg', 'rb').read(),
            content_type = 'image/jpeg'
        )
        self.valid_payload = {
            'name': 'Product11',
            'category': 'Category11',
            'brand_name': 'Brand11',
            'image': [self.image_path]
        }
        self.invalid_payload = {
            'name': '',
            'category': '',
            'brand_name': '',
            'image': [self.image_path]
        }

    def test_create_product(self):
        response = self.client.post(self.url, data = {
            'name': 'Product10',
            'category': 'Category10',
            'brand_name': 'Brand10', 
            'image': [self.image_path]
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        product = Product.objects.get(name = 'Product10')
        self.assertIsNotNone(product)

        serializer = ProductSerializer(product)
        self.assertEqual(response.data, serializer.data)

    def test_create_valid_payload(self):
        response = self.client.post(self.url, data = self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_payload(self):
        response = self.client.post(self.url, data = self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class ProductUpdateAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username = 'test-username', email = 'test-email@gmail.com', password = 'test-password'
        )
        self.client.login(username = 'test-username', password = 'test-password')

        self.product = Product.objects.create(
            name = 'Product3',
            category = 'Category3', 
            brand_name = 'Brand3', 
            image = 'product_images/product1.jpeg'
        )
    
        self.valid_payload = {
            'name': 'Updated Product3',
            'category': 'Updated Category3',
            'brand_name': 'Updated Brand3'
        }
        self.invalid_payload = {
            'name': '',
            'category': '',
            'brand_name': ''
        }

    def test_update_valid_product(self):
        url = reverse('product_update_view', kwargs = {'id': self.product.id}) 
        response = self.client.patch(url, data = self.valid_payload)
        product = Product.objects.get(id=self.product.id)
        serializer = ProductSerializer(product)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_invalid_product(self):
        url = reverse('product_update_view', kwargs = {'id': self.product.id}) 
        response = self.client.put(url, data = self.invalid_payload, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ProductDestroyAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username = 'test-username', email = 'test-email@gmail.com', password = 'test-password'
        )
        self.client.login(username = 'test-username', password = 'test-password')

        self.product = Product.objects.create(
            name = 'product',
            category = 'category',
            brand_name = 'brand',
            image = SimpleUploadedFile('product1.jpeg', b'image data', content_type = 'image/jpeg')
        )

        self.url = reverse('product_delete_view', kwargs = {'id': self.product.id})
    
    def test_delete_product(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)