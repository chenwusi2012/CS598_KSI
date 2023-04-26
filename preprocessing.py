import torch
import torch.autograd as autograd
import numpy as np


def preprocessing(data, label_to_ix, word_to_ix, wikivoc, batchsize):
    new_data = []
    for i, note, j in data:
        templabel = [0.0] * len(label_to_ix)
        for jj in j:
            if jj in wikivoc:
                templabel[label_to_ix[jj]] = 1.0
        templabel = np.array(templabel, dtype=float)
        new_data.append((i, note, templabel))
    new_data = np.array(new_data, dtype=object)

    lenlist = []
    for i in new_data:
        lenlist.append(len(i[0]))
    sortlen = sorted(range(len(lenlist)), key=lambda k: lenlist[k])
    new_data = new_data[sortlen]

    batch_data = []

    for start_ix in range(0, len(new_data) - batchsize + 1, batchsize):
        thisblock = new_data[start_ix:start_ix + batchsize]
        mybsize = len(thisblock)
        numword = np.max([len(ii[0]) for ii in thisblock])
        main_matrix = np.zeros((mybsize, numword), dtype=int)
        for i in range(main_matrix.shape[0]):
            for j in range(main_matrix.shape[1]):
                try:
                    if thisblock[i][0][j] in word_to_ix:
                        main_matrix[i, j] = word_to_ix[thisblock[i][0][j]]

                except IndexError:
                    pass  # because initialize with 0, so you pad with 0

        xxx2 = []
        yyy = []
        for ii in thisblock:
            xxx2.append(ii[1])
            yyy.append(ii[2])

        xxx2 = np.array(xxx2)
        yyy = np.array(yyy)
        batch_data.append((autograd.Variable(torch.from_numpy(main_matrix)), autograd.Variable(torch.FloatTensor(xxx2)),
                           autograd.Variable(torch.FloatTensor(yyy))))
    return batch_data
