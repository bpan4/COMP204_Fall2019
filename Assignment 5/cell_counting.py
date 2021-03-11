#Belle Pan
#260839939

import skimage.io as io
import numpy as np
from skimage.color import rgb2gray
from skimage import filters
    
# This function is provided to you. You will need to call it.
# You should not need to modify it.
def seedfill(im, seed_row, seed_col, fill_color, bckg):
    """
    im: The image on which to perform the seedfill algorithm
    seed_row and seed_col: position of the seed pixel
    fill_color: Color for the fill
    bckg: Color of the background, to be filled
    Returns: Number of pixels filled
    Behavior: Modifies image by performing seedfill
    """
    size=0  # keep track of patch size
    n_row, n_col = im.shape
    front={(seed_row,seed_col)}  # initial front
    while len(front)>0:
        r, c = front.pop()  # remove an element from front
        if im[r, c]==bckg: 
            im[r, c]=fill_color  # color the pixel
            size+=1
            # look at all neighbors
            for i in range(max(0,r-1), min(n_row,r+2)):
                for j in range(max(0,c-1),min(n_col,c+2)):
                    # if background, add to front
                    if im[i,j]==bckg and\
                       (i,j) not in front:
                        front.add((i,j))
    return size


# QUESTION 4
def fill_cells(edge_image):
    """
    Args:
        edge_image: A black-and-white image, with black background and
                    white edges
    Returns: A new image where each close region is filled with a different
             grayscale value
    """
    fill_image = edge_image.copy()
    nrow, ncol = fill_image.shape
    fill_colour = 0.5
    seedfill(fill_image, 0, 0, 0.1, 0.0)
    for row in range(nrow):
        for col in range(ncol):
            if fill_image[row, col] == 0.0:
                seedfill(fill_image, row, col, fill_colour, 0.0)
                fill_colour += 0.001
    return fill_image
                
#    return None # REMOVE THIS WHEN YOU'RE DONE

# QUESTION 5
def classify_cells(original_image, labeled_image, \
                   min_size=1000, max_size=5000, \
                   infected_grayscale=0.5, min_infected_percentage=0.02):
    """
    Args:
        original_image: A graytone image
        labeled_image: A graytone image, with each closed region colored
                       with a different grayscal value
        min_size, max_size: The min and max size of a region to be called a cell
        infected_grayscale: Maximum grayscale value for a pixel to be called infected
        min_infected_percentage: Smallest fraction of dark pixels needed to call a cell infected
    Returns: A tuple of two sets, containing the grayscale values of cells 
             that are infected and not infected
    """
    all_greyscale_values = set()
    for row in range(nrow):
        for col in range(ncol):
            all_greyscale_values.add(labeled_image[row, col]) #adds all greyscale values in the image to the set
    infected = set()
    not_infected = set()
    for value in all_greyscale_values:
        count = 0
        infected_count = 0
        for row in range(nrow):
            for col in range(ncol):     
                if labeled_image[row, col] == value:
                    count += 1 #keeps track of number of pixels with the same greyscale value
                    if original_image[row, col] <= infected_grayscale:
                        infected_count += 1 #keeps track of number of pixels that are within the infected greyscale value
        if count >= min_size and count <= max_size: #if the area with the same greyscale value is within the given size to be considered a cell
            if (count*min_infected_percentage) > infected_count:
                not_infected.add(value)
            elif (count*min_infected_percentage) <= infected_count:
                infected.add(value)
    return(infected, not_infected)
        
#    return None # REMOVE THIS WHEN YOU'RE DONE

