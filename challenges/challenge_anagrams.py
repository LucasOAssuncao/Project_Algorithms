def sort_list(letters):
    if len(letters) <= 1:
        return letters

    mid = len(letters) // 2
    left_half = letters[:mid]
    right_half = letters[mid:]

    left_half = sort_list(left_half)
    right_half = sort_list(right_half)

    return merge(left_half, right_half)


def merge(left_half, right_half):
    result = []

    while len(left_half) > 0 and len(right_half) > 0:
        if left_half[0] < right_half[0]:
            result.append(left_half[0])
            left_half = left_half[1:]
        else:
            result.append(right_half[0])
            right_half = right_half[1:]

    result += left_half
    result += right_half

    return result


def are_words_equal(word1, word2):
    return bool(word1 and word2 and word1 == word2)


def is_anagram(first_string, second_string):
    first_string_list_ordered = sort_list(list(first_string.lower()))
    second_string_list_ordered = sort_list(list(second_string.lower()))

    return (
        "".join(first_string_list_ordered),
        "".join(second_string_list_ordered),
        are_words_equal(
            "".join(first_string_list_ordered),
            "".join(second_string_list_ordered),
        ),
    )
