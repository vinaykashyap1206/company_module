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