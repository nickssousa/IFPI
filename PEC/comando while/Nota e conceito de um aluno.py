def main():
  a= float(input())
  while a>= 11 or a< 0:
    print("Nota inválida.")
    a= float(input())
  if a>= 8.5:
    print("A")
  if 8.5>a and a>= 7.0:
    print("B")
  if 7.0>a and a>= 5.0:
    print("C")
  if 5.0>a and a>= 4.0:
    print("D")
  if 4.0>a and a>= 0:
    print("E")


if __name__== "__main__":
  main()
