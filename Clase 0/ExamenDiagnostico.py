def RGBtoHex(red, green, blue):
  if(red<0 or red>255 or green<0 or green>255 or blue<0 or blue>255):
    print("Valor no valido")
    return 
  print("#", decToHex(red), decToHex(green), decToHex(blue), sep='')

def decToHex(num):
  letras = ['A', 'B', 'C', 'D', 'E', 'F']
  hex = ""
  
  while num > 0:
    hexTemp = num % 16
    num = num // 16
    if (hexTemp > 10):
      hex = letras[hexTemp - 10] + hex
    else:
      hex = str(hexTemp) + hex
  return hex

def sumaFracciones(num1, den1, num2, den2):
  if(num1<0 or num1>255 or num2<0 or num2>255):
    print("Numeradores no validos")
    return 
  if(den1<=0 or den1>255 or den2<=0 or den2>255):
    print("Denominadores no validos")
    return 

  num = num1*den2 + num2*den1
  den = den1*den2

  while True:
    if(num%2==0 and den%2==0):
      num=num//2
      den=den//2
    elif(num%3==0 and den%3==0):
      num=num//3
      den=den//3
    else:
      break
  return str(num)+'/'+str(den)
  
RGBtoHex(255, 64, 52)
print(sumaFracciones(1,2,1,4))

