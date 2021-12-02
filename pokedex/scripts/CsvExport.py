import csv
from Constants import Constants

class CsvExport:
  """
  Class responsible for...
  """
  def csv_export(file_name, content_from):
    with open(f'{Constants.ROOT_PATH()}/../{file_name}', 'w', encoding='UTF-8', newline='') as f:
      writer = csv.writer(f, delimiter=';')
      writer.writerow(['ID', 'NAME', 'IMAGE', 'TYPE'])
      for row in content_from:
        writer.writerow(row)
