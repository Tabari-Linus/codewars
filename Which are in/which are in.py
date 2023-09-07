def in_array(array1, array2):
    results = []
    for item in array1:
        for word in array2:
            if item in word and item not in results:
                results.append(item)

    results = sorted(results)
    return results

# worded but couldn't pass all test attempts
# def in_array(array1, array2):
#     results = []
#     for item in array1:
#         for i in range(len(array2)):
#             if set(item).issubset(set(array2[i])):
#                 if item in results:
#                     continue
#                 else:
#                     results.append(item)

#     results = sorted(results)
    return results


a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]





print(in_array(a1,a2))