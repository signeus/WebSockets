# -*- coding: utf-8 -*-
from modules.services.interfaces.i_service import IService
import xlrd
import base64
from xlrd.sheet import ctype_text

class ReadXlsService (IService):
    def __init__(self, core, parameters):
        super(ReadXlsService, self).__init__(core, parameters)

    def run(self):
        data = self.parameters.get("data", '')
        format = data[:data.rfind(",")]
        includedHeader = self.parameters.get("headers", True)
        data = data[data.find(",") + 1:]
        decodeFile = base64.b64decode(data)
        #book = xlrd.open_workbook(file_contents=decodeFile.read())
        book = xlrd.open_workbook(file_contents=decodeFile)
        worksheet = book.sheet_by_index(0)
        dic = {}
        num_cols = worksheet.ncols
        for row_idx in range(0, worksheet.nrows): # Iterate through rows
            if row_idx == 0 and includedHeader:
                continue
            for col_idx in range(0, num_cols):  # Iterate through columns
                if col_idx > 1:
                    break
                cell_obj = worksheet.cell(row_idx, col_idx)  # Get cell object by row, col
                if col_idx == 1:
                    dic.update({cell_obj: worksheet.cell(row_idx, col_idx - 1)}) #Create dictionary, key: email, value = name
        #TODO check if exists the emails in database. save like as "subscrited or invited to the community"