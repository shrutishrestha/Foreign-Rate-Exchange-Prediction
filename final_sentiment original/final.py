from initial_new import line
import initial_new as inew

from collections import Counter
import csv
from nltk.stem import PorterStemmer
ps=PorterStemmer()

testing=[]
category_prob={}
dictionary={}
diction={}
dictionary_word_count={}
final_dict={}
total_features=[]
pos=[]
neg=[]
feature_list=[]
with open("positive.csv", 'r') as file:
    posi= list(csv.reader(file))
with open("negative.csv", 'r') as file:
    nega= list(csv.reader(file))
for i in posi:
    po=ps.stem(*i)
    pos.append(po)
for j in nega:
    ne=ps.stem(*j)
    neg.append(ne)


# neg_words=["not","n't"]
neg_words=["not","n't","none","nobody","nothing","neither","nowhere","never"]

total_dict={}
def Naive_Bayes():
    count=0
    for i in range(len(line)):

        processed_tweet=inew.processTweet(line[i][1])
        count=count+1
        positive_class,negative_class=inew.getFeatureVector(processed_tweet,line[i][0])

    # positive_class,negative_class=inew.get_total_classes(positive,negative)
    feature_list=positive_class+negative_class



    diction[0] = negative_class
    diction[1]=positive_class
    for i in diction:
        count = {}
        category_prob[i]=cat_prob(line,i)
          #word prob
        for j in diction[i]:
            count[j] = diction[i].count(j)
        dictionary[i]=count
    #test

    test(text,diction,feature_list,dictionary)

def word_prob(word_value,length,feature_list):

    words_probability = (word_value ) / (int(length) + (len(feature_list)))

    return(words_probability)



with open("overalltweets.csv", 'r') as file:
    line= list(csv.reader(file))

with open("tweetwolabels.csv", 'r') as file:
    text= list(csv.reader(file))


def test(text,diction,feature_list,dictionary):
    county = 0
    for u in range(len(text)):#line

        oneline=text[u][0]


        negation=0
        processed_test_Tweet = inew.processTweet(oneline)
        print("processed_test_Tweet")
        print(processed_test_Tweet)
        words =processed_test_Tweet.split()
        for v in neg_words:
                for i in words:
                    if (v in i):
                        print("negation")
                        print(i)

                        negation=negation+1
                        print(negation)

        if negation>0:
                    count_not = neg_count(processed_test_Tweet)

                    sentence_prob = test_cal(processed_test_Tweet, diction, feature_list, dictionary)

                    if (count_not % 2 == 0):
                        if (sentence_prob[0] > sentence_prob[1]):
                            testing.append(0)
                            print(sentence_prob[0])
                            print(sentence_prob[1])
                            print("negative")
                        elif (sentence_prob[0] < sentence_prob[1]):
                            print(sentence_prob[0])
                            print(sentence_prob[1])
                            testing.append(int(1))
                            print("positive")
                    else:
                        if (sentence_prob[0] > sentence_prob[1]):
                              print(sentence_prob[0])
                              print(sentence_prob[1])
                              testing.append(int(1))
                              print("positive")
                        elif (sentence_prob[0] < sentence_prob[1]):
                              print(sentence_prob[0])
                              print(sentence_prob[1])
                              testing.append(0)
                              print("negative")



        else:
               sentence_prob=test_cal(processed_test_Tweet, diction, feature_list, dictionary)
               if (sentence_prob[0] > sentence_prob[1]):
                    testing.append(0)
                    print("negative")
               elif (sentence_prob[0] < sentence_prob[1]):
                    testing.append(int(1))
                    print("positive")


    calculate()

def test_user(line,diction,feature_list,dictionary):
   # line
        negation = 0
        processed_test_Tweet = inew.processTweet(line)
        words = processed_test_Tweet.split()
        for v in neg_words:
            for i in words:
                if (v in i):
                    negation = negation + 1

        if negation > 0:
            count_not = neg_count(processed_test_Tweet)
            print(count_not)


            sentence_prob = test_cal(processed_test_Tweet, diction, feature_list, dictionary)
            if(count_not%2==0):
                print("m 0")
                print(sentence_prob[0])
                print(sentence_prob[1])
                if (sentence_prob[0] >sentence_prob[1]):
                    testing.append(int(0))
                    print("negative")
                elif (sentence_prob[0] < sentence_prob[1]):
                    print("m not 0")
                    testing.append(int(1))
                    print("positive")
            else:
                if (sentence_prob[0] > sentence_prob[1]):
                    testing.append(int(1))
                    print("positive")
                elif (sentence_prob[0] < sentence_prob[1]):
                    testing.append(0)
                    print("negative")
        else:
            sentence_prob = test_cal(line, diction, feature_list, dictionary)
            if (sentence_prob[0] > sentence_prob[1]):
                testing.append(0)
                print("negative")
            elif (sentence_prob[0] < sentence_prob[1]):
                testing.append(int(1))
                print("positive")

        a = input("again?")
        if (a == "y" or "Y"):
            test_line = input("enter sentence--")
            test_user(test_line, diction, feature_list, dictionary)
        else:
            print("have a.csv good day")


