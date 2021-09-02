def celsius_to_farenheit(c) :
    f = (9/5)*c + 32
    return print(f)

def hour(m,s):
    h = (m/60) + (s/3600)
    return print(h)

a = int(input("Enter the value of temperature in celsius : "))
celsius_to_farenheit(a)

b = int(input("Enter the no of minutes : "))
c = int(input("Enter the no of seconds : "))
hour(b,c)
