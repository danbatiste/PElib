# iter_lib.py






def remove_duplicates(elements):
    """Returns a copy of the input list without duplicates removed.
    
        EX: remove_duplicates([1,2,3,3,4,4,4]) -> [1,2,3,4]
        - elements: The input list
        
    remove_duplicates(elements: list) -> list"""
    return list(set(elements))