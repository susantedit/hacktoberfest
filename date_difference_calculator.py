from datetime import datetime, date

def calculate_date_difference(date_str1, date_str2, date_format="%Y-%m-%d"):
    """
    Calculates the absolute difference in days between two dates.
    
    Args:
        date_str1 (str): The first date string (e.g., "2024-10-01").
        date_str2 (str): The second date string.
        date_format (str): The expected format of the date strings 
                           (default is ISO format YYYY-MM-DD).

    Returns:
        int: The absolute number of days between the two dates.
             Returns -1 for invalid input or parsing errors.
    """
    try:
        # 1. Parse the string dates into datetime objects
        date_obj1 = datetime.strptime(date_str1, date_format).date()
        date_obj2 = datetime.strptime(date_str2, date_format).date()
        
        # 2. Calculate the difference (a timedelta object)
        time_difference = date_obj1 - date_obj2
        
        # 3. Extract the number of days and return the absolute value
        return abs(time_difference.days)
        
    except ValueError as e:
        # Handle cases where the format is wrong or the date is invalid
        print(f"Error parsing date: {e}")
        return -1
    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return -1

# --- Example Usage ---

if __name__ == "__main__":
    
    # 1. Standard Test Case (Current year dates)
    date_a = "2025-01-01"
    date_b = "2025-01-31"
    diff_days = calculate_date_difference(date_a, date_b)
    print(f"Days between {date_a} and {date_b}: {diff_days}") # Expected: 30
    
    # 2. Crossing Years Test Case
    date_c = "2024-12-25"
    date_d = "2025-01-05"
    diff_days_2 = calculate_date_difference(date_c, date_d)
    print(f"Days between {date_c} and {date_d}: {diff_days_2}") # Expected: 11

    # 3. Using a different format
    date_e = "01/01/2025"
    date_f = "12/31/2025"
    # Pass the custom format string to the function
    diff_days_3 = calculate_date_difference(date_e, date_f, date_format="%m/%d/%Y")
    print(f"Days between {date_e} and {date_f}: {diff_days_3}") # Expected: 364 (non-leap year)

    # 4. Invalid Input Test
    date_invalid = "2025-99-99"
    calculate_date_difference(date_a, date_invalid)
