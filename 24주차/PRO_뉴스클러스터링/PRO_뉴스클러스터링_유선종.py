def make_set(string: str) -> dict:
    set_list = [string[i].lower()+string[i+1].lower() for i in range(len(string)-1)
                if string[i].isalpha() and string[i+1].isalpha()]
    set_dict = {}
    for string in set_list:
        if string in set_dict:
            set_dict[string] += 1
        else:
            set_dict[string] = 1
        
    return set_dict

def make_intersection(dict1: dict, dict2: dict) -> list:
    intersection = []
    for key, value in dict1.items():
        try:
            intersection.extend([key] * min(dict2[key], value))
        except:
            pass
    
    return intersection

def make_union(dict1: dict, dict2: dict) -> list:
    union = []
    for key1, value1 in dict1.items():
        try:
            union.extend([key1] * max(dict2[key1], value1))
        except:
            union.extend([key1] * value1)
    
    for key2, value2 in dict2.items():
        try:
            tmp = dict1[key2]
        except:
            union.extend([key2] * value2)
    
    return union

def solution(str1, str2):
    dict1, dict2 = make_set(str1), make_set(str2)
    if not dict1 and not dict2:
        return 1 * 65536
    intersection = make_intersection(dict1, dict2)
    union = make_union(dict1, dict2)

    answer = int((len(intersection) / len(union)) * 65536)
    
    return answer