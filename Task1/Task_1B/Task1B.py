import sympy as sym
import Task1A


def find_jacobian(x1,x2,x1_dot,x2_dot):
    jacobs=[]
    solution = Task1A.solve_equation(x1_dot,x2_dot)
    ################ Write your code here ################
    
    ######################################################
    return jacobs

if __name__ == '__main__':
    x1,x2 = sym.symbols('x1,x2')
    x1_dot= -x1 + 2*x1**3 + x2
    x2_dot = -x1 -x2
    jacobs = find_jacobian(x1,x2,x1_dot,x2_dot)
    print('\n', 'Jacobians: \t', jacobs)
    
