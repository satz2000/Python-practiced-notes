"""
# What is modules in python?
    break down the entire code in smaller packages or modules for easy understanding and debugging,
    that can reusable for the future projects without copy code from that, just use as package (import and use it)
"""

def hello():
    print("Hello", __name__)
    print("How are you ?")

# special variable
if __name__ == "__main__":
    # call the function inside the special variable
    hello()
