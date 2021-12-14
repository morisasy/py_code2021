try:
    # some code
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))


try:
    # some code
except (ValueError, KeyboardInterrupt):
    # some code

try:
    # some code
except ValueError:
    # some code
except KeyboardInterrupt:
    # some code

