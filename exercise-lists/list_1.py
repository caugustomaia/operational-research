########## FIRST EXERCISES LIST - OPERATION RESEARCH ##########
#
#  CONSIDER THE SETS A = {1,2,3,4,5} AND B = {3,4,5,6,7,8} DO PROGRAMS THAT PRINTS THE RESTRICTIONS:
#

A = [1,2,3,4,5]
B = [3,4,5,6,7,8]

#
# I. xi ≤ 50, ∀ i ∈ A
#

print("I. xi ≤ 50, ∀ i ∈ A")
print("")

for i in A:
    print("x_" + str(i) + " <= 50")

#
# II. xi ≤ 50, ∀ i ∈ A, i > 3
#

print("")
print("")
print("")
print("II. xi ≤ 50, ∀ i ∈ A, i > 3")
print("")

for i in A:
    if i>3:
        print("x_" + str(i) + " <= 50")

#
# III. i∈A∑ xi ≥ 2 
#

print("")
print("")
print("")
print("III. i∈ A ∑ xi ≥ 2")
print("")

LHS = ''
for i in A:
    LHS += 'x_' + str(i) + ' + '
print(LHS + ">= 2")

#
# IV. i∈A,i≤4 ∑ xi = 5
#

print("")
print("")
print("")
print("IV. i∈ A,i≤4 ∑ xi = 5")
print("")

LHS = ''
for i in A:
    if i <= 4:
        LHS += 'x_' + str(i) + ' + '
print(LHS + "= 5")

#
# V. yj ≤ i∈ A ∑ xi ∀j ∈ B
#

print("")
print("")
print("")
print("V. yj ≤ i∈ A ∑ xi ∀j ∈ B")
print("")

LHS = ''
for j in B:
    RHS = ''
    LHS = "y_" + str(j)
    for i in A:
        RHS += "x_" + str(i) + ' + '
    print(LHS + " <= " + RHS)

#
# VI. yj = i∈A, i<2 ∑ ∀j ∈ B, j < 3
#

print("")
print("")
print("")
print("VI. yj = i∈ A, i<2 ∑ ∀j ∈ B, j < 3")
print("")

# Shows nothing because all j values are equal or bigger then 3
LHS = ''
for j in B:
    RHS = ''
    if j<3:
        LHS = "y_" + str(j)
        for i in A:
            if i<2:
                RHS += "x_" + str(i) + ' + '
        print (LHS + ' = ' + RHS)

#
# VII. zij ≥ 20, ∀i ∈ A, ∀j ∈ B, i < j
#

print("")
print("")
print("")
print("VII. zij ≥ 20, ∀i ∈ A, ∀ j ∈ B, i < j")
print("")

for i in A:
    for j in B:
        if i<j:
            print ("z_" + str(i) + "_" + str(j) + " >= 20")

#
# VIII. j∈ B ∑ zij = 100, ∀i ∈ A
#

print("")
print("")
print("")
print("VIII. j∈ B ∑ zij = 100, ∀ i ∈ A")
print("")

LHS = ''
for i in A:
    LHS_2 = ''
    LHS = 'z_' + str(i)
    for j in B:
        LHS_2 += LHS + "_" + str(j) + " + "
    print(LHS_2 + " = 100")

#
# IX. j∈ B ∑ i∈A,i>5 ∑ zij ≤ 12
#

print("")
print("")
print("")
print("IX. j∈ B ∑ i∈ A,i>5 ∑ zij ≤ 12 ")
print("")

# LHS of restriction is 0 because all A values are equal or less then 5
LHS = ''
LHS_2 = ''
for j in B:    
    for i in A:
        if i>5:
            LHS = 'z_' + str(i)
            LHS_2 += LHS + '_' + str(j) + ' + '
LHS_2 += ' <= 12'
print (LHS_2)

#
# X. j∈ B, j>i ∑ zij = yi, ∀i ∈ A, i 6= 2
#

print("")
print("")
print("")
print("X. j∈ B, j>i ∑ zij = yi, ∀ i ∈ A, i 6= 2")
print("")

SUM_I = ''
for i in A:
    if i!=2:
        SUM_J = ''
        SUM_I = 'z_' + str(i)
        for j in B:
            if j>i:
                SUM_J+= SUM_I + '_' + str(j) + ' + '
        SUM_J+= ' = y_' + str(i)
        print(SUM_J)

#
# XI. i∈ A ∑ j∈ B,j>i ∑ zij ≥ j∈ B ∑ yj
#

print("")
print("")
print("")
print("XI. i∈ A ∑ j∈ B,j>i ∑ zij ≥ j∈ B ∑ yj") 
print("")

LHS = ''
LHS_2 = ''
LHS_3 = ''
RHS = ''
for i in A:
    LHS = 'z_' + str(i)
    LHS_2 = ''
    for j in B:
        if j>i:
            LHS_2 += LHS + '_' + str(j) + ' + '
    LHS_3 += LHS_2
for j in B:
    RHS += 'y_' + str(j) + ' + '
print (LHS_3 + ' >= ' + RHS)