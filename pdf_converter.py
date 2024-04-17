from pdf2docx import Converter
from pypdf import PdfReader, PdfWriter
import warnings

warnings.filterwarnings("ignore")

class PDFConverter:
    
    def __init__(self, fn):
        self.fn = fn
        
    def toDocx(self):
        try:
            msg = "Success!"
            converted = "%s.docx" % (self.fn.split(".")[0])
            content = Converter(self.fn)
            content.convert(converted, start=0, end=None)
            content.close()
        except Exception as e:
            msg = "Failed, met some error:\n%s" % (e)
        return msg
        
    def toText(self):
        try:
            msg = "Success!"
            converted = "%s.txt" % (self.fn.split(".")[0])
            reader = PdfReader(self.fn)
            for p in range(len(reader.pages)):
                text = "(Page %d)\n\n" % (p + 1)
                text += "%s\n\n" % (reader.pages[p].extract_text())
                with open (converted, "a+") as f:
                    f.write(text)
        except Exception as e:
            msg = "Failed, met some error:\n%s" % (e)
        return msg

    def unlock(self, pswd):
        try:
            msg = "Success!"
            reader = PdfReader(self.fn)
            reader.decrypt(pswd)
            converted = "%s(unlocked).pdf" % (self.fn.split(".")[0])
            writer = PdfWriter()
            for p in range(len(reader.pages)):
                writer.add_page(reader.pages[p])
            with open (converted, "wb") as f:
                writer.write(f)
            writer.close()
        except Exception as e:
            msg = "Failed, met some error:\n%s" % (e)
        return msg

    def merge(self):
        try:
            msg = "Success!"
            writer = PdfWriter()
            converted = "%s/combined.pdf" % ((self.fn)[0].split("/")[0])
            for p in self.fn:
                writer.append(p)
                writer.write(converted)
            writer.close()
        except Exception as e:
            msg = "Failed, met some error:\n%s" % (e)
        return msg