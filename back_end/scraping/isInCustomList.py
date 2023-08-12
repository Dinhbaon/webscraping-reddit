def isInCustomList(custom_list : list[str],  element: str):
    processed_list = []
    for i in range(len(custom_list)):
        if any(b in ' '.join(map(str, element)) for b in custom_list[i]): 
            processed_list.append(custom_list[i][0])
    return processed_list