# QUESTION 6
def annotate_image(color_image, labeled_image, infected, not_infected):
    """
    Args:
        color_image: A color image
        labeled_image: A graytone image, with each closed region colored
                       with a different grayscal value
        infected: A set of graytone values of infected cells
        not_infected: A set of graytone values of non-infcted cells
    Returns: A color image, with infected cells highlighted in red
             and non-infected cells highlighted in green
    """    
    new_colour_image = color_image.copy()
    
    for row in range(nrow):
        for col in range(ncol):
            
            if labeled_image[row, col] in infected:
                
                if row-1 in range(nrow):
                    if labeled_image[row-1, col] == 1.0:
                        new_colour_image[row, col] = [255, 0, 0]
                    if col-1 in range(nrow):
                        if labeled_image[row, col-1] == 1.0:
                            new_colour_image[row, col] = [255, 0, 0]
                        elif labeled_image[row-1, col-1] == 1.0:
                            new_colour_image[row, col] = [255, 0, 0]
                    if col+1 in range(nrow):
                        if labeled_image[row, col+1] == 1.0:
                            new_colour_image[row, col] = [255, 0, 0]
                        elif labeled_image[row-1, col+1]<0.5:
                            new_colour_image[row, col] = [255, 0, 0]
                            
                            
                if row+1 in range(nrow):
                    if labeled_image[row+1, col] == 1.0:
                        new_colour_image[row, col] = [255, 0, 0]
                    if col+1 in range(ncol):
                        if labeled_image[row, col+1] == 1.0:
                            new_colour_image[row, col] = [255, 0, 0]
                        elif labeled_image[row+1, col+1] == 1.0:
                            new_colour_image[row, col] = [255, 0, 0]
                    if col-1 in range(ncol):
                        if labeled_image[row, col-1] == 1.0:
                            new_colour_image[row, col] = [255, 0, 0]
                        elif labeled_image[row+1, col-1] == 1.0:
                            new_colour_image[row, col] = [255, 0, 0]
                            
            elif labeled_image[row, col] in not_infected:
                if row-1 in range(nrow):
                    if labeled_image[row-1, col] == 1.0:
                        new_colour_image[row, col] = [0, 255, 0]
                    if col-1 in range(nrow):
                        if labeled_image[row, col-1] == 1.0:
                            new_colour_image[row, col] = [0, 255, 0]
                        elif labeled_image[row-1, col-1] == 1.0:
                            new_colour_image[row, col] = [0, 255, 0]
                    if col+1 in range(nrow):
                        if labeled_image[row, col+1] == 1.0:
                            new_colour_image[row, col] = [0, 255, 0]
                        elif labeled_image[row-1, col+1]<0.5:
                            new_colour_image[row, col] = [0, 255, 0]
                if row+1 in range(nrow):
                    if labeled_image[row+1, col] == 1.0:
                        new_colour_image[row, col] = [0, 255, 0]
                    if col+1 in range(ncol):
                        if labeled_image[row, col+1] == 1.0:
                            new_colour_image[row, col] = [0, 255, 0]
                        elif labeled_image[row+1, col+1] == 1.0:
                            new_colour_image[row, col] = [0, 255, 0]
                    if col-1 in range(ncol):
                        if labeled_image[row, col-1] == 1.0:
                            new_colour_image[row, col] = [0, 255, 0]
                        elif labeled_image[row+1, col-1] == 1.0:
                            new_colour_image[row, col] = [0, 255, 0]
    return new_colour_image
    
#    return None # REMOVE THIS WHEN YOU'RE DONE

if __name__ == "__main__":  # do not remove this line   
    
    # QUESTION 1: WRITE YOUR CODE HERE
    
    image = io.imread ("malaria-1.jpg")
    grey_image = rgb2gray(image)
    grey_sobel= filters.sobel(grey_image)
    io.imsave ("Q1_Sobel.jpg", grey_sobel)
    
    # QUESTION 2: WRITE YOUR CODE HERE
    
    black_and_white = np.where(grey_sobel>0.05, 1.0, 0)
    io.imsave("Q2_Sobel_T_0.05.jpg", black_and_white)
    
    # QUESTION 3: WRITE YOUR CODE HERE
    
    nrow, ncol, colour = image.shape
    for row in range(nrow):
        for col in range(ncol):
            if (grey_image[row, col])<0.5:
                black_and_white[row, col] = 0.0
            else:
                if row-1 in range(nrow):
                    if grey_image[row-1, col]<0.5:
                        black_and_white[row, col] = 0.0
                    if col-1 in range(nrow):
                        if grey_image[row, col-1]<0.5:
                            black_and_white[row, col] = 0.0
                        elif grey_image[row-1, col-1]<0.5:
                            black_and_white[row, col] = 0.0
                    if col+1 in range(nrow):
                        if grey_image[row, col+1]<0.5:
                            black_and_white[row, col] = 0.0
                        elif grey_image[row-1, col+1]<0.5:
                            black_and_white[row, col] = 0.0
                            
                if row+1 in range(nrow):
                    if grey_image[row+1, col]<0.5:
                        black_and_white[row, col] = 0.0
                    if col+1 in range(ncol):
                        if grey_image[row, col+1]<0.5:
                            black_and_white[row, col] = 0.0
                        elif grey_image[row+1, col+1]<0.5:
                            black_and_white[row, col] = 0.0
                    if col-1 in range(ncol):
                        if grey_image[row, col-1]<0.5:
                            black_and_white[row, col] = 0.0
                        elif grey_image[row+1, col-1]<0.5:
                            black_and_white[row, col] = 0.0
    io.imsave("Q3_Sobel_T_0.05_clean.jpg", black_and_white)
    
    # QUESTION 4: WRITE YOUR CODE CALLING THE FILL_CELLS FUNCTION HERE
    
    fill_cell_image = fill_cells(black_and_white)
    io.imsave("Q4_Sobel_T_0.05_clean_filled.jpg", fill_cell_image)
    
    # QUESTION 5: WRITE YOUR CODE CALLING THE CLASSIFY_CELLS FUNCTION HERE
    
    infected, not_infected = classify_cells(grey_image, fill_cell_image)
    
    # QUESTION 6: WRITE YOUR CODE CALLING THE ANNOTATE_IMAGE FUNCTION HERE
    
    annotated_image = annotate_image(image, fill_cell_image, infected, not_infected)
    io.imsave("Q6_annotated.jpg", annotated_image)
    

