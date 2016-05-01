#!/usr/bin/env python
"""Example of some regular expression operations"""

import re

# re.search() => finds RE match anywhere in the string
assert re.search(r"bar", "foobar").group() == "bar"

# re.match() => finds RE match from start of the string
assert re.match(r"bar", "foobar") is None  # compared with match()

# re.sub(pattern, repl, string) => replace all occurances of RE with repl
assert re.sub(r"rabbit", "eggs", "spam and rabbit") == "spam and eggs"

# '.' => any character except newline
assert re.match(r".", r"\n").group() == '\\'  # r"\n" is 2 char str ('\n')
assert re.match(r".", "\n") is None  # "\n" is 1 char str (newline)

# '*' => 0 or more of preceding RE ('a' followed by zero or any number of 'b's)
pattern = re.compile(r"ab*")  # compile is more efficient when reusing
assert pattern.match("a").group() == "a"
assert pattern.match("abbb").group() == "abbb"
assert pattern.match("c") is None

# '+' => 1 or more of preceding RE
pattern = re.compile(r"ab+")
assert pattern.match("a") is None
assert pattern.match("abbb").group() == "abbb"

# '?' => 0 or 1 of preceding RE
pattern = re.compile(r"ab?")
assert pattern.match("a").group() == "a"
assert pattern.match("abb").group() == "ab"

# '^' => match start of string (with re.M = start of any line)
assert re.search(r"^bar", "foo\nbar", re.M).group() == "bar"
assert re.search(r"^bar", "foo\nbar") is None  # without re.MULTILINE

# '$' => match end of string (with re.M = end of any line)
assert re.search(r"foo$", "foo\nbar", re.M).group() == "foo"
assert re.search(r"foo$", "foo\nbar") is None  # without re.MULTILINE

# {m,n} => match preceding RE m to n number of time
assert re.match(r"a{3,5}", "aaaaaaaa").group() == "aaaaa"  # match max (greedy)
assert re.match(r"a{3,5}?", "aaaaaaaa").group() == "aaa"  # match min

# '\' => escape special characters like *, +, ?, etc.
assert re.match(r"\.\?\*\+", ".?*+").group() == ".?*+"

# [] => match a character as defined within brackets
assert re.match(r"[a-z][A-Z][0-9][a-zA-Z0-9]", "uB40").group() == "uB40"

# A|B => match RE A or B
assert re.match(r".*bar$|foo", "foobarbaz").group() == "foo"

# () => match expression within parentheses and save as special group
pattern = re.compile(r"([A-Z])([0-9][0-9])")
assert pattern.match("B52abc").group(0) == "B52"
assert pattern.match("B52abc").group(1) == "B"
assert pattern.match("B52abc").group(2) == "52"
assert re.sub(r"([a-z]{4})", r'"\1"', "ham and spam") == 'ham and "spam"'

# (?P<group_name>) => similar to regular parentheses, but with group name
assert re.match(r"(?P<foo>[a-z]{3})", "abcdefg").group("foo") == "abc"
