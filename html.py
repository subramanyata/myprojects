
# coding: utf-8



from boilerpipe.extract import Extractor


def extracttextfromhtml(filename):
    extractor = Extractor(extractor='KeepEverythingExtractor', html=filename)
    extracted_text = extractor.getText()
    return extracted_text

