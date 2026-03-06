import numpy as np
import pymupdf


from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

user_query = "British Cycling changed one day. User is asking for which year? Give some more insight"

# UserQuery ---> Embeddings
query_embedding = model.encode(user_query) # []

# import the pdf embedings
embeddings = np.load("embeddings.npy") # [ [], [], .....]


# COSINE SIMILARity
scores = np.dot(embeddings, query_embedding) # array 

# i willchoose the top 2 pages

top_2_indices = np.argsort(scores)[::-1][:2]


# extract the page text

doc = pymupdf.open("Book.pdf")

two_index = []

for rank, idx in enumerate(top_2_indices, start=1):
    page_index = int(idx)

    print(page_index)
    print("-"*20)
    page_text = doc[page_index].get_text()
    print(page_text)
    print("-"*20)

    two_index.append(page_index)

# two_index = [16, 251]


prompt = f"""
    You will anser based on user query, and based on context only, qute the lines also
    User Query: {user_query}



    Context:
    ---------Page{two_index[0]}-----------
    {doc[two_index[0]].get_text()}
    ---------Page{doc[two_index[1]].get_text()}-----------
    {doc[two_index[1]]}

    """

print(prompt)


from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-nano",
    input=prompt
)

print(response.output_text)
