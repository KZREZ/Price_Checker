# Price Checker
This is a platform for comparing prices of different commodities on the market to allow users buy the cheapest.

## Getting Started
* Clone the repo
``` git clone https://github.com/KengoWada/Price_Checker```
* Create a branch off the develop branch and push then create a PR.

### End-Points
HTTP Method|Endpoint|Functionality
-----------|--------|-------------
GET|/|Gets all products in the database
GET|/productId|Get a product with the given Id
GET|/supermarkets|Get all the supermarkets
POST|/products|Add product to database
POST|/supermarkets|Add a supermarket and its products and prices
POST|/products/productName/supermarketName|Update a product
DELETE|/products/productName|Add a product

### Author
Kengo Wada
