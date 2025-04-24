import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
from difflib import SequenceMatcher
from typing import List, Dict


# ---------- TOOL: Web Search ----------
def web_search(query: str, num_results: int = 5) -> List[str]:
    print(f"[SEARCH] Searching for: {query}")
    urls = []
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=num_results)
        for result in results:
            if "href" in result:
                urls.append(result["href"])
            elif "url" in result:
                urls.append(result["url"])
    return urls


# ---------- TOOL: Web Scraper ----------
def scrape_page(url: str) -> str:
    print(f"[SCRAPE] Scraping: {url}")
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text(separator=' ', strip=True)
        return text[:3000]  # limit to 3000 characters
    except Exception as e:
        print(f"[ERROR] Failed to scrape {url}: {e}")
        return ""


# ---------- TOOL: Content Analyzer ----------
def analyze_content(content: str, query: str) -> float:
    # Basic content relevance using SequenceMatcher (can improve with NLP)
    return SequenceMatcher(None, content.lower(), query.lower()).ratio()


# ---------- TOOL: News Aggregator (simulated by using same web search) ----------
def get_news_articles(query: str) -> List[str]:
    return web_search(query + " latest news")


# ---------- AGENT LOGIC ----------
def research_agent(query: str, num_sources: int = 5) -> str:
    print("[AGENT] Starting research agent")
    urls = web_search(query, num_sources)
    content_data = []

    for url in urls:
        text = scrape_page(url)
        if text:
            score = analyze_content(text, query)
            content_data.append({
                "url": url,
                "score": score,
                "summary": text[:500]  # simple summary (first 500 chars)
            })

    # Sort results by relevance score
    content_data = sorted(content_data, key=lambda x: x["score"], reverse=True)

    report = f"\n======= RESEARCH REPORT =======\n\n# Research Report on: {query}\n"
    for i, data in enumerate(content_data, 1):
        report += f"\n## Source {i}: {data['url']}\n"
        report += f"**Relevance Score**: {round(data['score'], 2)}\n\n"
        report += f"{data['summary']}\n"

    return report


# ---------- MAIN ----------
if __name__ == "__main__":
    query = input("Enter your research query: ").strip()
    final_report = research_agent(query)
    print(final_report)
