

def input_food_name():
    food_name:str= input("Melyik ételt fogyasztotta a kínálatunkból? ")
    return food_name

def input_customer_name():
    customer_name:str = input("Mi a teljes neve? ")
    return customer_name

def input_ratings():
    rating:int = 0
    rating:int= int(input("Nullától ötig, hányasra értékelné a kiszolgálásunkat? "))    
    while rating < 0 or rating > 5:
        if rating < 0:
            print("Az értékelés nem lehet negatív!")
        else:
            print("5 pont feletti értékelés nem elfogadható")
        rating:int= int(input("Nullától ötig, hányasra értékelné a kiszolgálásunkat? "))
    return rating
        
def print_out(food_name:str,customer_name:str, rating:int):
    print(f"Étel neve: {food_name}")
    print(f"Étel rendelőjének neve: {customer_name}")
    print(f"Értékelés(1-5): {rating}")