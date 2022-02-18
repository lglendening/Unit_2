'''
In your notebook
Predict what the following inputs will result in
Once you have filled in the "prediction" column, check your answers in interactive mode and write the actual result.
    Input                                       Prediction                                      Result
1.  float('1')                                  1                                               1
2.  str(1 + '2')                                error                                           error
3.  str('2')                                    2                                               2
4.  int('abc')                                  error                                           error
5.  int(float('1.6'))                           float                                           float
6.  float(int(1.6))                             INT                                             int
7.  str(float(1))                               1                                               1


In script mode
Create a program which will take in an input and print out that input divided by 2.
Alter one line of that program to return only whole numbers.

'''
number = input ("Give me a number: ")
print(number/2)
