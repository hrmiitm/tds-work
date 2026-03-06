from sentence_transformers import SentenceTransformer
import pymupdf
import numpy as np


doc = pymupdf.open("Book.pdf")
model = SentenceTransformer("all-MiniLM-L6-v2") # it will download locally this MODEL 


all_pages_array = [ page.get_text() for page in doc ]


embedding_array = model.encode(all_pages_array)

print(embedding_array.shape)
# print(embedding_array)

np.save("embeddings.npy", embedding_array)





