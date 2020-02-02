from itertools import *  # we need to use the Combinatory logic
# author Arthur Voronkin 02 February 2020


vectors = ['AJID', 'AFGC', 'EJFB', 'EIHC', 'BGHD', 'IOKF', 'INMG', 'JONH', 'JKLG', 'FLMH']  # list of vectors
triangle_full = 0                                                                           # counter of triangles

for vector in vectors:  # taking the first vector
    appearance_in_list = 0  # counter of appearances in list (should be 3 if this is the triangle)
    position_of_vector_in_list = 0  # counter of positions in the list

    for pair in combinations(vector, 2):  # taking a pair of vertices

        for i in vectors:  # taking a vector starting from first

            if pair[0] and pair[1] in i:  # checking if the pair in the vector
                position_of_vector_in_list = vectors.index(i)  # we need to remember the list position of the vector
                appearance_in_list += position_of_vector_in_list  # we have 3 pairs so we need to add all positions

        if appearance_in_list / 3 != position_of_vector_in_list:  # we don't count if all pairs are on the same position
            triangle_full += 1  # we count a triangle if positions in the list are different

print(triangle_full)  # print the total number of triangles
