#Karin Papismadov 209325810
#Yael Amsalem 314667411


def jacobi(a,b):   #a stands for the matrix's values and b are the results of each equation.
    if abs(a[0][0])<(abs(a[0][1])+abs(a[0][2])) or abs(a[1][1])<(abs(a[1][0])+abs(a[1][2])) or abs(a[2][2])<\
            (abs(a[2][0])+abs(a[2][1])):
        print ("The matrix entered is not a diagonal dominant matrix")
    else:
        x = 0
        y = 0
        z = 0
        eps = 0.001 #epsilon
        i = 0
        for i in range(9):
            X_1 = (b[0] - a[0][1] * y - a[0][2] * z) / a[0][0]
            Y_1 = (b[1] - a[1][0] * x - a[1][2] * z) / a[1][1]
            Z_1 = (b[2] - a[2][0] * x - a[2][1] * y) / a[2][2]
            print("Jacobi",i, "number:", X_1, " ", Y_1, " ", Z_1)
            if X_1 - x < eps and Y_1 - y < eps and Z_1 - z < eps:
                break

            x = X_1
            y = Y_1
            z = Z_1


def Gauss_Seidel(a,b): #a stands for the matrix's values and b are the results of each equation.
    if abs(a[0][0]) < (abs(a[0][1]) + abs(a[0][2])) or abs(a[1][1]) < (abs(a[1][0]) + abs(a[1][2])) or abs(a[2][2]) < \
            (abs(a[2][0]) + abs(a[2][1])):
        print("The matrix entered is not a diagonal dominant matrix")
    else:
        x = 0
        y = 0
        z = 0
        eps = 0.001 #epsilon
        i = 0
        for i in range(10):
            X_1 = (b[0] - a[0][1] * y - a[0][2] * z) / a[0][0]
            Y_1 = (b[1] - a[1][0] * X_1 - a[1][2] * z) / a[1][1]
            Z_1 = (b[2] - a[2][0] * X_1 - a[2][1] * Y_1) / a[2][2]
            if 10>eps:
                print("Gauss Seidel", i, "number:", X_1, " ", Y_1, " ", Z_1)
                break

            x = X_1
            y = Y_1
            z = Z_1

#main function

#building a matrix with user's values

print("Please enter the matrix's values only (without solutions) from left to right:")
i=0
j=0
a = []
for i in range(3):          # A for loop for row entries
    m =[]
    for j in range(3):      # A for loop for column entries
         m.append(int(input()))
    a.append(m)

print("Please enter the matrix's solutions only from top to bottom:")
b=[]
for i in range(3):
    b.append(int(input()))


jacobi(a,b)
Gauss_Seidel(a,b)
