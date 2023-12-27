################
Basic file handing
By: Sai Mahesh
19 DEC 2023
############

#Specify file name
my_filename = "logfile.txt"

#use try function
try:
    with open(my_filename, "a") as file_handle:
        print(f"Writing a test line to {my_filename}")
        file_handle.write("Test line")
except IOError as err:
    print(f"IOError was {err}")
except EOFError as err:
    print(f"End of file error was {err}")
except OSError:
    print("OS Error")
except:
    print("General Error")
else:
    print("File created")
finally:
    print("Finishing up!")
    # Closed because the statement suffices.
    # file_handle.close()