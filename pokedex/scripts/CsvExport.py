import csv
from pathlib import Path
from Constants import Constants


class CsvExport:
  """
  Class responsible for define the csv export method.
  """
  def csv_export(file_name, content_from):
    """
    Method for export csv files.

    Args:
    file_name (string): name of the file that will
    be created, containing it's extension.
    content_from (function): expects the return of functions 
    with a list containing the rows that will be written in the 
    file created.

    Verifies if the file already exists before it's creation.
    """
    if (Path(f'{Constants.ROOT_PATH()}/../{file_name}').is_file()) == False:
      with open(f'{Constants.ROOT_PATH()}/../{file_name}', 'w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['ID', 'NAME', 'IMAGE', 'TYPE'])
        for row in content_from:
          writer.writerow(row)
