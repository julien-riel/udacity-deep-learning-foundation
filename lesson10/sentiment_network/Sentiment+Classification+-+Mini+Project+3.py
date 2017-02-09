
# coding: utf-8

# # Sentiment Classification & How To "Frame Problems" for a Neural Network
# 
# by Andrew Trask
# 
# - **Twitter**: @iamtrask
# - **Blog**: http://iamtrask.github.io

# ### What You Should Already Know
# 
# - neural networks, forward and back-propagation
# - stochastic gradient descent
# - mean squared error
# - and train/test splits
# 
# ### Where to Get Help if You Need it
# - Re-watch previous Udacity Lectures
# - Leverage the recommended Course Reading Material - [Grokking Deep Learning](https://www.manning.com/books/grokking-deep-learning) (40% Off: **traskud17**)
# - Shoot me a tweet @iamtrask
# 
# 
# ### Tutorial Outline:
# 
# - Intro: The Importance of "Framing a Problem"
# 
# 
# - Curate a Dataset
# - Developing a "Predictive Theory"
# - **PROJECT 1**: Quick Theory Validation
# 
# 
# - Transforming Text to Numbers
# - **PROJECT 2**: Creating the Input/Output Data
# 
# 
# - Putting it all together in a Neural Network
# - **PROJECT 3**: Building our Neural Network
# 
# 
# - Understanding Neural Noise
# - **PROJECT 4**: Making Learning Faster by Reducing Noise
# 
# 
# - Analyzing Inefficiencies in our Network
# - **PROJECT 5**: Making our Network Train and Run Faster
# 
# 
# - Further Noise Reduction
# - **PROJECT 6**: Reducing Noise by Strategically Reducing the Vocabulary
# 
# 
# - Analysis: What's going on in the weights?

# # Lesson: Curate a Dataset

# In[1]:

def pretty_print_review_and_label(i):
    print(labels[i] + "\t:\t" + reviews[i][:80] + "...")

g = open('reviews.txt','r') # What we know!
reviews = list(map(lambda x:x[:-1],g.readlines()))
g.close()

g = open('labels.txt','r') # What we WANT to know!
labels = list(map(lambda x:x[:-1].upper(),g.readlines()))
g.close()


# In[2]:

len(reviews)


# In[5]:

reviews[0]


# In[6]:

labels[0]


# # Lesson: Develop a Predictive Theory

# In[7]:

print("labels.txt \t : \t reviews.txt\n")
pretty_print_review_and_label(2137)
pretty_print_review_and_label(12816)
pretty_print_review_and_label(6267)
pretty_print_review_and_label(21934)
pretty_print_review_and_label(5297)
pretty_print_review_and_label(4998)


# # Project 1: Quick Theory Validation

# In[9]:

from collections import Counter
import numpy as np


# In[10]:

positive_counts = Counter()
negative_counts = Counter()
total_counts = Counter()


# In[11]:

for i in range(len(reviews)):
    if(labels[i] == 'POSITIVE'):
        for word in reviews[i].split(" "):
            positive_counts[word] += 1
            total_counts[word] += 1
    else:
        for word in reviews[i].split(" "):
            negative_counts[word] += 1
            total_counts[word] += 1


# In[12]:

positive_counts.most_common()


# In[20]:

pos_neg_ratios = Counter()

for term,cnt in list(total_counts.most_common()):
    if(cnt > 100):
        pos_neg_ratio = positive_counts[term] / float(negative_counts[term]+1)
        pos_neg_ratios[term] = pos_neg_ratio

for word,ratio in pos_neg_ratios.most_common():
    if(ratio > 1):
        pos_neg_ratios[word] = np.log(ratio)
    else:
        pos_neg_ratios[word] = -np.log((1 / (ratio+0.01)))


# In[21]:

# words most frequently seen in a review with a "POSITIVE" label
pos_neg_ratios.most_common()


# In[22]:

# words most frequently seen in a review with a "NEGATIVE" label
list(reversed(pos_neg_ratios.most_common()))[0:30]


# # Transforming Text into Numbers

# In[26]:

from IPython.display import Image

review = "This was a horrible, terrible movie."

Image(filename='sentiment_network.png')


# In[27]:

review = "The movie was excellent"

Image(filename='sentiment_network_pos.png')


# # Project 2: Creating the Input/Output Data

# In[74]:

vocab = set(total_counts.keys())
vocab_size = len(vocab)
print(vocab_size)


# In[75]:

list(vocab)


# In[46]:

import numpy as np

layer_0 = np.zeros((1,vocab_size))
layer_0


# In[47]:

from IPython.display import Image
Image(filename='sentiment_network.png')


# In[48]:

word2index = {}

for i,word in enumerate(vocab):
    word2index[word] = i
word2index


# In[49]:

def update_input_layer(review):
    
    global layer_0
    
    # clear out previous state, reset the layer to be all 0s
    layer_0 *= 0
    for word in review.split(" "):
        layer_0[0][word2index[word]] += 1

update_input_layer(reviews[0])


# In[33]:

layer_0


# In[51]:

def get_target_for_label(label):
    if(label == 'POSITIVE'):
        return 1
    else:
        return 0


# In[54]:

labels[0]


# In[52]:

get_target_for_label(labels[0])


# In[55]:

labels[1]


# In[53]:

get_target_for_label(labels[1])


# # Project 3: Building a Neural Network

# - Start with your neural network from the last chapter
# - 3 layer neural network
# - no non-linearity in hidden layer
# - use our functions to create the training data
# - create a "pre_process_data" function to create vocabulary for our training data generating functions
# - modify "train" to train over the entire corpus

# ### Where to Get Help if You Need it
# - Re-watch previous week's Udacity Lectures
# - Chapters 3-5 - [Grokking Deep Learning](https://www.manning.com/books/grokking-deep-learning) - (40% Off: **traskud17**)
