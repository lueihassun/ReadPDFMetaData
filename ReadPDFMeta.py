from PyPDF4 import PdfFileReader


def get_meta(filename):

    with open(filename, 'rb') as pdf:
        pdf_file = PdfFileReader(pdf)
        doc_info = pdf_file.getDocumentInfo()
        pdfoutput = f'[*] PDF MetaData For: {str(filename)}'
        for meta_item in doc_info:
            pdfoutput += f'\n [+] {meta_item}: {doc_info[meta_item]}'
    return pdfoutput


# Für Nutzung über Konsole, mit Parameter -F
#
# def main():
#     parser = optparse.OptionParser('usage %prog "+ "-F <PDF file name>')
#     parser.add_option('-F', dest='filename', type='string', help='specify PDF file name')
#     (options, args) = parser.parse_args()
#     filename = options.filename
#     if filename is None:
#         print(parser.usage)
#         exit(0)
#     else:
#         print_meta(filename)
#
#
# if __name__ == '__main__':
#     main()

print(get_meta('document.pdf'))
