main_course_list = []
food_list = ["ข้าวผัด","ข้าวไข่เจียว","ข้าวยำ","ข้าวซอยไก่"]

for food in food_list:
    if food == "ข้าวยำ":
        main_course_list.append(food)
        break

def quli(list_quty):
    max= list_quty[0]
    for x in list_quty :
        if x > max : 
            max = x
    return max
list_quty = [7,4,10,8]
q= (quli(list_quty))

def polar(list_pop):
    min = list_pop[0]
    for y in list_pop:
        if y < min :
            min = y
    return min
list_pop = [5,9,3,5]
p= (polar(list_pop))

sum= (0.6 * q) + (0.4 * p)

print("ข้าวที่เเนะนำ = " , main_course_list , "คะเเนนสำหรับเลือกอาหาร = " , sum)
