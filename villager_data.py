"""Functions to parse a file containing villager data."""
filename = open('villagers.csv')
read_file = filename.read()
split_file_lines = read_file.split('\n')
villagers = []
for line in split_file_lines:
    villagers.append(line.split('|'))
    


def all_species(villagers):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    species = set()
    for line in villagers:
        species.add(line[1])
        
    return species


def get_villagers_by_species(villagers, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villager_name = []
    for line in villagers:
        if search_string in line:
            villager_name.append(line[0])

    # TODO: replace this with your code

    return sorted(villager_name)

# print(get_villagers_by_species(villagers, search_string="Rabbit"))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    fitness = []
    nature = []
    education = []
    music = []
    fashion =[]
    play = []

    for line in filename:
        if "Fitness" in line:
            fitness.append(line[0])
        elif "Nature" in line:
            nature.append(line[0])
        elif "Education" in line:
            education.append(line[0])
        elif "Music" in line:
            music.append(line[0])
        elif "Fashion" in line:
            fashion.append(line[0])
        else:
            play.append(line[0])

    fitness = sorted(fitness)
    nature = sorted(nature)
    education = sorted(education)
    music = sorted(music)
    fashion = sorted(fashion)
    play = sorted(play)

    return [fitness, nature, education, music, fashion, play]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    for line in filename:
        all_data.append(tuple(line))

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    # villager_name = []
    for line in filename:
        # print(line[0], line[-1])
        if villager_name == line[0]:
            return line[-1]
    return None
  

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
    personality = ""
    same_personality = set()
    for line in villagers:
        if villager_name in line:
            personality = line[2]
    
    for line in villagers:
        if personality in line:
            same_personality.add(line[0])

    return same_personality

print(find_likeminded_villagers(villagers, "Tutu"))

