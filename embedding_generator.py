from sentence_transformers import SentenceTransformer
import pandas as pd

# Load your data
df = pd.read_csv("Booking dataset.csv")  # Ensure the filename is correct

# Create the model
model = SentenceTransformer('paraphrase-MiniLM-L3-v2')

# Generate embeddings
text_data = df.apply(lambda x: f"Hotel: {x['hotel']}, Country: {x['country']}", axis=1)
embeddings = model.encode(text_data.tolist())

print(embeddings.shape)  # Optionally, print the shape of your embeddings

