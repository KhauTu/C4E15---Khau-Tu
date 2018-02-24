'''
S = 's\np\ta\x00m' # Escape sequences
S = '''...multiline...''' # Triple-quoted block strings
S = r'\temp\spam' # Raw strings (no escapes)
S = b'sp\xc4m' # Byte strings
S = u'sp\u00c4m' # Unicode strings
S1 + S2 # Concatenate
S * 3 # Repeat
S[i] # index
S[i:j] # slice
len(S) # length
"a %s parrot" % kind # String formatting expression
"a {0} parrot".format(kind) # String formatting method
S.find('pa') # String methods: search
S.rstrip() # remove whitespace
S.replace('pa', 'xx') # replacement
S.split(',') # split on delimiter
S.isdigit() # content test
S.lower() # case conversion
S.endswith('spam') # end test
'spam'.join(strlist) # delimiter join
S.code('latin-1') # Unicode encoding
B.decode('utf8') # Unicode decoding
for x in S: print(x) # Iteration
'spam' in S # membership
[c * 2 for c in S]
map(ord, S)
re.match('sp(.*)am', line) # Pattern matching: library module
'''
S = "spa'm" # Sing- and Double-Quoted strings are the same
print(S)

'''
Escape Meaning
\newline Ignored (continuation line)
\\ Backslash (stores one \)
\' Single quote (stores ')
\" Double quote (stores ")
\a Bell
\b Backspace
\f Formfeed
\n Newline (linefeed)
\r Carriage return
\t Horizontal tab
\v Vertical tab
\xhh Character with hex value hh (exactly 2 digits)
\ooo Character with octal value ooo (up to 3 digits)
\0 Null: binary 0 character (doesn’t end string)
\N{ id } Unicode database ID
\uhhhh Unicode character with 16-bit hex value
\Uhhhhhhhh Unicode character with 32-bit hex valuea
\other Not an escape (keeps both \ and other)

>>> path = r'C:\new\text.dat'
>>> path # Show as Python code
'C:\\new\\text.dat'
>>> print(path) # User-friendly format
C:\new\text.dat
>>> len(path) # String length
15
'''
'''
% python
>>> len('abc') # Length: number of items
3
>>> 'abc' + 'def' # Concatenation: a new string
'abcdef'
>>> 'Ni!' * 4 # Repetition: like "Ni!" + "Ni!" + ...
'Ni!Ni!Ni!Ni!'
'''
'''
>>> myjob = "hacker"
>>> for c in myjob: print(c, end=' ') # Step through items, print each (3.X form)
...
h a c k e r
>>> "k" in myjob # Found
True
>>> "z" in myjob # Not found
False
>>> 'spam' in 'abcspamdef' # Substring search, no position returned
True
'''
'''
>>> S = 'spam'
>>> S[0], S[−2] # Indexing from front or end
('s', 'a')
>>> S[1:3], S[1:], S[:−1] # Slicing: extract a section
('pa', 'pam', 'spa')
'''
