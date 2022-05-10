from views.models import products
class MobileList:

    def get(self):
        return products
# class Mobiledetail():
#     def get(self,**kwargs):
#         # print(kwargs)
#         id=kwargs["id"]
#         product=list(filter(lambda p:p["pid"]==id,products))
#         return product
class Mobileprice():
    def get(self,**kwargs):
        lower=kwargs["low"]
        upper = kwargs["upp"]
        price = list(filter(lambda p:p["price"] in range(lower,upper),products))
        return price

m = Mobileprice()
# print(m.get(id=101))
print(m.get(low=15000,upp=25000))