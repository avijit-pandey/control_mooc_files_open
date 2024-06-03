import sympy as sym
import Task1A
import Task1B


def eigens(jacobs):
    eigenvalues = []
    stability = []
    ################ Write your code here ################
    
    ######################################################
    return eigenvalues, stability


if __name__ == '__main__':
    x1,x2 = sym.symbols('x1,x2')
    x1_dot= -x1 + 2*x1**3 + x2
    x2_dot = -x1 -x2
    solution = Task1A.solve_equation(x1_dot,x2_dot)
    jacobs = Task1B.find_jacobian(x1,x2,x1_dot,x2_dot)
    eigenvalues, stability = eigens(jacobs)
    print('\n', 'eigenvalues: ', eigenvalues, '\n', 'stability: ', stability)
    
