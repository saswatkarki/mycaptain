#code for printing the extention of the filename entered by the user
filename = input("Input the Filename: ")
f_ext = filename.split(".")
print ("The extension of the file is : " + repr(f_ext[-1]))
