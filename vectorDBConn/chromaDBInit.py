from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import os


class ChromaDBInit:

    def __init__(self, doc_path, persist_loc):

        self.doc_path = doc_path
        # OpenAI embeddings being used, it can be changed to other or local embeddings.
        self.embedding = OpenAIEmbeddings()
        self.persist_loc = persist_loc
        self.vectordb = None

        # location to store db
        if self.persist_loc is None:
                self.persist_loc = "./resources/docs-db"

        # Load and process the text files
        if self.doc_path is None:
            self.doc_path = os.path.join('resources', 'KnowledgeDocument(pan_card_services).txt')

        loader = TextLoader(self.doc_path)

        # loader = DirectoryLoader('./new_articles/', glob="./*.txt", loader_cls=TextLoader)
        documents = loader.load()

        # splitting the text into
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.texts = text_splitter.split_documents(documents)

    def create_db(self):
        """
        It will create a vector db (chroma DB) from a local file storage. Once created it stores the embeddings vector
        to disk.
        :return:
        """

        self.vectordb = Chroma.from_documents(documents=self.texts, embedding=self.embedding,
                                              persist_directory=self.persist_loc)
        # persist the db to disk
        self.vectordb.persist()

    def load_db(self):
        # Now we can load the persisted database from disk, and use it as normal.
        self.vectordb = Chroma(persist_directory=self.persist_loc, embedding_function=self.embedding)

        return self.vectordb

    def db_retriever(self):
        # retriever = self.vectordb.as_retriever()
        retriever = self.vectordb.as_retriever(search_kwargs={"k": 2})

        return retriever
