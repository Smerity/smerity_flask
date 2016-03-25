# TayAndYou - broken well before human contact

I'll keep this brief as I don't think it's actually worth a great deal of attention.

Humans have the tendency to imbue machine learning models with more intelligence than they deserve, especially if it involves the magic phrases of artificial intelligence, deep learning, or neural networks.
TayAndYou is a perfect example of this.

For me and many of my friends who work in the field of machine learning, we generally don't appreciate the hype.
Hype throws expectations so far out from reality that they're at escape velocity.
This will not help us understand how people become radicalized.
This is not a grand experiment about the human condition.
This is a marketing experiment that was particularly poorly executed.

Summary:

+ Conversational models are not new and there is no details on new tech in TayAndYou
+ The training data that TayAndYou bot used was already poisonous and many of TayAndYou's worst tweets were historical, not learned after activation (i.e. was at best overfitting to training data)
+ How the media did not realize that it copy pasted tweets I've no clue
+ Sanity checks were not added to prevent trivial exploits
+ Don't pump out 96,000 tweets in under 24 hours unless you're confident in the quality of output
+ Hype hype hype hype

## Conversational models have history

### Ancient history

Language models for producing conversational agents aren't a particularly new concept.

[Mark V. Shaney](https://en.wikipedia.org/wiki/Mark_V._Shaney) was an elegant play on this many decades ago.
This model was based upon word level Markov chains, sampling the next word based upon how frequently it was seen following the previous N.

Given the phrase `once upon a <blank>` it would sample `time` with high probability, given that the phrase was highly common.

As this bot first played with humans in 1984, it had the advantage that no-one expected replies on Usenet to be automated.
Indeed, many thought this was just a strange man spouting the occasional beautiful annecdote of accidental wisdom.

> I hope that there are sour apples in every bushel.

If you're interested in more about Mark V. Shaney's exploits, I heartily recommend this [Scientific American article from 1989](https://www.clear.rice.edu/comp200/09fall/textriff/sci_am_paper.htm).

I could continue on to CleverBot and other such items but I'm going to do a far longer jump to...

### Modern history

In more recent years, language models have moved on to new tech.
The one most likely at the heart of TayAndYou are recurrent neural networks (RNNs).
For a detailed discussion, I'd recommend Karpathy's [Unreasonable Effectiveness of Recurrent Neural Networks
](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) and Olah's more technical [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/).

RNNs, most frequently long short term memory (LSTM) units, perform well at a variety of tasks, including machine translation and language modeling.

Given that TayAndYou has no specific details on the model, we're left to guesstimate.
It is likely that Microsoft's bot was similar to Google's [Neural Conversational Model](http://arxiv.org/pdf/1506.05869.pdf) (Vinyals and Le).
An RNN is fed with the relevant context, in TayAndYou's case the previous tweet, and then produces words until it hits and end of sequence character.

Google trained their model on a variety of text domains with varying success.
After being supplied an IT help desk corpus for example it acts like a distracted pro-Windows troubleshooter.

> **Machine:** could you please let me know what is
the operating system you are using ?  
> **Human:** linux  
> ...  
> **Machine:** is it a windows machine ?  
> **Machine:** we have linux on your machine .  
> **Machine:** is it windows xp or windows 7 ?  
> **Human:** i am using linux  

Admittedly it tells the human to run `sudo apt-get update` then `sudo apt-get upgrade` later so we'll forgive the poor bot the Windows bias.

Whilst Google's work was a far more constrained experiment - they didn't throw Twitter or trolls at it - the Google conversational model still caused a stir.
Why?
They fed it [movie and television show subtitles](http://www.opensubtitles.org/) and asked it fairly provocative questions.

> **Human:** what is the purpose of existence ?  
> **Machine:** to find out what happens when we get to the planet earth .

> **Human:** what is immoral ?  
> **Machine:** the fact that you have a child .

The media had a field day, all the time neglecting to mention the unfortunate truth that it was randomly generating what is in essence movie quotes rather than actually conjecturing on our death and damnation at a deeper level.
I guess one drives more page views?

_Special note:_ no, it didn't magically produce consciousness.
I never thought I'd need to say this but it's not an infrequent question, even amongst ML/AI meetups in SF/SV.
This is an entirely different arena of hype - one I'm not going into here - but the short summary is two layers of 4096 dimensionality LSTM units does not intelligence make.

## The major flaw of TayAndYou: the training data

Assume the TayAndYou bot never tried to learn from the conversations it was experiencing.
Would that solve the eventual decline into Godwin's law?
No, not if the training data was flawed.

It perfectly replicated responses to statements it had seen perfectly.
The text is modified, indicating that the model was overfitting strongly.

At first this response appears witty:

![](https://i.imgur.com/PPnCHnf.jpg)

until you realize that it's literally a copycat from a month ago...

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/child0besity">@child0besity</a> <a href="https://twitter.com/clmazin">@clmazin</a> Disagree. Ted Cruz would never have been satisfied with destroying the lives of only 5 innocent people.</p>&mdash; Merylnet (@merylnet) <a href="https://twitter.com/merylnet/status/703079627288260608">February 26, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Analyzing many of the responses that got the most attention, either for being intelligent or offensive, you'll likely find that most of them are [almost exact repeats from the past](https://twitter.com/Queeeten/status/703049861214547968).

<!--
It's not the first time that overfitting has occurred.
Indeed, if it's a common phrase, overfitting is exactly what it should do.

Humans can imbue intelligence into anything they want.
It's likely related to the reason we feel sympathy when seeing a basketball slowly deflate.

For image captioning models, it's not infrequent to see a model look at an image and produce a sentence that is _exactly the same_ as the model had seen during training.
-->

## Sanity flaws

Was implementing a filter for swearing out of scope..?
Maybe at least filter anything that starts discussing Hitler.


## Hype