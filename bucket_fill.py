
def load_image(filename):
    """ Load image from file made of 0 (unfilled pixels) and 1 (boundary pixels) and 2 (filled pixel)

    Example of content of filename:

0 0 0 0 1 1 0 0 0 0
0 0 1 1 0 0 1 1 0 0
0 1 1 0 0 1 0 1 1 0
1 1 0 0 1 0 1 0 1 1
1 0 0 1 0 0 1 0 0 1
1 0 0 1 0 0 1 0 0 1
1 1 0 1 0 0 1 0 1 1
0 1 1 0 1 1 0 1 1 0
0 0 1 1 0 0 1 1 0 0
0 0 0 0 1 1 0 0 0 0

    Args:
        filename (str) : path to file containing the image representation

    Returns:
        list : a 2D representation of the filled image, where
               0 represents an unfilled pixel,
               1 represents a boundary pixel
               2 represents a filled pixel
    """

    image = []
    with open(filename) as imagefile:
        for line in imagefile:
            if line.strip():
                row = list(map(int, line.strip().split()))
                image.append(row)
    return image


def stringify_image(image):
    """ Convert image representation into a human-friendly string representation

    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)

    Returns:
        str : a human-friendly string representation of the image
    """

    if image is None:
        return ""

    # The variable "mapping" defines how to display each type of pixel.
    mapping = {
        0: " ",
        1: "*",
        2: "0"
    }

    image_str = ""
    if image:
        image_str += "_ " * (len(image[0]) + 2) + "\n"
    for row in image:
        image_str += "| "
        for pixel in row:
            image_str += mapping.get(pixel, "?") + " "
        image_str += "|"
        image_str += "\n"
    if image:
        image_str += "‾ " * (len(image[0]) + 2) + "\n"

    return image_str


def show_image(image):
    """ Show image in terminal

    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)
    """
    print(stringify_image(image))


def valid_seed_type(seed_coords):
    """
    Checks that the seed point elements are of the type int

    Parameters
    -----------
    First: Coordinate tuple of seed point -> (x,y)
    """
    x, y = seed_coords
    seed1 = isinstance(x, int)
    seed2 = isinstance(y, int)

    if seed1 and seed2:
        return seed_coords
    else:
        return 'Returning image'


def valid_seed_size(seed_coords, original_image):
    """
    This checks if the given seed coordinates are valid
    for the chosen image (valid here means that the seed
    exists in the image)

    Parameters
    ------------
    First: Tuple of integers -> (x,y)
        Coordiantes of the seed point from which the image will be filled.
        Must have the same dimensionality as the image.

    Second: Image to fill -> 2D list
        Original image that we wish to fill.

    Returns
    ------------
    Boolean:
        If the seed coordinate exists in the image list -> True
        Else -> False
    """
    (seed_row, seed_col) = seed_coords
    if seed_row > len(original_image)-1:
        return 'Return image'
    elif seed_col > len(original_image[0])-1:
        return 'Return image'
    else:
        return seed_coords


def valid_seed_val(seed_coords):
    """
    Checks if the seed coordinates are positive values
    such that we ignore all negative inputs
    """
    x,y = seed_coords
    if x < 0 or y < 0:
        return 'Return image'
    else:
        return seed_coords


def valid_seed(seed_coords, image):
    """
    Check if the seed coordinates are valid for both size and type

    Parameters
    ------------
    First: Tuple of coorindates for the seed site -> (x,y)

    Second: Image to be filled -> 2D list


    Returns
    ---------
    If seed site is valid:
        -> True
    Else:
        -> False
    """
    seed_coords = valid_seed_type(seed_coords)

    if type(seed_coords) == str:
        return False

    seed_coords = valid_seed_size(seed_coords, image)
    if type(seed_coords) == str:
        return False

    seed_coords = valid_seed_val(seed_coords)
    if type(seed_coords) == str:
        return False

    return True


def valid_coord(x, y, list):
    """
    Checks if the given coordinate is valid in the image

    Parameters
    ----------
    First: x coordinate -> int

    Second: y coordinate -> int

    Third: list -> 2D list

    Returns
    ---------
    If the coordinate exists in the list:
        -> True
    Else:
        -> False
    """
    if x < 0 or y < 0:
        return False
    try:
        list[x][y]
        return True
    except (IndexError):
        return False


def add_coord_to_set(img, x, y, past_set, future_set):
    """
    Adds the chosen coordinate to future_set after ensuring
    it has not already been checked

    Parameters
    -----------
    First: Image -> 2D list

    Second: x coordinate -> int

    Third: y coordinate -> int

    Fourth: Set of already checked site coordinates -> {(x,y)}

    Fifth: Set of site coordinates to be checked -> {(x,y)}

    Returns
    ----------
    Updated set of sites to be checked -> {(x,y), (x1,y1), ...}
    """
    if valid_coord(x, y, img):
        if (x,y) not in past_set:
          future_set.add((x, y))
    return future_set


