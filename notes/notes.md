# In this project
Build an AI assistant that can 
- read CSV file
- understand natural language question
- execute analysis code
- create visualizations
- remember context for follow-up questions
- handle error gracefully
- export analysis reports

## Not including below functionalities, but worth handling in next phrase
- authentication
- rate limiting
- more robust error handling
- support more file formats, e.g. Excels, JSON
- add SQL Query interface to let users write custom queries
- integrate with Google Sheet API to analyze live data directly from spreadsheets

## AI Enhancement TODO
- create custom prompts for specify industries such as finance or healthcare
- add model selector to choose between GPT-4, Claude or other open souce models based on user needs
- explore LangChain for building more complex AI workflows

## Business Enhancement
- implement usage tracking to understand which feature matters most
- build team collaboration features where users can share and annotate analysis

## Hot Reloading
A feature that allows developers to see changes instantly without restarting the application.

It is perfect for rapid prototyping.


## Enforce upload file format as CSV
It is to avoid scope creep in our prototyping phase of a product.

Scope creep is the continuous, uncontrolled expansion of a project goal or requirement. It typically happens gradually through informal requests or shifting priorities, rather than through a formal change management process, leading to severe budget overruns, missed deadlines and strained resources.


## ChatGPT Temperature
Temperature controls how creative or random the model's response is.
Zero means output is as focused as predictable as possible.
Tow means adding more variety and unpredictability. The model has more creative freedom to give unusual approaches.


## Tradeoff

### Memory vs Cost
Why can't we just send all our conversation history to GPT?

Large Language Model (LLM) like GPT has "context window", which represents the model working memory. Just like how you keep your so much information in your head at once.

GPT can only process a certain amount of texts at a time.

For GTP-4, this window is actually quite large, about 128,000 tokens, which is roughly 96,000 words.

In real world scenario where you may have hundreds or thousands of users, every token costs money.
The more conversation history we send, the more we pay for each request. 
Plus, longer contexts take more time to process, making our app feel slower, so we need to be strategic. 

## Hidden Costs of API Calls

- Financial cost per token
- Latency from processing more tokens
- Risk of hitting context limits

Solution:
Truncate long messages in history before saving them to GPT to save tokens.
Preserving key information without including the entire code responses previously received.

Small tricks like above can be easily overlooked, this can reduce your token usage by 60-70% without affecting the quality of responses.

The AI still understands the conversation flows, but we are not paying to send same code blocks again and again.
