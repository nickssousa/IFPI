def main():
    list2 = ["Hey",20,14,"Look","An Example List"]

    def total_elements(list):
        count = 0
        for element in list:
            count += 1
        return count

    print("The total number of elements in the list: ", total_elements(list2))
    

    
if __name__== "__main__":
  main()
