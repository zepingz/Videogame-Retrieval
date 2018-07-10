import numpy as np

def get_score(embeddings):
    embeddings = np.array(embeddings)
    length = len(embeddings)
    bbox_sum = np.zeros(length-1)
    nuc_norm = np.zeros(length-1)
    for i in range(2, length):
        bbox_sum[i-1] = sum(np.amax(embeddings[:i], axis=0) - np.amin(embeddings[:i], axis=0))
        nuc_norm[i-1] = np.linalg.norm(np.cov(embeddings[:i].T), ord='nuc')
        
    return bbox_sum, nuc_norm
	
def get_embedding(img, model):
    return model.predict(np.expand_dims(img, axis=0))[0]
