Brance <Position>Task
Name:   Navneet
Linkedin Profile: 
Date Challenge Received:
Date Solution Delivered:


<hr>


## Problem Statement 
What was the task and how you understood it. 


## Approach
Your approach to the problem. Mention any assumptions made.

For building such AI model that can handle 1 million requests daily, need to 
consider `scalability`, `performance` and `reliability`. My proposed architecture
 that incorporates a _vector database_ and meets these requirements:

- __Load Balancer__: A load balancer to distribute incoming requests across multiple
 instances of the QA module. This helps distribute the workload and improve fault
tolerance.
- __Question Answer Moduel__: Set up multiple instances of the question answering 
module, which can be either a hardcoded response or a model-based approach. 
These instances should be stateless and capable of handling concurrent requests.
- __Vector Database__: To efficiently search and retrieve information for question 
 answering, we can use a vector database. Other popular options are 
 `Redis` and `Qdrant`, both of which provide vector storage and 
 indexing capabilities.
  - __Redis__: Redis is an _in-memory_ data structure store that can be used as a
  vector database. It supports efficient search operations using Redis modules 
  like RedisAI and Redisearch. RedisAI allows you to perform vector-based 
  similarity searches, while Redisearch enables full-text search capabilities. 
  Redis is known for its simplicity, performance, and wide community support.
  - __
  



## Solution
Details about your solution. Illustrate performance and design with diagrams.


## Future Scope
Thoughts on how you could have improved the solution.