def test_cal(u,diction,feature_list,dictionary):
        oneline = replace_neg(u)

        feature_test=inew.get_test_feature(oneline)

        sentence_prob={}
        for i in diction:

            probability_sentence = 1
            cat=category_prob[i]


            for w in feature_test:

                if w not in feature_list:
                    continue
                else:
                    if w not in diction[i]:
                        word_value = 0

                    elif w in diction[i]:
                        word_value = dictionary[i].get(w)


                    length=len(diction[i])

                    word_probaility=word_prob(word_value,length,feature_list)

                    probability_sentence=probability_sentence*word_probaility


            total_probability=probability_sentence*cat

            sentence_prob[i]=total_probability
        if(((sentence_prob[0]==cat_prob(line,0)) and (sentence_prob[1]==cat_prob(line,1))) or (sentence_prob[0]==0 and sentence_prob[1]==0)):
            pos_count = 0
            neg_count = 0
            for one_word in feature_test:

                if one_word in pos:
                    pos_count = pos_count + 1

                elif one_word in neg:

                    neg_count = neg_count + 1

            sentence_prob[0] = neg_count
            sentence_prob[1] = pos_count
            if (sentence_prob[0] == sentence_prob[1] ):
                print("ulala----------------")

                cnil=0
                main=u.split()
                print(main)
                for p in neg_words:
                    for q in main:

                        if p in q:
                            print("q")
                            print(q)

                            cnil=cnil+1
                            print("cnil")
                            print(cnil)
                if ((cnil!=0) and (cnil%2==0)):
                    sentence_prob[0]=0
                    sentence_prob[1]=1
                elif((cnil!=0) and (cnil%2!=0)):
                    sentence_prob[0]=1
                    sentence_prob[1]=0


        return sentence_prob

def replace_neg(line):
    words = line.split()

    for w in words:
        for n in neg_words:

            if (w.count(n)!=0):

                line = line.replace(n, " ")

                line = " ".join(line.split())
    print(line)
    return line


def cat_prob(line,i):
    count=0
    for one_line in line:
        if int(one_line[0])==i:
            count=count+1
        else:
            continue
    return count/len(line)

#calculating
a=[]
with open("tweetwithlabels.csv", 'r') as file:
    tests_text= list(csv.reader(file))


def calculate():
    tests_original=[]
    tests_original=[]
    counti=0
    for i in tests_text:
        tests_original.append(int(i[0]))

    true_negative=0
    true_positive=0
    false_negative=0
    false_positive=0
    for i in tests_original:

        if(i==1):
            if(tests_original[counti]==testing[counti]):
                true_positive=true_positive+1

            else:
                false_negative=false_negative+1

        if(i==0):
            if(tests_original[counti]==testing[counti]):
                true_negative=true_negative+1

            else:
                false_positive=false_positive+1

        counti = counti + 1
    calculate_prf(true_positive,true_negative,false_positive,false_negative)

    # print("----------------")
    # print(true_positive)
    # print(false_positive)
    # print(false_negative)
    # print(true_negative)
    # precision=true_positive/(true_positive+false_positive)
    # print("precision",precision)
    # recall=true_positive/(true_positive+false_negative)
    # accuracy=(true_positive+true_negative)/(true_positive+false_positive+true_negative+false_negative)
    # print("recall",recall)
    # print("accuracy",accuracy)
    # F=(2*precision*recall)/(precision+recall)
    # print("F",F)

    oo=input("do u want to test Y or N?")
    if(oo=="y" or "Y"):
        test_line=input("enter sentence--")
        test_user(test_line,diction,feature_list,dictionary)
    else:
        print("have a.csv good day")

def calculate_prf(tp,tn,fp,fn):
    pos_precision=tp/(tp+fp)
    neg_precision=tn/(tn+fn)
    pos_recall=tp/(tp+fn)
    neg_recall=tn/(tn+fp)

    print("pos_precision")
    print(pos_precision)
    print("neg_precision")
    print(neg_precision)
    print("pos_recall")
    print(pos_recall)
    print("neg_recall")
    print(neg_recall)
    accuracy=(tp+tn)/(tp+fp+tn+fn)
    print("accuracy")
    print(accuracy)


def neg_count(str):
    aa=0
    for nega in neg_words:
        aa=aa+str.count(nega)


    return aa

Naive_Bayes()





