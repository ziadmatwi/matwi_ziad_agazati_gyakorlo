import ertekel
import sorozat
import poggyasz1
import poggyasz2

print("1. feladat:")
print("Kedves vásárlónk! Kérjük segítsge munkánkat azzal, hogy kitölti az alábbi rövid kérdőivet!:")
print("2/A és B")
customer_name:str = ertekel.input_customer_name()
food_name:str = ertekel.input_food_name()
rating:int = ertekel.input_ratings()
print("2/C")
ertekel.print_out(customer_name,food_name,rating)


print("2.feladat")
print("2/A")
sorozat.random_method(12)
print("2/B")
random_list = []
sorozat.random_method(12,random_list)
print("")
print("2/C")
print(sorozat.random_method_modified(12))
print("2/D")
even_count = sorozat.paratlanok_szama(random_list)
sorozat.printout(even_count)


print("3.feladat")
luggageobject = poggyasz2.Poggyasz()
luggageobject.readfile("csomag.txt")
print(luggageobject.listoftext)