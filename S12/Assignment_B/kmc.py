import numpy as np
from sklearn.cluster import KMeans

def kmc_elbow(input_data):
    X = np.array(input_data[['bbox_rel_log_width', 'bbox_rel_log_height']])

    wcss = []
    for cluster_index in range(1, 15):
        kmeans = KMeans(n_clusters=cluster_index, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
    plt.plot(range(1, 15), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()

def plot_clusters(num_of_clusters, input_data):
    X = np.array(input_data[['bbox_rel_log_width', 'bbox_rel_log_height']])

    kmeans = KMeans(n_clusters=num_of_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
    pred_y = kmeans.fit_predict(X)
    plt.figure(figsize=(10,8))
    plt.scatter(X[:,0], X[:,1], c=pred_y, cmap="tab10", s=100)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, alpha=.7)
    plt.title('Clustering of bbox ratios')
    plt.show()