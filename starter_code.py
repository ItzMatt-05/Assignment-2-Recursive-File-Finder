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
    if numbers[0]%2==0:
        return 1+count_even(numbers[1:])
    return count_even(numbers[1:])


def find_strings_with(strings,target):
    """
    Recursively find all strings that contain a target substring.
    """
    if len(strings)==0:
        return []
    if target in strings[0]:
        return [strings[0]]+find_strings_with(strings[1:],target)
    return find_strings_with(strings[1:],target)

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
    for item in os.listdir(directory_path):
        full_path=os.path.join(directory_path,item)
        total+=count_files(full_path)
    return total


# ============================================================================
# PART 3: FIND INFECTED FILES
# ============================================================================

def find_infected_files(directory_path,extension=".encrypted"):
    """
    Recursively find all files with a specific extension in a directory tree.
    """
    if os.path.isfile(directory_path):
        if directory_path.endswith(extension):
            return [directory_path]
        return []
    infected=[]
    for item in os.listdir(directory_path):
        full_path=os.path.join(directory_path,item)
        infected+=find_infected_files(full_path,extension)
    return infected


# ============================================================================
# TESTING & BENCHMARKING
# ============================================================================

if __name__ == "__main__":
    print("RECURSION ASSIGNMENT - STARTER CODE")
    print("Complete the functions above, then run this file to test your work.\n")
    
    print("Total files (Test Case 1):", count_files("test_cases/case1_flat")) # 5
    print("Total files (Test Case 2):", count_files("test_cases/case2_nested")) # 4
    print("Total files (Test Case 3):", count_files("test_cases/case3_infected")) # 5

    print("Total files (breached files):", count_files("breach_data"))

    print("Total Infected Files (Test Case 1):", len(find_infected_files("test_cases/case1_flat"))) # 0
    print("Total Infected Files (Test Case 2):", len(find_infected_files("test_cases/case2_nested"))) # 0
    print("Total Infected Files (Test Case 3):", len(find_infected_files("test_cases/case3_infected"))) # 3

    print("Total Infected Files (breached files):", len(find_infected_files("breach_data")))
