from site_loader import get_pdf

analysis = {
    'url': 'https://metaphor.ethz.ch/x/2018/hs/401-1261-07L/',
    'link_text_pattern': 'Serie ',
    'file_path': 'C:\\Users\\Jonas\\Documents\\Studium\\Analysis I\\Serien\\',
}

lin_alg = {
    'url': 'http://metaphor.ethz.ch/x/2018/hs/401-1151-00L/',
    'link_text_pattern': 'Serie ',
    'file_path': 'C:\\Users\\Jonas\\Documents\\Studium\\Lineare Algebra I\\Serien\\',
}

# physik = {
#     'url': 'http://metaphor.ethz.ch/x/2018/hs/401-1151-00L/',
#     'link_text_pattern': 'Serie ',
#     'file_path': 'C:\\Users\\Jonas\\Documents\\Studium\\Lineare Algebra I\\Serien\\',
# }


get_pdf(analysis)
