# If you want an n-bit representation of binary, you can use the lambda function.
getbinary = lambda x, n: format(x, 'b').zfill(n)

print(getbinary(11, 21))

# See also
# https://appdividend.com/2021/06/14/how-to-convert-python-int-to-binary-string/