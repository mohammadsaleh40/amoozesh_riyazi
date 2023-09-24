from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations,\
    implicit_multiplication_application
transformations = (standard_transformations +
    (implicit_multiplication_application,))
from sympy import latex
def gereftan():
    with open("moadele.txt") as f:
        s = f.read().split("=")
        
        ebarat_taraf_ha = list(map(lambda x: parse_expr(x, transformations=transformations), s))
    aamal_taraf_ha =[]


    taraf_ha = ["avval" , "dovom"]
    khorooji = [s[0]+" = "+s[1]]
    
    for x in taraf_ha:
        with open(f"aamal_taraf_{x}.txt") as f:

            aamal_taraf_n = f.read().split("\n")
            aamal_taraf_ha.append(aamal_taraf_n)

    for i in range(len(aamal_taraf_ha[0])):
        st = ""    
        
        for j in range(len(ebarat_taraf_ha)):
            if aamal_taraf_ha[j][i][0] == "-":
                ebarat_taraf_ha[j] -= parse_expr(aamal_taraf_ha[j][i][1:])
        
            if aamal_taraf_ha[j][i][0] == "+":
                ebarat_taraf_ha[j] += parse_expr(aamal_taraf_ha[j][i][1:])
        
            if aamal_taraf_ha[j][i][0] == "*":
                ebarat_taraf_ha[j] *= parse_expr(aamal_taraf_ha[j][i][1:])

            if aamal_taraf_ha[j][i][0] == "/":
                ebarat_taraf_ha[j] /= parse_expr(aamal_taraf_ha[j][i][1:])
        for j in range(len(taraf_ha)):
            print(latex(ebarat_taraf_ha[j]) , end= " ")
            st += latex ( ebarat_taraf_ha[j]) + " "
            if j < len(ebarat_taraf_ha)-1:
                print("=" , end= " ")
                st += "= "
        print()
        khorooji.append(st)


    return khorooji