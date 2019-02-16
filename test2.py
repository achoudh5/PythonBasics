import argparse
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help= "first number")
    parser.add_argument("number2", help="second number")
    parser.add_argument("operation", help="operation")

    #args= parser.parse_args()

    args= parser.parse_args()
    print (args.number1)
    print (args.number2)
    print (args.operation)