from views.books import books
class BookList:

    def get(self):
        return books
class Bookdetail():
    def get(self,**kwargs):
        # print(kwargs)
        id=kwargs["id"]
        book=list(filter(lambda p:p["bk_id"]==id,books))
        return book
class Bookprice():
    def get(self,**kwargs):
        price=kwargs["price"]
        price=list(filter(lambda p:p["price"]<=price,books))
        return price



# m = Bookdetail()
# print(m.get(id=101))
m2 = Bookprice()
print(m2.get(price=550))