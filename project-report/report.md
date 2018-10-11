## Instacart basket Analysis using MongoDB and Performance Benchmarking on VM and Cloud

### Project Participants

- Izolda Fetko fa18-523-60
- Nishad Tupe fa18-523-64
- Vishal Bhoyar fa18-523-72


### Abstract

In today’s busy world, time is a valuable asset. People 
are trying to save time and money in all segments of their 
lives, one of them being grocery shopping. Instacart is an 
e-commerce platform that helps them save both. This technology 
allows its app and website users to shop at their favorite 
stores as well as combine products from more than one store 
in the same order, without having to make the trips to those 
stores. Our project focuses on this interesting concept and 
conducts an Instacart market basket analysis while utilizing 
MongoDB as the data storage apparatus. The goal of our project 
is two-fold, the first part includes evaluating the benefits of 
this NoSQL database technology for the online shopping analysis 
purposes that can ultimately be applied to other e-commerce 
platforms. The second part entails a MongoDB performance 
benchmarking by testing it on a local machine, a virtual 
machine, and on a cloud service - Mongo Atlas.

### Keywords

Online grocery shopping, market basket analysis, Instacart, 
MongoDB, PyMongo, Kaggle.com Public API, virtual machine, 
Mongo Atlas

### Introduction

The modern world is increasingly becoming busier each year. 
The number of daily tasks has exponentially increased compared 
to the days when our parents were in the same life stage as we 
are now. This increase in daily tasks is even more noticeable 
in the urban areas where people are, in their commute to and 
from those tasks, continuously being slowed down by traffic 
jams, construction, and other hurdles. In addition to the time 
constraint, cost of living is steadily increasing in all areas, 
with some urban area costs reaching the all-time highs. Due to 
these changes, humans are becoming very creative in finding ways 
to save their precious time and cut down the cost of living. In 
their search, a large number of individuals are turning towards 
the online shopping which allows them to fulfill their needs 
without all the hassle. The online shopping concept has been 
established by large companies such as Amazon, and it is slowly 
sneaking into other industries and services. One of those industries 
includes the large grocery stores and wholesale chains such as 
Krogers and Costco. These two companies are partnered with the 
grocery delivery service and platform which is the topic of our 
report - its name is Instacart [@www-partnerships]. 

This e-commerce platform was founded in 2012 by a former Amazon 
employee, Apoorva Mehta, who is the company’s current 
CEO[@www-wikinstacart]. The service is mainly offered through 
the company website, but it also offers an Android and iOS 
version of a smartphone app [@www-apps]. To deliver its services, 
the company uses a team of “personal shoppers” to “procure grocery 
items from a variety of stores” in the desired geographical 
area [@www-apps]. The app allows one to place an order from a 
specific store or multiple stores while also offering substitutions 
for all items in case the originally chosen items are out of 
stock [@www-bold]. Once an order is placed, the app offers a live 
view of the actions performed by the “personal shopper” with 
timestamps for each step taken as well as their GPS location [@www-bold]. 
This is a very valuable feature as it helps Instacart users to 
prepare for the delivery. The service is paid for through the 
Android Pay or Apple Pay, depending on the app used [@www-pay], 
and the receipts are sent via email to the customers [@www-bold]. 
According to the Data and Machine Learning Advisor of the company, 
Jeremy Stanley, 2017 yielded more than 200,000 users and over 
3 million orders placed [@www-stanley]. These results are a great 
indicator of how software technologies and big data are slowly 
making changes in the way of how we think of grocery shopping and 
overall retail shopping in general.

In our project, we focus on the market basket analysis of the 
Instacart customers, more specifically on the 3 million orders 
that are publicly available via the Kaggle platform. The application 
built by our team allows a seamless download of the dataset via 
Kaggle’s public API and data import into MongoDB. 
Once in this NoSQL database, the data is ultimately joined and wrapped 
into a form ready for data analysis. The exploratory analysis is completed
with use of PyMongo and the visualizations are completed with help of Python 
and its packages such as Numpy, Pandas, Matplotlib, Altair, and Seaborn. 
In this segment, the project touches upon statistics such as Average Order 
Size, Average Item Quantity per Order, Time of Order, Most Frequently Purchased 
Items, Most Frequently Purchased Categories of Items, and similar. The final 
stage of the project includes technology benchmarking, where our team 
is comparing MongoDB performance on a local machine, on a virtual machine,
and on a cloud service – Mongo Atlas. We are hoping that 
the results and the underlying idea of our research will not only encourage
other researchers to consider MongoDB as a suitable medium in future Big 
Data applications, considering its cloud capabilities, but also encourage 
them to become more curious about the Big Data involving online shopping.
The online retail market is rapidly expanding in all areas. Global 
companies are not the only ones who offer their products online any more.
Small, local stores are slowly starting to offer these services and 
compete with market leaders. This is in return slowly expanding the 
network of interconnected technologies, in other words, Internet of 
Things (IoT) realm. In this regard, the capabilities of the IoT are very 
impressive, but have an enormous potential to get even more fascinating. 
Currently, Amazon Alexa is capable of placing online orders on Amazon. 
Given the rate AI technology is accelerating nowadays, perhaps virtual 
assistants will have the capability of placing orders on non-native 
platforms in the near future as well.
