def func_args_ex(*args):
    for arg in args:
        print(arg)

def func_kwargs_ex(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}={value}')

func_args_ex(1,2,-3,4,'suresh',7,8,9.0,10)

func_kwargs_ex(name= 'suresh', address= 'Hyderabad', doorNo= '1')