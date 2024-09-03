

def read_text(filename):
    """
    
    filename : string, name of file to read
    Returns: string, contains all file contents
    """
    
    inFile = open(filename, 'r')
    line = inFile.read()
    return line

text = read_text ("sonnet18.txt")
print(text)
print(read_text("sonnet18.txt"))