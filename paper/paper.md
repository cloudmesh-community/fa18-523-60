#Kaggle.com Public API

In the recent years, data science has become one of the 
most important drivers of the modern economy. It is used 
to uncover actionable insights into the consumer markets, 
for conveying powerful messages drawn from big data to 
shareholders and consumers, as well as building technologies 
that are continuously improving the quality of life around 
the globe [@www-datascience]. This “growing importance of 
data science has, in turn, led to the growth and importance 
of data scientists”[@www-datascience]. An online platform 
that allows the continuous idea sharing, learning, and 
collaboration for those individuals is Kaggle.com.

Kaggle.com is a website, a virtual space where data
enthusiasts flock to explore project topics, work on 
their own projects, and participate in lucrative 
competitions [@www-kaggle]. This platform was created 
in 2010 by Anthony Goldbloom and Ben Hamner, and today 
it includes a community of more than one million data 
scientists and machine learners [@www-kaggle-blog]. According 
to the company’s CEO (Anthony Goldbloom), the earliest competitions 
included  “participants who called themselves computer scientists, 
statisticians, econometricians and bioinformaticians” [@www-kaggle-blog]. 
Over time, those “silo-ed” communities came together, “shared 
different approaches and ideas through the forums and Kaggle Kernels”[@www-kaggle-blog]
which resulted in forming of the well-known platform we see today. 
According to the Kaggle documentation, the platform supports various 
types of datasets, such as CSV, Excel (although recommended to be 
uploaded as CSV), JSON, SQLite, BigQuery, and other [@www-kaggle-datasets].
Other file formats constitute PNG imagery files, NPZ specialty file formats
, as well as complex hierarchical data formats like HDF5 [@www-kaggle-datasets]. 
Kaggle also supports archives, in other words, “files compressed using 
the ZIP file format as well as other common archive formats like 7z” [@www-kaggle-datasets]. 
The datasets are organized in a list on the Datasets webpage, and can be 
filtered in a few different ways: by searching a common term in the 
search bar; by choosing the dataset type from the drop-down menu; by 
choosing the dataset size; and/or by choosing one of the available tags 
in the Tags submenu. “Tags are added by dataset owners to indicate the 
topic of the dataset”, as well as techniques that can be used to explore 
the dataset (e.g., “classification”), “or the type of the data itself 
(e.g., “text data”) “ [@www-kaggle-datasets].

To easily obtain those datasets, Kaggle offers their newly created 
Public API option to its users. API stands for “Application Programming 
Interface” “through which interactions happen between an enterprise and 
applications that use its assets” [@www-apiwiki]. “When used in the 
context of web development, an API is typically defined as a set of 
specifications, such as Hypertext Transfer Protocol (HTTP) request 
messages, along with a definition of the structure of response messages, 
usually in an Extensible Markup Language (XML) or JSON format” [@www-apiwiki].
Kaggle Public API  was launched in February 2018 and can be used for 
“creating datasets, kernels”, or simply “connect with Kaggle”[@www-kaggleapi]. 
Although still in its beta phase, it allows more user-friendly data 
download as well as a seamless workflow for the community members. In 
order to be able to use this technology, users need to ensure that they 
have installed the latest Python 3 version on their machines as well as 
the pip package manager [@www-githubkagapi]. Accessing the API is done by 
using a simple command line, however, this is not possible until a Kaggle 
account is created [@www-githubkagapi]. Once the initial step is completed,
an API token can be created, which triggers a download of a JSON file that
contains the user credentials necessary to access the API [@www-githubkagapi].
Once the sign up is finalized, the various command lines can be used to 
access the list of competitions along with the files and submissions 
associated with them [@www-githubkagapi]. A different set of commands 
can be used for dataset downloads and dataset creation, while the final 
group of commands listed on the Kaggle API GitHub page is the commands to 
manage Kernels, more specifically Kernel pull and push [@www-githubkegapi].

The relationship between public APIs and Big Data is very strong. The Big 
Data volume has grown so much in the recent years with the rise of open/public 
APIs that some of the experts started “using the term ‘API economy’ to refer to 
transactions taking place with help of APIs” [@www-apieconomy]. This technology
has allowed developers, data scientists, and even ordinary layman to access 
datasets quickly and excel business, and ultimately industries. It is also 
helping students with their education as it can aid “apps and websites interact 
with data storage systems” used in online education [@www-apieconomy]. 