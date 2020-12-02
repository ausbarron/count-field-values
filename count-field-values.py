#!/usr/bin/python3

import sys
import csv

## Prints error for 0 in field_list ##
def print_field_list_checker ():
    sys.stderr.write("Usage: 0 is not a valid field value\n")
    exit(1)
### USAGE Function: ###

def print_usage ():
    sys.stderr.write("Usage: count-fields-values FIELDS_LIST [CSV_FILE...]\n")
    exit(1)

### MAIN ###
def main():

    argc = len(sys.argv) ##specifies length for argc
    if(argc < 2): ##checks to make sure there is appropiate cmd args
        print_usage()
        
    fields_list = sys.argv[1].split(",") ##splits the field list specified into a list
    counts = {} ##dict for counts
    column = [] ##list for columns

    ## For loop that iterates through fields_list to check for 0 in the field's
    for col in range(0, len(fields_list)):
        x = (int(fields_list[col]))
        if x != 0:
            column.append(x)
        else:
            print_field_list_checker()
    
    ##For loop that iterates through CSV File and adds values to counts                  
    for arg in sys.argv[2:] or [None]:
        ofile = sys.stdin if arg is None else open(arg, 'r')
        csvreader = csv.reader(ofile, delimiter = ",")
        next(csvreader)

        for row in csvreader:
            for i in range(0, len(column)):
                for item in row[column[i]-1]: ## subtract 1
                        if not item in counts:
                            counts[item] = 1
                        else:
                            counts[item] += 1
                            
    ##sorts the values for printing
    sort_keys = sorted(counts.keys(), key=lambda k: counts[k], reverse = True)
    for i in sort_keys:
        print(i, counts[i])

# END MAIN

#RUN MAIN
if __name__ == "__main__":
    main()

#EOF
