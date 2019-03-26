import tabula

class PdfReader:
    def __init__(self, filename):
        self.filename = filename
        self.filetype = filename.rpartition('.')[-1]
        self.pdf_reader()

    def pdf_reader(self):
        if self.filetype == 'pdf':
            self.result = tabula.read_pdf(self.filename, pages = 'all')

def lambda_handler(event):
    # Get data
    r1 = PdfReader(event)

    print(r1.result)

lambda_handler('C:/Users/william.snodgrass/Documents/Provider_Sanction/StateList/IdahoMedicaidExclusionList.pdf')

