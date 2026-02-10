"""
Recursion Assignment Starter Code
Complete the recursive functions below to analyze the compromised file system.
"""
import os
# ============================================================================
# PART 1: RECURSION WARM-UPS
# ============================================================================
def sum_list(numbers):
    """
    Recursively calculate the sum of a list of numbers.
    """
    if len(numbers)==0:
        return 0
    return numbers[0]+sum_list(numbers[1:])
def count_even(numbers):
    """
    Recursively count how many even numbers are in a list.
    """
    if len(numbers)==0:
        return 0
    return (1 if numbers[0]%2==0 else 0)+count_even(numbers[1:])
def find_strings_with(strings, target):
    """
    Recursively find all strings that contain a target substring.
    """
    if len(strings)==0:
        return[]
    rest=find_strings_with(strings[1:], target)
    if target in strings[0]:
        return[strings[0]]+rest
    return rest
# ============================================================================
# PART 2: COUNT ALL FILES
# ============================================================================
def count_files(directory_path):
    """
    Recursively count all files in a directory and its subdirectories.
    """
    if os.path.isfile(directory_path):
        return 1
    total=0
    for name in os.listdir(directory_path):
        path=os.path.join(directory_path, name)
        if os.path.isfile(path):
            total+=1
        elif os.path.isdir(path):
            total+=count_files(path)
    return total
# ============================================================================
# PART 3: FIND INFECTED FILES
# ============================================================================
def find_infected_files(directory_path, extension=".encrypted"):
    """
    Recursively find all files with a specific extension in a directory tree.
    """
    if os.path.isfile(directory_path):
        return [directory_path] if directory_path.endswith(extension)else[]
    infected=[]
    for name in os.listdir(directory_path):
        path=os.path.join(directory_path, name)
        if os.path.isfile(path) and path.endswith(extension):
            infected.append(path)
        elif os.path.isdir(path):
            infected.extend(find_infected_files(path, extension))
    return infected
# ============================================================================
# TESTING & BENCHMARKING
# ============================================================================
if __name__=="__main__":
    print("Total files (breach_data):", count_files("breach_data"))
    print("Total infected (breach_data):", len(find_infected_files("breach_data")))
