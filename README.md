# Introduction
This is set of RESTful APIs with Django Rest Framework(DRF) for managing product catalog. The API provides:
- Creating, updating, listing and deleting products
- Searching for products
- Uploading product image
- Tests to check if the API are working correctly

# Installation and setup 
1. Clone the repository  <br/>
`git clone https://github.com/sonaljain067/CatalogManager.git`

2. Create a virtual environment  <br/>
`cd CatalogMaster` <br/>
`python3 -m venv env`   or  `virtualenv env`  <br/>
to create virtual environment named env

3. Activate the virtual environment  <br/>
In Ubuntu: `source env/Scripts/activate`  <br/>
In Windows: `.\env\Scripts\activate`

4. Install dependencies  <br/>
`pip install -r requirements.txt`

5. Setup database  <br/>
`python manage.py migrate` or `python3 manage.py migrate`

6. Create a superuser  <br/>
`python manage.py createsuperuser` or `python3 manage.py createsuperuser`
6. Run the server  <br/>
`python manage.py runserver` or `python3 manage.py runserver`


# API Endpoints
`GET /api/product/` - Retrives all products  <br/>
`POST /api/product/create` - Create a new product  <br/>
`PUT /api//product/<id>` - Update an existing product  <br/>
`DELETE /api/product/<id>` - Delete an existing product  <br/>

# Test Cases
1. Test that API returns a list of products when no search is provided.
2. Test that API returns a list of products when search is provided
3. Test that API return a empty list when search is not 
4. Test that API create a product with only valid payload
5. Test that API doesn't create product with invalid payload
6. Test that API update a product with only valid payload
7. Test that API doesn't create product with invalid payload
6. Test that API delete a existing product 


# Running Tests 
To test the test suite, run the command:  <br/>
`python manage.py test` or `python3 manage.py test` <br/>
This will run all the tests in tests.py file