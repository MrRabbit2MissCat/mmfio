from mfio.iolib.excel import Excel
from mfio.iolib.mcsv import Csv
from mfio.utils.download import download_file
from mfio.utils.log import logger
from mfio.utils.print_table import PrintTable

# value_dic = {
#     "sheet1": [[1, 2, 3], [4, 5, 67, 8, 9]],
#     "表格": [[1, 2, 3], [4, 5, 67, 8, 9]],
# }
# Excel.write_openpyxl("a.xlsx", value_dic)

# Csv.write("a.csv",[["asdf","1"],["你好"]])


a = [[1, "asdfasdf", 3], [4, 5, 655555555], [4, 5, 0]]
logger.info("asdf")
PrintTable(a)


download_file(r"https://images.cnblogs.com/cnblogs_com/yunhgu/1999467/t_2107150739571.jpg",
              r"D:\a.png")