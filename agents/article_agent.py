
from services.llm_service import get_llm
from tools.tavily_tool import search_articles
from agents.prompts import ARTICLE_PROMPT
from langchain_core.prompts import PromptTemplate


class ArticleAgent:

    def __init__(self):
        self.llm = get_llm()

    def generate_content(self, topic, output_type):

        search_data = search_articles(topic)

        formatted_results = ""

        for result in search_data["results"]:

            formatted_results += f"""
            Title: {result.get('title')}
            Content: {result.get('content')}
            """

        prompt = PromptTemplate(
            input_variables=["topic", "search_results", "output_type"],
            template=ARTICLE_PROMPT
        )

        final_prompt = prompt.format(
            topic=topic,
            search_results=formatted_results,
            output_type=output_type
        )

        response = self.llm.invoke(final_prompt)

        return response.content
