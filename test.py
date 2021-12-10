import numpy as np


def augmented_euclidean_dist(a, b):
    # Write your code here.
    # Remember to return the right object.

    assert len(a) == len(b)
    id_a = np.where(a == -999)
    id_b = np.where(b == -999)

    id_ab = list(set(list(id_a[0])+list(id_b[0])))

    if (len(a) - len(id_ab))<2:
        return np.Inf
    else:
        id_sel = list(set(range(len(a))) - set(id_ab))

        a = a[id_sel]
        b = b[id_sel]

        return sum(np.power(np.abs(a-b),2))


a = np.array([1, 2, 3.5, 4.24])
b = np.array([-999, 4, 1.2, 3])
c = np.array([2, 1, -999, -999])

print(augmented_euclidean_dist(a,b))
