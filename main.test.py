from main import select_lowercase_string_array, select_stemmed_string_array, select_tokenized_array, \
    select_string_array_without_stop_words

import pytest

selected = select_lowercase_string_array(["TEST", "test", "Test"])
assert selected == ["test", "test", "test"]

selected = select_stemmed_string_array(["conjonction", "test2"])
assert selected == ['conjonct', 'test2']

selected = select_tokenized_array("This is a test")
assert selected == ['This', 'is', 'a', 'test']

selected = select_string_array_without_stop_words(["test", "is", "test2"])
assert selected == ["test", "test2"]

