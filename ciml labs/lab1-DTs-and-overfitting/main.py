from data import loadTextDataBinary

def main():
    # Load the data
    X, Y, dictionary = loadTextDataBinary('data/sentiment.de')
    print(dictionary)
    print("Hello from lab1-dts-and-overfitting!")


if __name__ == "__main__":
    main()
