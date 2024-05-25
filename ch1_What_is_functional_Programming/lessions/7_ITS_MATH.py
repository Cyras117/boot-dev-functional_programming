def get_median_font_size(font_sizes):

    if len(font_sizes) <= 0 :
        return None
    
    sorted_fonts = sorted(font_sizes)
    middle_index = (len(sorted_fonts)//2)
    
    if len(sorted_fonts) % 2 == 0:
        return (sorted_fonts[middle_index-1]+sorted_fonts[middle_index])/2

    return sorted_fonts[middle_index]
