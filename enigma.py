import config as co
# a-z vars
a=co.a
b=co.b
c=co.c
d=co.d
e=co.e
f=co.f
g=co.g
h=co.h
i=co.i
j=co.j
k=co.k
l=co.l
m=co.m
n=co.n
o=co.o
p=co.p
q=co.q
r=co.r
s=co.s
t=co.t
u=co.u
v=co.v
w=co.w
x=co.x
y=co.y
z=co.z
# A-Z vars
val = 0
A=co.A
B=co.B
C=co.C
D=co.D
E=co.E
F=co.F
G=co.G
H=co.H
I=co.I
J=co.J
K=co.K
L=co.L
M=co.M
N=co.N
O=co.O
P=co.P
Q=co.Q
R=co.R
S=co.S
T=co.T
U=co.U
V=co.V
W=co.W
X=co.X
Y=co.Y
Z=co.Z
#key
valk = "2021/2/16"
# encode function
def encode6(num1,num2,num3,num4,num5,num6):
    if val == 1:
        ip = num1, (num2-num1), (num3 - num2), (num4 - num3), (num5 - num4), (num6 - num5)
        print(num1,num2,num3,num4,num5,num6,ip)
    pass
def encode3(num1,num2,num3):
    if val == 1:
        ip = num1, (num2-num1), (num3 - num2)
        print(num1,num2,num3,ip)
    pass
def encode4(num1,num2,num3,num4):
    if val == 1:
        ip = num1, (num2-num1), (num3 - num2), (num4 - num3)
        print(num1,num2,num3,num4,ip)
    pass
def encode5(num1,num2,num3,num4,num5):
    if val == 1:
        ip = num1, (num2-num1), (num3 - num2), (num4 - num3), (num5 - num4)
        print(num1,num2,num3,num4,num5,ip)
    pass
def encode2(num1,num2):
    if val == 1:
        ip = num1, (num2-num1)
        print(num1,num2,ip)
    pass
# decode
def decode6(num1,num2,num3,num4,num5,num6):
    if val == 1:
        i2 = (num2 + num1)
        i3 = (num3 + i2)
        i4 = (num4 + i3)
        i5 = (num5 + i4)
        i6 = (num6 + i5)
        ip = num1, i2, i3, i4, i5, i6
        print(num1,num2,num3,num4,num5,num6,ip)
    pass
def decode5(num1,num2,num3,num4,num5):
    if val == 1:
        i2 = (num2 + num1)
        i3 = (num3 + i2)
        i4 = (num4 + i3)
        i5 = (num5 + i4)
        ip = num1, i2, i3, i4, i5
        print(num1,num2,num3,num4,num5,ip)
    pass
def decode4(num1,num2,num3,num4):
    if val == 1:
        i2 = (num2 + num1)
        i3 = (num3 + i2)
        i4 = (num4 + i3)
        ip = num1, i2, i3, i4
        print(num1,num2,num3,num4,ip)
    pass
def decode3(num1,num2,num3):
    if val == 1:
        i2 = (num2 + num1)
        i3 = (num3 + i2)
        ip = num1, i2, i3
        print(num1,num2,num3,ip)
    pass
def decode2(num1,num2):
    if val == 1:
        i2 = (num2 + num1)
        ip = num1, i2
        print(num1,num2,ip)
    pass
# input
# validation:
if co.key == valk:
    val = 1
    pass
else:
    back = input("key")
    if back == co.backdoor:
        val = 1
        print("found a backdoor? devmode initaited")
    pass
# NOTE: add the letter before the word for a sentence
encode5(h,e,l,l,o)
decode5(8,-3,7,0,3)