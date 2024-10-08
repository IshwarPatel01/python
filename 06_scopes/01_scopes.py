#scopes ko namespace bhi kaha jata hain

#konsa variable kaha mere liye available hai kaha nai yeh pata karege

#importance sabse jyada global scope aur function scope ko di jati hain

#hum sabse jyada concern rahete function ke scope ke liye qki ifelse mei hum sirf condition check karte hain.

#jab bhi aap ek function banayege toh aise samjiye ki aapne memory ke andr 1ghr banaya hain 

#humare function ke andr jo bhi variable ya jo bhi declare karte hain woh sabka dena dena bas function ke andr hii hai


#aisa bhi ho sakta hai ki woh ghr mei aap chote chote rooms banaye , unko maine scope access kar sakta hai , main ghr ek hi hai toh function toh ek hii mar bana

# jo room ke andr a banaya woh ghr ko access rahega?


#yeh  joh file hai global hain 


username = "ishwar"   #gloabal variable

def func():
    # username = "chai"   #main scope variable
    print(username)

print(username)
func()


x = 99

# def func2(y):
#     z = x + y
#     return z 

# result = func2(1)
# print(result)


# def func3():
#     global x  #avoid this
#     x = 88

# func3()
# # print(func3())
# print(x)

def f1():
    x = 88
    def f2():
        print(x)
    return f2

myresult = f1()
myresult()

#closure start from 20mins # bag throry also called 

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

#yeh hain proper closure
#py mei isko factory function ke naam se bhi jana jata hain 


# ----------------------------------------------
#  ye hii trick hai programming ke andr ki aapke variable ke andr konsi value hai aur konsa data type hain uska woh samj mei aagaya toh 90% programming samaj aati hai aur fir ye aapke sath chalti har programming ke andr