# def open_or_senior(data):
#     count = 0
#     for item in data:
#         if item[0] > 55 and item[1] > 7:
#             data[count] = ['Senior']
#         else:
#             data[count] = ['Open']
#         count +=1 
#     return data



def open_or_senior(data):
    data = ["Senior" if item[0] >= 55 and item[1] > 7 else 'Open' for item in data]
    return data


registration_data =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
print(open_or_senior(registration_data))