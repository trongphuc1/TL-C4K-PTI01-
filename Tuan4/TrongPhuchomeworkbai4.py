def sort_and_filter_zoo(animal_list, begin):
    
    sorted_list = sorted(animal_list)
    
    
    filtered_list = filter(lambda x: x.startswith(begin), sorted_list)
    
   
    reversed_list = list(filtered_list)[::-1]
    
    return reversed_list


animal_list = ["elephant", "tiger", "lion", "giraffe", "zebra", "leopard"]
begin_with_L_sorted = sort_and_filter_zoo(animal_list, "L")
print(begin_with_L_sorted)


