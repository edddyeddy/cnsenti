from cnsenti import *

def main():
    senti = Sentiment()
    test_text= '我好开心啊，非常非常非常高兴！今天我得了一百分，我很兴奋开心，愉快，开心'
    result = senti.sentiment_count(test_text)
    print(result)

if __name__ == "__main__":
    main()