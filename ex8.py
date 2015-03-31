#define the string formatter as %r %r %r %r
formatter = "%r %r %r %r"

#prints 1 2 3 4
print formatter % (1, 2, 3, 4)
#prints 'one' 'two' 'three' 'four'
print formatter % ("one", "two", "three", "four")
#prints 'True' 'False' 'False' 'True'
print formatter % (True, False, False, True)
#prints '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
print formatter % (formatter, formatter, formatter, formatter)
#prints 'I had this thing.' 'That you could type up right.' ' But it didn't sing'
#'So I said goodnight'
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)