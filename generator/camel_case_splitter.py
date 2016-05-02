import re


# Credit: http://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
def camel_case_to_underscore(camel_case_input):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_case_input)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def test_camel_case_to_underscore():

    test_values = [
        ("singleLetterWordsIsAPain", "single_letter_words_is_a_pain"),
        ("butAbbreviationsLikeHTTPShouldStillWork", "but_abbreviations_like_http_should_still_work"),
        ("my_oh_my_is_this_already_fixed?", "my_oh_my_is_this_already_fixed?"),
    ]

    def test_with_values(before, expected):
        after_removing_camel_case = camel_case_to_underscore(before)
        if after_removing_camel_case != expected:
            print "'%s' does not equal '%s'" % (after_removing_camel_case, expected)
            return False
        return True

    result = True

    for withCamelCase, no_camel_case in test_values:
        if not test_with_values(withCamelCase, no_camel_case):
            result = False

    assert result

if __name__ == "__main__":
    test_camel_case_to_underscore()



