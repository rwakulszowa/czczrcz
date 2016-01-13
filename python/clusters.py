from sklearn.cluster import KMeans as KM

class KMeans(object):
    def __init__(self, test, n_clusters, init_means):
        self.km = KM(n_clusters=n_clusters, init=init_means, n_init=1)
        self.test = test

    def get_readable_means_ffs(self):
        return {label: center[0]
            for label, center in enumerate(self.km.cluster_centers_)}

    def split(self, data):
        values = [self.test(d) for d in data]

        self.km.fit([[v] for v in values])
        means = self.get_readable_means_ffs()

        containers = {label: (means[label], [])
            for label in means}

        for el, label in zip(data, self.km.labels_):
            containers[label][1].append(el)

        return containers

    def predict(self, x):
        return self.km.predict(x)
