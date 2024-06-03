import sympy as sym


def solve_equation(x1_dot,x2_dot):
    ################ Write your code here ################
    
    ######################################################
    return result


if __name__ == '__main__':
    x1,x2 = sym.symbols('x1,x2')
    x1_dot= -x1 + 2*x1**3 + x2
    x2_dot = -x1 -x2
    solution = solve_equation(x1_dot,x2_dot)
    print('\n', 'Original solution: \t', solution)
    