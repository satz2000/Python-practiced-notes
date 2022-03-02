# How to read and write text files in python

# how to create a files and write some data in it.
Files = open("Files.txt", "w")          # using the keyword open to access the text files, "W" is a writing mode
Files.writelines("Hai G")
Files.writelines("\nHow are you sir?")
Files.writelines("\nIam fine")
# After opening and writing in the file, we need to close the files
Files.close()

# or you can also use loop to writing a paragraph for advance and automated stuff
def write_files():

    # creating a text files and to stored using a variable called Files
    Files = open("Files.txt", "w")

    # Getting the topic/Heading of the user entered data
    topic = input("Enter a topic of Your data: ")

    # write the topics into the text files
    Files.write(topic)

    print("Add your information by giving input value:")
    print("------------------------------")
    for i in range(1000):

        print("To stop the loop by enter keyword 'stop':")
        user = input("")

        # If user input is about stop, then breaks the loop
        if user.lower() == "stop":
            break
        # If user input is not about stop then writes the data into the files
        Files.writelines(f"\n{user}")

    # Finally, after the writing is completed then close the files that are opened
    Files.close()

# Call the function
write_files()
