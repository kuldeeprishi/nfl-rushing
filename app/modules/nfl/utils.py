def get_paginated_data(data, page, per_page):
    '''Paginates a array of data based on given page and per_page args'''
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    return data[start_index:end_index]
