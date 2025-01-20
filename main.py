import kagglehub

# Download latest version
path = kagglehub.dataset_download("kaushiksuresh147/top-10-cryptocurrencies-historical-dataset")

print("Path to dataset files:", path)