import csv
# Create a class to hold a product. Call the class "Product". It should have
# fields for name and price.
class Product:
    def __init__(self, name, price):
        # super().__init__()
        self.name = name
        self.price = price

    def __str__(self):
        return f"product name: {self.name}, product price: {self.price}"
# We have a collection of products stored in the
# file "products.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `productreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a Product instance. Then
# return the list with all the Product instances from the function.
#
# Store the instances in the "products" list, below.
products = []
# next() ?
def productreader(products=[]):
    with open('products.csv') as csvfile:
        data = csv.reader(csvfile)
        next(data)
        for row in data:
            print(row)
            products.append(Product(row[0], row[1]))

productreader(products)
# print(product for product in products)
print(products[1])


# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a Product object.
# Print the list of products, 1 record per line.