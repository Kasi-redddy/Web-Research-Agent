# Web-Research-Agent
This project provides a research agent that fetches top search results from the web using DuckDuckGo, scrapes content from the fetched pages, analyzes the content for relevance to the search query, and generates a research report based on the results.

#Features
Web Search: Perform a web search using DuckDuckGo.

Web Scraping: Scrape the top results from the search and extract text.

Content Analysis: Analyze the relevance of the content based on the search query using SequenceMatcher.

Report Generation: Generate a research report with URLs, relevance scores, and summaries of the content.

#Requirements
Make sure you have Python 3.x installed on your machine. You can install the required dependencies by running:

bash
Copy
Edit
pip install -r requirements.txt

#Here is a list of the dependencies:

requests: To send HTTP requests and retrieve webpage data.

beautifulsoup4: To parse and extract HTML content from web pages.

duckduckgo_search: To perform web searches using DuckDuckGo’s API.

#Setup
Clone or download this repository to your local machine.

Navigate to the project directory in your terminal.

#Install dependencies:

bash
pip install -r requirements.txt


#Usage
Run the app.py file:

bash

python app.py

You will be prompted to enter a research query (e.g., "apple" or "latest technology trends").

The program will perform a search, scrape the top results, analyze their relevance, and generate a research report.

The report will display the URLs of the top results, their relevance scores, and a short summary of each page's content.

#Example
If you enter the query apple, the program will fetch the top 5 search results, scrape the pages, and display a research report with the relevant information.

Code Structure
web_search(query, num_results): Performs a web search using DuckDuckGo and returns a list of URLs.

scrape_page(url): Scrapes the content of the given URL and returns the text.

analyze_content(content, query): Analyzes the relevance of the scraped content to the search query using the SequenceMatcher.

get_news_articles(query): Fetches the latest news articles based on the search query (this can be extended for news aggregation).

research_agent(query, num_sources): Main function to handle the agent's logic, including searching, scraping, and analyzing content.


#Example Output
text
Copy
Edit
Enter your research query: apple
Fetching results for: apple
[SEARCH] Searching for: apple


# Research Report on: apple

## Source 1: https://www.apple.com
**Relevance Score**: 0.92

Apple Inc. is a multinational technology company headquartered in Cupertino, California. It designs, develops, and sells consumer electronics, computer software, and online services...

## Source 2: https://en.wikipedia.org/wiki/Apple_Inc.
**Relevance Score**: 0.85

Apple Inc. is known for its innovation and development of products such as the iPhone, iPad, and Mac computers. The company has grown to become one of the most valuable tech companies...

(Additional sources and summaries)


#Contributing
Feel free to open issues or submit pull requests if you want to contribute to this project. You can contribute by:

Enhancing the web scraping functionality.

Improving content analysis algorithms.

Adding more features like saving reports to a file.
