import csv
from pathlib import Path
from Constants import Constants


class CsvExport:
  """
  Class responsible for define the csv export method
  """
  def csv_export(file_name, content_from):
    """
    Method for export csv files.

    Verify if the file already exists before it's creation.
    """
    if (Path(f'{Constants.ROOT_PATH()}/../{file_name}').is_file()) == False:
      with open(f'{Constants.ROOT_PATH()}/../{file_name}', 'w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['ID', 'NAME', 'IMAGE', 'TYPE'])
        for row in content_from:
          writer.writerow(row)
