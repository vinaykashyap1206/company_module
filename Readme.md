# - Write an simple read-only API endpoint for companies to get the company name + street+postal_code+city from the headquarter office.

URL: https://company-module.herokuapp.com/companies/
Method: GET
Headers: Content-Type : application/json

# - Write an simple read-only API endpoint to get all the offices for a company

URL: https://company-module.herokuapp.com/companies/1
Method: GET
Headers: Content-Type : application/json


# - Write an API endpoint to change the headquarter of the company
URL: https://company-module.herokuapp.com/companies/1/update
Method: PATCH
Headers: Content-Type : application/json
Body: {"office_id" : 2}

# - Customize the API endpoint to include the sum of rent for all offices of a Company. How would you approach / test this?
- I have modifies the endpoint so that we can get the total rent of offices in response.



# Testing

Regarding to the Test the Objects and Rest apis, we can use following approaches:

1. Unit test cases: Here we will create model objects and pass it to serializers. By using this, we can check the logic of our code.

2. Integration test cases: In DRF, before starting test cases, It creates a test DB and delete it after executing all test cases. So, we can directly call the rest apis with values and perform end-to-end testing. 