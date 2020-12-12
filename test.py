from flask import Flask, redirect, url_for, request, render_template
import re
import string
import pandas as pd
import nltk
from nltk.corpus import stopwords

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("test.html")

def clean_text(text):
    text = text.lower().strip()
    text = " ".join([w for w in text.split() if len(w) > 2])
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

def predict_rate(df,word_all_rate,word_rate_list,rate):
    df["comment"] = df["comment"].apply(tokenizer.tokenize)
    df["comment"] = df["comment"].apply(remove_stopwords)
    exploded = df.explode('comment')
    
    
    for i in range (10):
        exploded[i+1] = exploded['comment'].apply(
        lambda x: naive_bayes(x,word_all_rate,word_rate_list[i-1],1))
    
    

    for i in df.index:
        ff=exploded.loc[exploded.index == i].prod()
        max_ = -1
        position=0
        for j,k in zip(range(10), rate):
            df.loc[df.index == i,k]=ff[j+1]
            if max_<ff[j+1]:
                max_=ff[j+1]
                position=j+1
        df.loc[df.index == i,"predict"] = position
    
    return df

def naive_bayes(text,word_all_rate,word_rate_1,smoothing):
    if smoothing != True:
        if (text in word_all_rate) & (text in word_rate_1):
            return word_rate_1[text]/word_rate_1.size
        else: 
            return 0
    else:
        if (text in word_all_rate) & (text in word_rate_1):
            return (word_rate_1[text]+1)/(word_rate_1.size+10)

        else:
            return 1/(word_rate_1.size+10)


def remove_stopwords(word_tokens):
    stop_words = set(stopwords.words('english')) 
    filtered_sentence = [w for w in word_tokens if not w in stop_words] 

    filtered_sentence = [] 

    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w) 
            
    return filtered_sentence

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')

def convert_pd_seriest(df):
    df=df.set_index("words")
    df=df.T
    df=df.iloc[0]
    return df

word_all_rate = pd.read_csv("./dictionary/word_all_rate.csv")
word_rate_1 = pd.read_csv("./dictionary/word_rate_1.csv")
word_rate_2 = pd.read_csv("./dictionary/word_rate_2.csv")
word_rate_3 = pd.read_csv("./dictionary/word_rate_3.csv")
word_rate_4 = pd.read_csv("./dictionary/word_rate_4.csv")
word_rate_5 = pd.read_csv("./dictionary/word_rate_5.csv")
word_rate_6 = pd.read_csv("./dictionary/word_rate_6.csv")
word_rate_7 = pd.read_csv("./dictionary/word_rate_7.csv")
word_rate_8 = pd.read_csv("./dictionary/word_rate_8.csv")
word_rate_9 = pd.read_csv("./dictionary/word_rate_9.csv")
word_rate_10 = pd.read_csv("./dictionary/word_rate_10.csv")

word_all_rate = convert_pd_seriest(word_all_rate)
word_rate_1=convert_pd_seriest(word_rate_1)
word_rate_2=convert_pd_seriest(word_rate_2)
word_rate_3=convert_pd_seriest(word_rate_3)
word_rate_4=convert_pd_seriest(word_rate_4)
word_rate_5=convert_pd_seriest(word_rate_5)
word_rate_6=convert_pd_seriest(word_rate_6)
word_rate_7=convert_pd_seriest(word_rate_7)
word_rate_8=convert_pd_seriest(word_rate_8)
word_rate_9=convert_pd_seriest(word_rate_9)
word_rate_10=convert_pd_seriest(word_rate_10)


word_rate_list=[word_rate_1,word_rate_2,word_rate_3,word_rate_4,word_rate_5,word_rate_6,word_rate_7,word_rate_8
               ,word_rate_9,word_rate_10]


rate = ["1_","2_","3_","4_","5_","6_","7_","8_","9_","10_","predict"]


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    result= ""
    if request.method == 'POST':
        comment = request.form['comment']
    else:
        comment = request.args.get('comment')
    result = ' '
    if comment:
        df = pd.DataFrame([[comment]] , columns = ['comment']) 
        result = predict_rate(df,word_all_rate,word_rate_list,rate)
        result=result["predict"][0]
    else:
        comment = ''
    
    return render_template('test.html', rating=result)

if __name__ == '__main__':
    app.run(debug=True)