# from .models import Product
# from random import randint

# products_all = Product.objects.all()

# class FeaturedProduct:
# 	'''
# 	Список продуктов для сортировки на главной 
# 	странице под заголовком Featured Product

# 	'''

# 	featured_vegetables = list(products_all.filter(draft=False, department=1).order_by('-pub_date')[:2])
# 	featured_meat = list(products_all.filter(draft=False, department=2).order_by('-pub_date')[:2])
# 	featured_fruits = list(products_all.filter(draft=False, department=3).order_by('-pub_date')[:2])
# 	featured_salads = list(products_all.filter(draft=False, department=9).order_by('-pub_date')[:2])

# 	list_featured_products = featured_vegetables + featured_meat + featured_fruits + featured_salads


# 	def get_random(args):
# 	    random_values = []
# 	    repeat = []
# 	    i = 0
# 	    while i <= len(args) - 1:
# 	        random_number = randint(0, len(args) - 1)
# 	        if str(random_number) in repeat:
# 	            continue
# 	        else:
# 	            random_values.append(args[random_number])
# 	            repeat.append(str(random_number))
# 	        i += 1
# 	    return random_values


# 	featured_products = get_random(list_featured_products)