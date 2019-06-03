# TO-DO: Complete the selection_sort() function below

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        print(smallest_index)
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
               smallest_index = j

        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

        # TO-DO: swap




    print(arr)
    return arr



array_test = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
selection_sort(array_test)
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


#     class Book:
# 	def __init__(self, t, a, g)
# 		self.title = t
# 		self.author = a
# 		self.genre = g

# def insertion_sort(books):
# 	for i in range(1, len(books)):
# 		temp = books[i]
# 		j = i

# 		while j > 0 and temp.genre < books[j - 1].genre:
# 			books[j] = books[j - 1] # scoot books over to make room
# 			j -= 1

# 		# j is now the index of where we want to place the book
# 		books[j] = temp

# 	return books
