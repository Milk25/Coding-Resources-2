# and
# or
# not

1 < 2
# True
2 < 3
# True


1 < 2 < 3
# True

1 < 2 > 3
# False

1 < 2 and 2 > 3
# False
1 < 2 and 2 < 3
# True

'h' == 'h' and 2 == 2
# True
('h' == 'h') and (2 == 2)
# True

1 == 1 or 2 == 2
# True

100 == 1 or 2 == 2
# True

100 == 1 or 2 == 200
# False


1 == 1
# True

not(1 == 1) # False

not 1 == 1
# False

not 400 > 5000
# True

1 != 1
# False
