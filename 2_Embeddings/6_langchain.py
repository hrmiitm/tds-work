"""
RAG with LangChain - Simple version (no chains)
"""

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.messages import HumanMessage

# ── 1. Load PDF (each page = one Document) ──
print("Loading PDF...")
docs = PyMuPDFLoader("Book.pdf").load()

# ── 2. Embed pages and store in FAISS ──
print("Creating FAISS vector store...")
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

# ── 3. Retrieve Top-2 most relevant pages ──
query = "Who won gold medal at olympic games in cycling?"
print(f"Query: {query}")

top_2_docs = vectorstore.similarity_search(query, k=2)

# ── 4. Build prompt manually with the retrieved context ──
context = "\n\n---\n\n".join([doc.page_content for doc in top_2_docs])

prompt = f"""You are a helpful assistant. Answer based only on the context provided.

Question: {query}

Context:
{context}
"""

print("\nPrompt sent to LLM:")
print("-" * 40)
print(prompt[:500], "...")  # print just a snippet
print("-" * 40)

# ── 5. Pass to LLM directly ──
llm = ChatOpenAI(model="gpt-4.1-nano")
response = llm.invoke([HumanMessage(content=prompt)])

print("\nAnswer:", response.content)