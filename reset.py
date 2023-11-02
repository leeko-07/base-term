#Execute this to reset 'history.txt' and 'base.csv' documents and start new ones.
def deleteContent(fName):
    with open(fName, "w"):
        pass
deleteContent('base.csv')
deleteContent('history.txt')
deleteContent('cats.txt')

print('Successfully ')


# --------------------- END OF RESET.PY ---------------------------------