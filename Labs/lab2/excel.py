import pyexcel

a_list_of_dictionaries = [
    {
        'title': 'SU25',
        'link': 'http://google.com.vn'
    },
    {
        'title': 'SU25-2',
        'link': 'http://google.com.vn/2'
    },
    {
        'title': 'SU25-3',
        'link': 'http://google.com.vn/3'
    },
]

pyexcel.save_as(records = a_list_of_dictionaries, dest_file_name = 'excel_py.xlsx')
