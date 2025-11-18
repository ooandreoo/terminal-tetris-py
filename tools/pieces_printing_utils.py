def get_piece_0_matrix():
    return [
        ["  ","  ","  "],
        ["  ","# ","  "],
        ["# ","# ","# "],
        ["  ","  ","  "]]

def get_piece_1_matrix():
    return [
        ["  ","  ","  "],
        ["  ","# ","# "],
        ["  ","# ","# "],
        ["  ","  ","  "]]

def get_piece_2_matrix():
    return [
        ["  ","  ","  "],
        ["  ","# ","  "],
        ["  ","# ","# "],
        ["  ","  ","# "]]

def get_piece_3_matrix():
    return [
        ["  ","  ","  "],
        ["  ","  ","# "],
        ["  ","# ","# "],
        ["  ","# ","  "]]

def get_piece_4_matrix():
    return [
        ["  ","# ","  "],
        ["  ","# ","  "],
        ["  ","# ","  "],
        ["  ","# ","  "]]

def get_piece_5_matrix():
    return [
        ["  ","  ","  "],
        ["# ","# ","  "],
        ["  ","# ","  "],
        ["  ","# ","  "]]

def get_piece_6_matrix():
    return [
        ["  ","  ","  "],
        ["  ","# ","# "],
        ["  ","# ","  "],
        ["  ","# ","  "]]

def get_blank_space_matrix():
    return [
        ["  "],
        ["  "],
        ["  "],
        ["  "]]

def join_matrixes_horizontally(a,b):
    result = []
    for index in range(len(a)):
        row = list()
        row.extend(a[index])
        row.extend(b[index])
        result.append(row)
    return result

def retrieve_matrix_by_type(type):
    if(type==0):
        return get_piece_0_matrix()
    elif(type==1):
        return get_piece_1_matrix()
    elif(type==2):
        return get_piece_2_matrix()
    elif(type==3):
        return get_piece_3_matrix()
    elif(type==4):
        return get_piece_4_matrix()
    elif(type==5):
        return get_piece_5_matrix()
    elif(type==6):
        return get_piece_6_matrix()
    elif(type==None):
        return get_blank_space_matrix()

def get_matrix_to_print(next, switch):
    printing_matrix = []
    next_matrix = retrieve_matrix_by_type(next)
    switch_matrix = retrieve_matrix_by_type(switch)
    blank = get_blank_space_matrix()
    printing_matrix = join_matrixes_horizontally(blank,blank)
    printing_matrix = join_matrixes_horizontally(printing_matrix,blank)
    printing_matrix = join_matrixes_horizontally(printing_matrix,next_matrix)
    printing_matrix = join_matrixes_horizontally(printing_matrix,blank)
    printing_matrix = join_matrixes_horizontally(printing_matrix,blank)
    printing_matrix = join_matrixes_horizontally(printing_matrix,blank)
    printing_matrix = join_matrixes_horizontally(printing_matrix,blank)
    printing_matrix = join_matrixes_horizontally(printing_matrix,blank)
    printing_matrix = join_matrixes_horizontally(printing_matrix,blank)
    printing_matrix = join_matrixes_horizontally(printing_matrix,switch_matrix)
    return printing_matrix
