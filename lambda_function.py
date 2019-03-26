import tabula
import pandas

# define class
class PdfReader:
    def __init__(self, filename):
        self.filename = filename
        self.filetype = filename.rpartition('.')[-1]
        self.reader()

    def reader(self):
        if self.filetype == 'pdf':
            self.result = tabula.read_pdf(self.filename, pages = 'all')
        if self.filetype == 'csv'
            self.result = pandas.read_csv(self.filename)
    

def lambda_handler(event):
    # Get data
    r1 = PdfReader(event)

    print(r1.result)

#test file on my local - PDF
lambda_handler('C:/Users/william.snodgrass/Documents/Provider_Sanction/StateList/IdahoMedicaidExclusionList.pdf')

