PROMPT_TEMPLATE = """
        Context = {context}

        Question: {question}"""


class RAGBase():

    def __init__(self,index,llm_client,config,
                 prompt_template = PROMPT_TEMPLATE,course = "llm-zoomcamp",model = "gemini-3.5-flash"):
        self.index = index
        self.llm_client = llm_client
        self.config = config
        self.course = course
        self.prompt_template = prompt_template
        self.model = model


    def search(self,question,num_results = 5):
        boost_dict = {"question": 2.0, "section": 0.5}
        filter_dict = {"course": self.course}

        return self.index.search(
            question,
            boost_dict=boost_dict,
            filter_dict=filter_dict,
            num_results=num_results
        )


    def build_context(self,search_results):

        lines = []

        for doc in search_results:
            lines.append(doc["section"])
            lines.append("Q: " + doc["question"])
            lines.append("A: " + doc["answer"])
            lines.append("")

        return "\n".join(lines).strip()

    def build_prompt(self, question, search_results):
        context = self.build_context(search_results)
        return self.prompt_template.format(
                question=question, context=context
            )

    def llm(self,prompt):
        response = self.llm_client.models.generate_content(model = self.model, contents = prompt,config = self.config)
        return response.text or "Couldn't get a response"

    def rag(self,question):
        search_results = self.search(question)
        prompt = self.build_prompt(question,search_results)
        response = self.llm(prompt)

        return response











