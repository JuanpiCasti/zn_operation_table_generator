from math import gcd

def class_sum(n, a, b):
    return (a+b)%n

def class_prod(n, a ,b):
    return (a*b)%n

def get_inversibles(n):
    for x in range(1,n):
      if gcd(n,x) == 1:
        yield x

def build_table(n, selected_operation, headers=False, inversibles=False):
    if type(n) != int:
        raise ValueError("Please pass an integer as first argument. ")
    if selected_operation in ["sum", "prod"]:
        operation = class_sum if selected_operation == 'sum' else class_prod
        
        integer_set = list(get_inversibles(n)) if inversibles else set(range(n))

        if headers:
                table = [['+' if selected_operation == 'sum' else '*'] + integer_set]
        else:
            table = []

        for i in integer_set:
            row = [i] if headers else []
            for j in integer_set:
                row.append(operation(n, i, j))
            table.append(row)

        return table
    else:
        raise ValueError("Please pass a valid operation ('sum' or 'prod') as second argument.")