from bucket_fill import fill, load_image

import random


def test_random_strcoord(N, seed_coords):
    orig_img = [[0 for i in range(N)] for j in range(N)]
    orig_img = fill(orig_img, seed_coords)
    ans = [[0 for i in range(N)] for j in range(N)]
    assert orig_img == ans
    print("Success: string input\n")


def test_random_floatcoord(N, seed_coords):
    orig_img = [[0 for i in range(N)] for j in range(N)]
    ans = [[0 for i in range(N)] for j in range(N)]
    orig_img = fill(image = orig_img, seed_point = seed_coords)
    assert orig_img == ans
    print("Success: non-integer float input\n")


def integer_float_input(N):
    orig_img = [[0 for i in range(N)] for j in range(N)]
    seed_coords = (1.0,2)
    orig_img = fill(orig_img, seed_coords)
    ans = [[0 for i in range(N)] for j in range(N)]
    assert (orig_img == ans)
    return print("Success: integer float input\n")


def test_full_0(N, seed_coords):
    orig_img = [[0 for i in range(N)] for j in range(N)]
    orig_img = fill(orig_img, seed_coords)
    ans = [[2 for i in range(N)] for j in range(N)]
    assert (orig_img == ans)
    return print("Success: square of all 0\n")


def test_full_1(N, seed_coords):
    orig_img = [[1 for i in range(N)] for j in range(N)]
    orig_img = fill(orig_img, seed_coords)
    ans = [[1 for i in range(N)] for j in range(N)]
    assert (orig_img == ans)
    return print("Success: square of all 1\n")


def test_empty_row(N, seed_coords):
    orig_img = [[0 for i in range(N)]]
    orig_img = fill(orig_img, seed_coords)
    ans = [[2 for i in range(N)]]
    assert (orig_img == ans)
    return print("Success: row of 0\n")


def test_row_blocked():
    orig_img = [[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]]
    orig_img = fill(orig_img, (0,0))
    ans =      [[2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0]]
    assert (orig_img == ans)
    return print("Success: row of 0 with blocking 1\n")


def test_empty_col(N, seed_coords):
    orig_img = [[0] for i in range(N)]
    orig_img = fill(orig_img, seed_coords)
    ans = [[2] for i in range(N)]
    assert (orig_img == ans)
    return print("Success: col of 0\n")


def test_empty_list():
    seed_coords = (0,0)
    orig_img = [[]]
    orig_img = fill(orig_img, (seed_coords))
    ans = [[]]
    assert (orig_img == ans)
    return print("Success: empty 2D list\n")


def test_empty_list_2():
    seed_coords = (0,0)
    orig_img = []
    orig_img = fill(orig_img, (seed_coords))
    ans = []
    assert (orig_img == ans)
    return print("Success: empty 1D list\n")


def test_identity_bottom(n):
    seed_coords = (1,0)
    orig_img=[[0 for x in range(n)] for y in range(n)]
    for i in range(0,n):
        orig_img[i][i] = 1
    orig_img = fill(orig_img, seed_coords)
    ans = [[1,0,0,0,0],
           [2,1,0,0,0],
           [2,2,1,0,0],
           [2,2,2,1,0],
           [2,2,2,2,1]]
    assert orig_img == ans
    return print("Succes: bottom identify matrix\n")


def test_identity_top(n):
    seed_coords = (0,1)
    orig_img=[[0 for x in range(n)] for y in range(n)]
    for i in range(0,n):
        orig_img[i][i] = 1
    orig_img = fill(orig_img, seed_coords)
    ans = [[1,2,2,2,2],
           [0,1,2,2,2],
           [0,0,1,2,2],
           [0,0,0,1,2],
           [0,0,0,0,1]]
    assert orig_img == ans
    return print("Success: upper identity matrix\n")


def negative_seeds():
    img = load_image('data/snake.txt')
    ans = load_image('data/snake.txt')
    seed_coords = (-5,-3)
    img = fill(img, seed_coords, True)
    assert img == ans
    print("Success: negative seed coordinates\n")


