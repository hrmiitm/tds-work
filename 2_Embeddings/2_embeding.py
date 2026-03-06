from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2") # it will download locally this MODEL 


all_pages_array = ["page 1 data", "introduction"]

array = model.encode(all_pages_array)

print(array.shape)
print(array)