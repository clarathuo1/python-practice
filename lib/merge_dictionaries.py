#Merges two dictionaries into a single dictionary. If there are any common keys, their values are summed up.

def merge_dicts(dict1, dict2):

    #Returns dict which is the merged dictionary

    merged_dict = {**dict1, **dict2}
    for key in dict1.keys() & dict2.keys():
        merged_dict[key] = dict1[key] + dict2[key]
    return merged_dict