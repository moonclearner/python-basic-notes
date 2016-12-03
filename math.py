def calc_prod(lst):
	def math():
		return reduce(lambda x, y : x * y, lst)
	return math

f = calc_prod([1, 2, 3, 4])
print f()

# def calc_prod(lst):
#     def prod():
#         return reduce(lambda x, y : x * y, lst)
#     return prod

# f = calc_prod([1, 2, 3, 4])
# print f()
# 