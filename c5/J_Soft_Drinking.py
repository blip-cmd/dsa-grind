n, k, l, c, d, p, nl, np = map(int, input().split())

# 1 person 
# n(l) of k(l) 
#   and 1(d) of c(d) 
#       and n(p) of p

total_drink = k * l
total_limes = c * d
total_salt = p

toasts_by_drink = total_drink // nl
toasts_by_limes = total_limes
toasts_by_salt = total_salt // np

max_toasts = min(toasts_by_drink, toasts_by_limes, toasts_by_salt) // n
print(max_toasts)