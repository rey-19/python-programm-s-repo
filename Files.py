my_file = open('text.txt',"a")
my_file.write("\nFatty")
my_file.close()
#open('FILE NAME','r/r+/a') u can mention 3 things -read(r) , read and appened(r+) , appened(a)
#readable()-tells us whether file is readable or not 
#read()-reads everything in the file 
#readline()-reads the first line of the document 
#          -when 2 consecutive readline functions are excuted it goes to the next line 
#close()-close the opened file 
