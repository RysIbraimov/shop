# >>> i4 = Item.objects.get(id=4)
# >>> i4.purchase_set.create(name="Jyldyz" , age=45, date_purchase=timezone.now())
# <Purchase: Jyldyz>
# >>> i4.purchase_set.create(name="Kanat" , age=35, date_purchase=timezone.now())
# <Purchase: Kanat>
# >>> i5 = Item.objects.get(id=5)
# >>> i5.purchase_set.create(name="Nurbek" , age=35, date_purchase=timezone.now())
# <Purchase: Nurbek>
# >>> i5.purchase_set.create(name="Nyrkyz" , age=35, date_purchase=timezone.now())
# <Purchase: Nyrkyz>

#
# >>> i1 = Item(name="Shirt",price=300)
# >>> i1.save()
# >>> i2 = Item(name="ball",price=500)
# >>> i2.save()
# >>> i3 = Item(name="glasses",price=3000)
# >>> i3.save()
# >>> i4. = Item(name="phone",price12000)
