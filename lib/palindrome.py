def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
    # If string is empty or one character, return itself
    if len(s) < 2:
        return s

    start = 0
    max_length = 1

    # Helper function to expand palindrome from the center
    def expand_from_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    # Check every character as center
    for i in range(len(s)):
        # Odd length palindrome
        length1 = expand_from_center(i, i)
        # Even length palindrome
        length2 = expand_from_center(i, i + 1)
        # Max of the two
        current_max = max(length1, length2)

        # Update max palindrome if found longer
        if current_max > max_length:
            max_length = current_max
            start = i - (max_length - 1) // 2

    # Return the longest palindrome substring
    return s[start:start + max_length]