def snake_test():
    img = [[0,1,1,1,1,0,0,0,0,1],
           [0,0,1,1,1,0,1,1,0,1],
           [1,0,0,1,0,0,1,1,0,1],
           [1,1,0,1,1,0,1,1,0,1],
           [1,1,0,1,1,0,1,1,0,1],
           [1,1,0,1,1,0,1,1,0,1],
           [1,1,0,0,0,0,1,1,0,1],
           [1,1,1,1,1,1,1,1,0,0]]
    ans = img.copy()
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if ans[i][j] == 0:
                ans[i][j] = 2
    seed_coords = (0,0)
    comp = fill(img, seed_coords)
    assert comp == ans
    print("Success: snake input\n")


def diff_len():
    img = [[0],
           [0,0],
           [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,0],
           [1,1,0],
           [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,1,0,0,0,0],
           [1,1,1,1,1,0,0,0,0,0]]
    ans = [[2],
           [2,2],
           [1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,2],
           [1,1,2],
           [1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
           [1,1,2,2,2,2],
           [1,1,1,1,1,2,2,2,2,2]]
    seed_coords = (0,0)
    comp = fill(img, seed_coords)
    assert comp == ans
    print("Success: varying length input\n")


def diff_len_neg_seed():
    img = [[0],
           [0,0],
           [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,0],
           [1,1,0],
           [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,1,0,0,0,0],
           [1,1,1,1,1,0,0,0,0,0]]
    ans = [[0],
           [0,0],
           [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,0],
           [1,1,0],
           [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,1,0,0,0,0],
           [1,1,1,1,1,0,0,0,0,0]]
    seed_coords = (-1,2)
    comp = fill(img, seed_coords)
    assert comp == ans
    print("Success: varying length input with negative seed\n")


def diff_len_remaining_zeroes():
    img = [[0],
           [0,0],
           [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,0],
           [1,1,0],
           [1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
           [1,1,0,0,0,0],
           [1,1,1,1,1,0,0,0,0,0]]
    ans = [[2],
           [2,2],
           [1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,2],
           [1,1,2],
           [1,1,2,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0],
           [1,1,2,2,2,2],
           [1,1,1,1,1,2,2,2,2,2]]
    seed_coords = (0,0)
    comp = fill(img, seed_coords)
    assert comp == img
    print("Success: varying length input with leftover zeroes\n")


def diff_len_remaining_zeroes_neg_seed():
    img = [[0],
           [0,0],
           [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,0],
           [1,1,0],
           [1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
           [1,1,0,0,0,0],
           [1,1,1,1,1,0,0,0,0,0]]
    ans = [[0],
           [0,0],
           [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,0],
           [1,1,0],
           [1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
           [1,1,0,0,0,0],
           [1,1,1,1,1,0,0,0,0,0]]
    seed_coords = (-1,-1)
    comp = fill(img, seed_coords)
    assert comp == ans
    print("Success: varying length input with leftover zeroes and negative seed\n")


def connector():
    img = [[0],
           [0,0],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,0],
           [1,1,1,1,1,1,1,1,1,1,0],
           [1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
           [1,1,0,0,0,0],
           [1,1,1,1,1,0,0,0,0,0]]
    ans = [[2],
           [2,2],
           [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,2],
           [1,1,1,1,1,1,1,1,1,1,2],
           [1,1,2,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0],
           [1,1,2,2,2,2],
           [1,1,1,1,1,2,2,2,2,2]]
    seed_coords = (0,0)
    comp = fill(img, seed_coords)
    assert comp == ans
    print("Success: connecting line\n")


test_random_strcoord(30,('a',2))
test_random_floatcoord(30, (0.5, 5))
test_full_0(1000, (0,200))
integer_float_input(100)
test_full_1(500, (5,5))
test_empty_row(20, (0,0))
test_row_blocked()
test_empty_col(20, (0,0))
test_empty_list()
test_empty_list_2()
test_identity_bottom(5)
test_identity_top(5)
snake_test()
diff_len()
diff_len_neg_seed()
diff_len_remaining_zeroes()
diff_len_remaining_zeroes_neg_seed()
connector()
