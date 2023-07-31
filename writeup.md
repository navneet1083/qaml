Brance <Position>Task
Name:   Navneet
Linkedin Profile: 
Date Challenge Received:
Date Solution Delivered:


<hr>


## Problem Statement 
What was the task and how you understood it. 

> Problem statement (in my way !!!)

There are subjective QAs list which needs to get hosted as a service on cloud platform and should be able to cater millions
of requests. These requests may grow in future so accordingly it should be catered. It requires a generative AI approach
as no-one can restrict end-user to raise questions. So the embedding vectors of such questions play an important role for 
providing solutions.

## Approach
Your approach to the problem. Mention any assumptions made.

For building such AI model that can handle 1 million requests daily, need to 
consider `scalability`, `performance` and `reliability`. My proposed architecture
 that incorporates a _vector database_ and meets these requirements:

- __Load Balancer__: A load balancer to distribute incoming requests across multiple
 instances of the QA module. This helps distribute the workload and improve fault
tolerance.
- __Reverse Proxy__: The Reverse Proxy sits between the Load Balancer and the Application Servers.
It handles tasks like `SSL termination, caching, and serving static content`, offloading these responsibilities from the Application Servers.
The Reverse Proxy can also protect the Application Servers from direct external exposure and potential attacks.
- __Application Server__: This component hosts the question answering AI model.
When a request comes in, the Application Server processes it by using the AI model to provide the relevant answer.
If needed, the Application Server can cache frequently asked questions or responses to reduce processing time for similar queries.
- __Question Answer Model__: Set up multiple instances of the question answering 
module, which can be either a hardcoded response or a model-based approach. 
These instances should be stateless and capable of handling concurrent requests.
- __Vector Database__: To efficiently search and retrieve information for question 
 answering, we can use a vector database. Other popular options are 
 `Redis` and `Qdrant`, both of which provide vector storage and 
 indexing capabilities.
- __AI Model__: This is the core of the system, consisting of the trained AI model responsible for answering questions. 
It can be fine-tuned model or online service (e.g. OpenAI) for generating embedding vectors which will be helpful in 
retrieval from any chosen vector databases.
  



## Solution
Details about your solution. Illustrate performance and design with diagrams.

> Flow of Request Processing:

- The incoming request is received by the Load Balancer.
- The Load Balancer routes the request to an available Reverse Proxy.
- The Reverse Proxy forwards the request to one of the Application Servers.
- The Application Server uses the AI Model to generate the answer to the question.
- The AI Model may use the Vector Database to perform similarity searches for relevant answers if necessary.
- The Application Server sends the answer back to the Reverse Proxy.
- The Reverse Proxy forwards the answer back to the Load Balancer.
- Finally, the Load Balancer returns the answer to the user who made the initial request.


> Scalability Consideration

To handle 1 million daily requests, you may need to scale the system horizontally. You can achieve this by:

- By chosen microservice architecture I can choose `kubernetes` to host application for those many requests.
- Adding more Application Servers to distribute the processing load.
- Using a load balancer that can automatically scale based on traffic.
- Using a distributed and scalable Vector Database to handle the increasing number of embeddings efficiently.
- Ensuring the AI Model is optimized for parallel processing and can handle concurrent requests.

> Below is very high level architecture view for a request-QA model

```shell
                           +----------------------------------+
                           |                                  |
                           |         Load Balancer           |
                           |                                  |
                           +-----------------+----------------+
                                             |
                                             |
                                 +-----------v----------+
                                 |                      |
                                 |  Reverse Proxy      |
                                 |                      |
                                 +-----------+----------+
                                             |
                                             |
                       +---------------------v---------------------+
                       |                                           |
                       |             Application Server            |
                       | (Handles AI Model and Question Answering) |
                       |                                           |
                       +---------------------+---------------------+
                                             |
                                             |
                 +---------------------------v---------------------+
                 |                                                 |
                 |                 Vector Database                 |
                 |             (e.g., Redis, Qdrant)               |
                 |                                                 |
                 +---------------------------+---------------------+
                                             |
                                             |
                                 +-----------v----------+
                                 |                      |
                                 |       Data Store     |
                                 |                      |
                                 +-----------+----------+
                                             |
                                             |
                                 +-----------v----------+
                                 |                      |
                                 |       AI Model       |
                                 |                      |
                                 +----------------------+

```

Note: The above architecture is a high-level overview and doesn't include all the details, such as security measures, caching strategies, or specific database configurations. Those details should be considered while implementing the system for real-world deployment.


<br>
<br>

>  Implemented solution

This is only the replication of the given problem statement and the same can be enhanced and be tested for large scale 
real-word.

For chosen `microservice` architecture, I have implemented `fastAPI` because of its robustness, easy-to-code and fastness.
For vector database, it is very convenient to store `embeddings` in terms of retrieval and comparison for faster 
results. Most prominent vector database would be `qdrant` because of its latency, handling data, caching, on disk, 
on memory, fault-tolerance, distributed etc. 

For the complexity and demo perspective, I have used/chosen `ChromaDB` for easy handling (without client-server). Embeddings
are written on-disk (I/O operations would be there; atleast for this demo). ChromaDB is used for storing embedding vectors
so the retrieval would be faster and efficient. I have used `RAG` approach for retrieval embeddings in an efficient way.

I have used OpenAI's `GPT-3.5` for generating embeddings. It requires `token API` key for generating embeddings and which 
will be a `request API call` to OpenAI. To run/execute this code, token would be needed.

> AI Model (Generative AI)

Apart from OpenAI's API call I tried to fine-tune Google's `FLAN-T5` model to simply test how the fine tuned model go upto.
Since, the dataset is very small it was very bad in estimating tokens. The `ROUGE` score was not satisfactory. To fine tune
such a large model, I have used `A5000` GPU (ran for 500 epochs). 

Not only full fine-tuned, because it could update weights and the whole model will not behave as previously. So, I have 
also did `PEFT` optimisation with `LoRA` strategies. It was only 10-13% of weight updation or learned rather update the whole
network weights. Which was efficient in terms of maintaining the old behaviour as well as encorporating the new task features.

All experiments are conducted on cloud based platform (in this case, jarvislabs) and are there in `notebooks` folder.


## Future Scope
Thoughts on how you could have improved the solution.

For any Generative AI model there can be 2 approaches for hosting either by calling existing API for embeddings or fine-tuned
model (which requires a GPU; optimization or quantization can make difference but depends on usecase).

By what I have understood the problem statement, you can store embeddings and serve it as a request but down the line it 
needs to get updated with more data and storing these would cost more. For serving such massive number would require more 
computations and much complex strategies which may include `complex load balancer`, `distributed API calls` and even 
underlying vector database distributed computations could be better.

Currently `RAG` (from facebook) is being implemented but as the data grows up it may require querying on distributed mode.
So `RAY` would be efficient while retrieving through distributed model which may be very convenient for retrival in 
millions of records.

Again it depends on the problem statement (real world usecase), if sufficient data is there then it can be easily fine-tuned
with `PEFT` and even quantization would impact a lot. Also, with the advancement of technology it can also be incorporated with 
`RLHF` for human feedback as policy agents to enhance the model.
