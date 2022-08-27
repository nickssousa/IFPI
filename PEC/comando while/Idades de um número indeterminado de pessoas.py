def main():
    pessoas = 0
    idades= 0
    x= 0
    y= 99999999999999
     
    while True:
      b= int(input())
      if b!= 0:
          pessoas+= 1
          idades+= b

          if x<b: x= b
          if y>b: y= b

      if b== 0:
          break

    if pessoas== 0:
        pass

    else:
        c= idades/pessoas
        print(pessoas)
        print("%.2f"%c)
        print(y)
        print(x)

if __name__== "__main__":
  main()
