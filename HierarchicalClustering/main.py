from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, inconsistent
from scipy.spatial.distance import pdist
import numpy as np

# generate two clusters : a with 100 points, b with 50

np.random.seed(4711)
a = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100, ])
b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], size=[50, ])
X = np.concatenate((a, b), )

# print(X.shape)

plt.scatter(X[:,0], X[:,1])
#plt.show()

# generate linkage matrix
Z = linkage(X, 'ward')

c, coph_dists = cophenet(Z, pdist(X))
# print(c)

# # print(Z[:20])
# print(X[[33, 68, 62]])
#
# idxs = [33, 68, 62]
# plt.figure(figsize=(10, 8))
# plt.scatter(X[:,0], X[:,1])
# plt.scatter(X[idxs,0], X[idxs,1], c='r')
# idxs = [15, 69, 41]
# plt.scatter(X[idxs,0], X[idxs,1], c='y')
# # plt.show()
#
# # calculate full dendrogram
# plt.figure(figsize=(25, 10))
# plt.title('Hierarchial Clusterning Dendrogram')
# plt.xlabel('sample index')
# plt.ylabel('distance')
#
# dendrogram(Z,
#            leaf_rotation=90,
#            leaf_font_size=8 )
# # plt.show()
#
# print(Z[-4:,2])
#
# plt.title('Hierarchical Clustering Dendrogram (truncated)')
# plt.xlabel('sample index or (cluster size)')
# plt.ylabel('distance')
# dendrogram(
#     Z,
#     truncate_mode='lastp',  # show only the last p merged clusters
#     p=12,  # show only the last p merged clusters
#     leaf_rotation=90.,
#     leaf_font_size=12.,
#     show_contracted=True,  # to get a distribution impression in truncated branches
# )
# #plt.show()
#
#
# def fancy_dendrogram(*args, **kwargs):
#     max_d = kwargs.pop('max_d', None)
#     if max_d and 'color_threshold' not in kwargs:
#         kwargs['color_threshold'] = max_d
#     annotate_above = kwargs.pop('annotate_above', 0)
#
#     ddata = dendrogram(*args, **kwargs)
#
#     if not kwargs.get('no_plot', False):
#         plt.title('Hierarchical Clustering Dendrogram (truncated)')
#         plt.xlabel('sample index or (cluster size)')
#         plt.ylabel('distance')
#         for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
#             x = 0.5 * sum(i[1:3])
#             y = d[1]
#             if y > annotate_above:
#                 plt.plot(x, y, 'o', c=c)
#                 plt.annotate("%.3g" % y, (x, y), xytext=(0, -5),
#                              textcoords='offset points',
#                              va='top', ha='center')
#         if max_d:
#             plt.axhline(y=max_d, c='k')
#     return ddata
#
# # set cut-off to 50
# max_d = 50  # max_d as in max_distance
#
# fancy_dendrogram(
#     Z,
#     truncate_mode='lastp',
#     p=12,
#     leaf_rotation=90.,
#     leaf_font_size=12.,
#     show_contracted=True,
#     annotate_above=10,
#     max_d=max_d,  # plot a horizontal cut-off line
# )
# plt.show()


# fancy_dendrogram(
#     Z,
#     truncate_mode='lastp',
#     p=12,
#     leaf_rotation=90.,
#     leaf_font_size=12.,
#     show_contracted=True,
#     annotate_above=10,
#     max_d=16,
# )
# plt.show()

# depth = 5
depth = 3
incons = inconsistent(Z, depth)
print(incons[-10:])

last = Z[-10:, 2]
last_rev = last[::-1]
idxs = np.arange(1, len(last) + 1)
plt.plot(idxs, last_rev)

acceleration = np.diff(last, 2)  # 2nd derivative of the distances
acceleration_rev = acceleration[::-1]
plt.plot(idxs[:-2] + 1, acceleration_rev)
plt.show()
k = acceleration_rev.argmax() + 2  # if idx 0 is the max of this we want 2 clusters
print ("clusters:", k)