def get_neigh_coords( x, y):
    """
    Returns neighbour coordinates of the point (x,y)
    """
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]


def include_neighbours(coords, past_set, future_set, img):
    """
    Updates the future_set. Determines whether a site is in a corner
    or edge of the grid and accordingly adds the next sites to
    be checked (if they have not been checked beforehand).

    Parameters
    -----------
    First: Coordinates of desired site -> (x,y)

    Second:  Set of already checked site coordinates -> {(x,y)}
        Will be used so that sites that have already been checked
        do not need to be checked again, and so that their
        neighbours do not need to be added.

    Third: Set of tuples correspond to sites to be checked -> {(x,y)}
        Valid neighbour sites that are not in past_set will be added
        to this set. The Set data type is used so that neighbour sites
        cannot be added multiple times.

    Fourth: Image -> 2D list

    Returns
    ---------
    Updated set of tuples corresponding to neighbour sites that have
    not previously been checked -> {(x,y), (x1,y1) ...}
    """
    x, y = coords
    neigh_coords = get_neigh_coords(x, y)
    for neighs in neigh_coords:
        x1, y1 = neighs
        future_set = add_coord_to_set(img, x1, y1, past_set, future_set)
    return future_set


def extend_future_set(coords, image, future_set, past_set):
    """
    Ends the fill and returns the original image if the seed
    point is a boundary, and otherwise returns an updated
    future set (with valid neighbour site coords)

    Parameters
    ----------
    First: Tuple of coordinates of desired site -> (x,y)
        Coordinates of site from which neighbour sites will be found

    Second: List representation of image (2D)
        Input image as a 2D list, where each site has a value of either
        0, 1, or 2

    Third: Set of tuples of form -> {(x,y)}
        Set of sites that whose values will be checked

    Fourth: Set of tuples of form -> {(x,y)}
        Set of tuples corresponding to coordinates of sites whose values
        have already been checked

    Returns
    ----------
    Updated set of tuples of form -> (x,y), where additional entries are
    neighbour sites that have not been previously checked.
    """
    x, y = coords

    if image[x][y] == 0:
        image[x][y] = 2
        past_set.add((x,y))

    if image[x][y] == 1:
        future_set = past_set
        return future_set

    return include_neighbours(coords, past_set, future_set, image)


def iterate_future_set(original_image, future_set, past_set):
    """
    Function that updates the values of the sites in the image,
    as well as the set of checked sites.

    Parameters
    -----------
    First: Image to fill -> 2D list

    Second: Set of coordinates of sites to check -> {(x,y)}

    Third: Set of coordinates of sites already checked -> {(x,y)}

    -----------
    Run in a while loop until future_set is empty
    """

    future_set_list = list(future_set)
    for i in future_set_list:
        x, y = i; point = original_image[x][y]
        if i in past_set:
            pass #Already checked and so ignored
        elif point == 1:
            past_set.add((x,y)) #Boundary point.
        elif point == 0:
            future_set = extend_future_set(i, original_image,
                                          future_set, past_set)
        future_set.remove((x,y))


def invalid_image(img):
    try:
        len(img)
        len(img[0])
    except (TypeError, IndexError):
        return True
    else:
        return False


def fill(image, seed_point):
    """
    Fills an image from given seed point to boundary.

    Parameters
    -----------
    First: Image to be filled -> 2D list
        Must consist of 0s (==> unfilled site) or 1s (==> filled site)
        exclusively.

    Second: Tuple of seed point coordinates -> (x,y)
        Will be tested to ensure this seed exists in the list and
        that the site is a 0

    Returns
    ----------
    2D list with filling from the seed point to the boundary
        0 ==> Remains unfilled pixel
        1 ==> Boundary site
        2 ==> Filled pixel
    """
    if invalid_image(image):
        return image

    if not valid_seed(seed_point, image):
        return image

    #Initialising the future_set and checked sets
    past_set = set()
    future_set = set()

    #Adds the neighbours of the seed point to the future_set
    future_set = extend_future_set(seed_point, image,
                                future_set, past_set)

    #Continually updates both sets, stops adding neighbours
    while len(future_set) != 0:
        iterate_future_set(image, future_set, past_set)

    return image


def example_fill():
    image = load_image("data/smiley.txt")
    print("Before filling:")
    show_image(image)

    image = fill(image=image, seed_point=(5,5))

