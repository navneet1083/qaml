from chainpipeline.lpipeline import LangChainPipeline
from vectorDBConn.chromaDBInit import ChromaDBInit
import yaml
import os
from functools import lru_cache


class BuildResponse:

    def __init__(self, config_data):
        self.response_type = 'text'
        self.config_data = config_data
        self.retriever = None

    def get_db(self):
        doc_path = self.config_data['vectordb']['chromadb']['paths']['doc_path']
        persist_loc = self.config_data['vectordb']['chromadb']['paths']['persist_loc']
        print(f'doc_path : {doc_path} :: persist_loc : {persist_loc}')

        if self.retriever is None:
            print(f'retriever is NONE ********************************************')
            chromadb = ChromaDBInit(doc_path=doc_path, persist_loc=persist_loc)
            # creating db and storing in disk
            chromadb.create_db()
            # load the existing db
            vectordb = chromadb.load_db()
            # get retriever
            self.retriever = vectordb.as_retriever(search_kwargs={"k": 2})

    def process_llm_response(self, llm_response):
        # print(f'llm response : {llm_response}')
        # print(llm_response['result'])
        # print('\n\nSources:')
        # for source in llm_response["source_documents"]:
        #     print(source.metadata['source'])
        return llm_response['result']

    @lru_cache(maxsize=16)
    def get_response(self, question):
        # First get the db conn
        self.get_db()

        # building chain
        chains = LangChainPipeline(retriever=self.retriever)
        qa_chain = chains.get_qa_chain()
        llm_response = qa_chain(question)

        processed_resp = self.process_llm_response(llm_response)

        return processed_resp


class ConfigReader:
    def __init__(self):
        self.filename = os.path.join('configs', 'config')
        self.output = None

    def get_yaml_data(self):
        if self.output is None:
            with open(f'{self.filename}.yaml', 'r') as f:
                self.output = yaml.safe_load(f)
        return self.output


