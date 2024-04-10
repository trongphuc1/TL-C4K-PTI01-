def sort_and_filter_zoo(animal_list, begin):
    # Sắp xếp danh sách con vật theo thứ tự giảm dần
    sorted_list = sorted(animal_list)
    
    # Lọc danh sách con vật bắt đầu bằng chữ cái cụ thể
    filtered_list = filter(lambda x: x.startswith(begin), sorted_list)
    
    # Đảo ngược danh sách
    reversed_list = list(filtered_list)[::-1]
    
    return reversed_list

try:
    animal_list = ["elephant", "tiger", "lion", "giraffe", "zebra", "leopard"]
    begin_with_L_sorted = sort_and_filter_zoo(animal_list, "L")
    print(begin_with_L_sorted)
except Exception as e:
    print("An error occurred:", e)

