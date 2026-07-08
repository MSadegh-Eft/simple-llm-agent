from datetime import datetime
import wikipedia
from ddgs import DDGS
from langchain_core.tools import tool

@tool("web_search")
def search_tool(query: str) -> str:
    """Search the web for current information on a topic."""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
    except Exception as exc:  # network/backend errors from the search provider
        return f"Search failed: {exc}"

    if not results:
        return "No results found."

    return "\n\n".join(
        f"{r.get('title', 'Untitled')}\n{r.get('body', '')}\nSource: {r.get('href', '')}"
        for r in results
    )


@tool("wikipedia")
def wiki_tool(query: str) -> str:
    """Look up a topic on Wikipedia and return a short summary."""
    try:
        return wikipedia.summary(query, sentences=3, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError as exc:
        options = ", ".join(exc.options[:5])
        return f"'{query}' is ambiguous. Try one of: {options}"
    except wikipedia.exceptions.PageError:
        return f"No Wikipedia page found for '{query}'."
    except Exception as exc:
        return f"Wikipedia lookup failed: {exc}"


@tool("save_text_to_file")
def save_tool(data: str, filename: str = "research_output.txt") -> str:
    """Save structured research data to a local text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"