


import argparse
import sys
from input_reader import read_csv_file
from database import *
from app import *


def main(argv=None):
    
    app.run()
    read_csv_file('test.csv')
    print_database_content()

    return 0



if __name__ == "__main__":
    main()









  

