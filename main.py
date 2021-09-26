from cnsenti import *

def main():
    senti = Sentiment()
    emotion = Emotion()
    with open("test.txt","r") as f:
        test_text = f.read() 
        sentiResult = senti.sentiment_count(test_text)
        emotionResult = emotion.emotion_count(test_text)
        print(sentiResult)
        print(emotionResult)

if __name__ == "__main__":
    main()
