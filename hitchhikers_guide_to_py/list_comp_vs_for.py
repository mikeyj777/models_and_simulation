from datetime import datetime as dt

def list_comp():
    r = list(range(97,97+27))
    s = [chr(c) for c in r]

def for_append():
    s = []
    for c in range(97,97+27):
        s.append(chr(c))
    
def for_plus_eq():
    s = ''
    for c in range(97,97+27):
        s += chr(c)


num_tests = 50000

t0 = dt.now()
for i in range(num_tests):
    list_comp()

time_list_comp = dt.now() - t0

t0 = dt.now()
for i in range(num_tests):
    for_append()

time_for_append = dt.now() - t0

t0 = dt.now()
for i in range(num_tests):
    for_plus_eq()

time_for_plus_eq = dt.now() - t0

print("list comp:  {}.  for-append:  {}.  for-plus-eq: {}."\
    .format(str(time_list_comp), str(time_for_append), str(time_for_plus_eq)))

