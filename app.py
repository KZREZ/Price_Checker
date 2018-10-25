from flask import Flask, jsonify, json, request

app = Flask(__name__)

products_list = ['milk', 'bread', 'jam', 'apples']
super_markets = ['CS', 'Shoprite', 'Quality']
products_dict = {
	'milk': {
		'CS': 1500,
		'Shoprite': 1600,
		'Quality': 1350
	},
	'bread': {
		'CS': 3000,
		'Shoprite': 3200,
		'Quality': 2950
	},
	'jam': {
		'CS': 4500,
		'Shoprite': 4900,
		'Quality': 4300
	},
	'apples': {
		'CS': 1000,
		'Shoprite': 1200,
		'Quality': 800
	}
}

@app.route('/products', methods=['GET'])
def get_all_products():
	return jsonify({
		'message': 'Fetched all products.',
		'Products': products_list
		})

@app.route('/supermarkets', methods=['GET'])
def get_all_supermarkets():
	return jsonify({
		'message': 'Fetched all products.',
		'Products': super_markets
		})

@app.route('/products/<productName>', methods=['GET'])
def get_one_product(productName):
	for product in products_list:
		if product == productName:
			return jsonify({
				'message': 'Fetched successfully.',
				productName: products_dict[productName]
				})
	return jsonify({
		'message': 'Product not in DB.'
		})

@app.route('/products', methods=['POST'])
def add_product():
	info = request.json

	productName = info.get('productName')
	productInfo = info.get('productInfo')

	products_dict[productName] = productInfo
	products_list.append(productName)

	return jsonify({
		'message': productName + ' added successfully.'
		})

@app.route('/products/<productName>/<supermarketName>', methods=['POST'])
def update_product_price(productName, supermarketName):
	info = request.json

	productInfo = info.get('price')

	for supermarket in super_markets:
		if supermarketName == supermarket:
			product = products_dict[productName]
			product[supermarketName] = productInfo
			products_dict[productName] = product
			return jsonify({
				'message': 'Updated successfully.',
				productName: products_dict[productName]
			})
		
		return jsonify({
			'message': 'We do not have data on that supermarket yet.'
		})

@app.route('/products/<productName>', methods=['DELETE'])
def delete_product(productName):
	del products_dict[productName]
	products_list.remove(productName)

	return jsonify({
		'message': productName + ' deleted successfully'
	})

@app.route('/supermarkets', methods=['POST'])
def add_supermarket():
	info = request.json

	supermarket = info.get('supermarket')
	products = info.get('products')
	prices = info.get('prices')

	if supermarket not in super_markets:
		super_markets.append(supermarket)
		for product in products:
			if product not in products_list:
				products_list.append(product)
		for product in products_list:
			price = products_dict[product]
			price[supermarket] = prices[product]
		return jsonify({
			'message': 'Done'
		})
	else:
		return jsonify({
			'message': 'Supermarket already exists.'
	})	


if __name__ == '__main__':
	app.run(debug=True)