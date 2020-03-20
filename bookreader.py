filenames = ('a_tale_of_two_cities.txt','siddharta.txt')



def count_words(filename):
    """ Gets a file and  """
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print('File not found.')
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} is {num_words} words long.")



for filename in filenames:
    count_words(filename)
