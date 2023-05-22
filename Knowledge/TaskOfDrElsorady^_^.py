String=input("""You Must Seperate With Spaces !!\n
                Enter Ur Beta3 : """)
N_B=String.count("B");N_S=String.count("S");N_C=String.count("C")
print(f"B : {N_B}\tS : {N_S}\tC : {N_C}")
C_B, C_S, C_C =input("""Without Any Seperate !!\n
                        Enter Count Of Beto3 Like this 211:""")
P_B, P_S, P_C =input("""Without Any Seperate !!\n
                        Enter Count Of Beto3 Like this 111:""")
M=int(input("Enter Ur Money : "))

C_San=(int(P_B)*N_B) + (int(P_S)*N_S) + (int(P_C)*N_C)
# https://codeforces.com/problemset/problem/371/C



