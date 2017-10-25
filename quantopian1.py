
 Q Research Tutorials (autosaved)
Notebook
Insert
Edit
Run
 Cell Type:Research Memory: 11%

×
Getting started with your notebook
The box below is called a cell. When you write Python code in a cell and run it, the output will appear on the next line.
Run a cell by pressing Shift + Enter or by clicking the  button on the toolbar above.
Run a Sample Cell  More Samples
In [1]:

from quantopian.interactive.data.sentdex import sentiment
from quantopian.interactive.data.sentdex import sentiment
Share
In [2]:

from quantopian.pipeline.filters.morningstar import Q1500US
from quantopian.pipeline.filters.morningstar import Q1500US
In [3]:

type(sentiment)
type(sentiment)
Out[3]:
<class 'blaze.expr.expressions.Field'>
In [4]:

dir(sentiment)
dir(sentiment)
Out[4]:
['apply',
 u'asof_date',
 'cast',
 'count',
 'count_values',
 'distinct',
 'drop_field',
 'dshape',
 'fields',
 'head',
 'isidentical',
 'map',
 'ndim',
 'nelements',
 'nrows',
 'nunique',
 'peek',
 'relabel',
 'sample',
 'schema',
 u'sentiment_signal',
 'shape',
 'shift',
 u'sid',
 'sort',
 u'symbol',
 'tail',
 u'timestamp']
In [10]:

aapl
AAPL = symbols('AAPL').sid
aapl_sentiment = sentiment[ (sentiment.sid==AAPL) ]
In [14]:

.head
aapl_sentiment.head()
Out[14]:
symbol	sentiment_signal	sid	asof_date	timestamp
0	AAPL	6.0	24	2012-10-15	2012-10-16
1	AAPL	2.0	24	2012-10-16	2012-10-17
2	AAPL	6.0	24	2012-10-17	2012-10-18
3	AAPL	6.0	24	2012-10-18	2012-10-19
4	AAPL	6.0	24	2012-10-19	2012-10-20
5	AAPL	6.0	24	2012-10-20	2012-10-21
6	AAPL	1.0	24	2012-10-21	2012-10-22
7	AAPL	-1.0	24	2012-10-22	2012-10-23
8	AAPL	-3.0	24	2012-10-23	2012-10-24
9	AAPL	-1.0	24	2012-10-24	2012-10-25
In [15]:

aapl_sentiment.peek()
Out[15]:
symbol	sentiment_signal	sid	asof_date	timestamp
0	AAPL	6.0	24	2012-10-15	2012-10-16
1	AAPL	2.0	24	2012-10-16	2012-10-17
2	AAPL	6.0	24	2012-10-17	2012-10-18
3	AAPL	6.0	24	2012-10-18	2012-10-19
4	AAPL	6.0	24	2012-10-19	2012-10-20
5	AAPL	6.0	24	2012-10-20	2012-10-21
6	AAPL	1.0	24	2012-10-21	2012-10-22
7	AAPL	-1.0	24	2012-10-22	2012-10-23
8	AAPL	-3.0	24	2012-10-23	2012-10-24
9	AAPL	-1.0	24	2012-10-24	2012-10-25
10	AAPL	-3.0	24	2012-10-25	2012-10-26
In [16]:

import blaze
In [19]:

a
aapl_sentiment = blaze.compute(aapl_sentiment)
In [20]:

aapl_sentiment
type(aapl_sentiment)
Out[20]:
<class 'pandas.core.frame.DataFrame'>
In [21]:

aapl_sentiment.head()
Out[21]:
symbol	sentiment_signal	sid	asof_date	timestamp
0	AAPL	6.0	24	2012-10-15	2012-10-16
1	AAPL	2.0	24	2012-10-16	2012-10-17
2	AAPL	6.0	24	2012-10-17	2012-10-18
3	AAPL	6.0	24	2012-10-18	2012-10-19
4	AAPL	6.0	24	2012-10-19	2012-10-20
In [22]:

, inplace=True)
aapl_sentiment.set_index('asof_date', inplace=True)
In [23]:

aapl_sentiment.head()
Out[23]:
symbol	sentiment_signal	sid	timestamp
asof_date				
2012-10-15	AAPL	6.0	24	2012-10-16
2012-10-16	AAPL	2.0	24	2012-10-17
2012-10-17	AAPL	6.0	24	2012-10-18
2012-10-18	AAPL	6.0	24	2012-10-19
2012-10-19	AAPL	6.0	24	2012-10-20
In [24]:

aapl_sentiment['sentiment_signal'].plot()
aapl_sentiment['sentiment_signal'].plot()
Out[24]:
<matplotlib.axes._subplots.AxesSubplot at 0x7ff21b5a2090>

In [27]:

10
aapl_sentiment = aapl_sentiment[ (aapl_sentiment.index > '2016-10-01')]
In [28]:

aapl_sentiment['sentiment_signal'].plot()
Out[28]:
<matplotlib.axes._subplots.AxesSubplot at 0x7ff219eac210>

In [ ]:

​
