# from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI


class LangChainPipeline:

    def __init__(self, retriever, model_name=None):
        self.model_name = model_name
        self.retriever = retriever

        if self.model_name is None:
            self.model_name = 'gpt-3.5-turbo'

    # def get_turbo_llm(self, temperature=0, model_name='gpt-3.5-turbo'):
    #     turbo_llm = ChatOpenAI(temperature=temperature, model_name=model_name)
    #
    #     return turbo_llm

    def get_qa_chain(self, chain_type='stuff', llm_type=None):
        """
        Build a chain using langchain for retrival of embeddings through vector db or directly pass to openai call.
        :param chain_type: type of chain to be used while building chains
        :param llm_type: which type of llm to be used
        :return: returns a question-answer pipeline build through langchain
        """

        if llm_type is None:
            llm_type = OpenAI()
        qa_chain = RetrievalQA.from_chain_type(llm=llm_type, chain_type=chain_type,
                                               retriever=self.retriever, return_source_documents=True)

        return qa_chain
