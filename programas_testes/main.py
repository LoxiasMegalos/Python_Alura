# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#   print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

vector = [[1,2],[3,4]]
print(vector)
print()
print(vector[0])
print()
print(vector[0][1])
print()

vector[0][0]= input("Qual primeiro numero da matriz?")

for r in vector:
    for c in r:
        print(c,end = " ")
    print()

