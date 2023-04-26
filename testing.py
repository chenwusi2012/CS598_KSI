import torch.nn as nn
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.metrics import f1_score


def testmodel(model, modelstate, sim, batchtest_data, wikivec, topk):
    model.cuda()
    model.load_state_dict(modelstate)
    loss_function = nn.BCELoss()
    model.eval()
    recall = []
    lossestest = []

    y_true = []
    y_scores = []

    for inputs in batchtest_data:

        targets = inputs[2].cuda()

        tag_scores = model(inputs[0].cuda(), inputs[1].cuda(), wikivec.cuda(), sim)

        loss = loss_function(tag_scores, targets)
        targets = targets.data.cpu().numpy()
        tag_scores = tag_scores.data.cpu().numpy()

        lossestest.append(loss.data.cpu().mean())
        y_true.append(targets)
        y_scores.append(tag_scores)

        for iii in range(0, len(tag_scores)):
            temp = {}
            for iiii in range(0, len(tag_scores[iii])):
                temp[iiii] = tag_scores[iii][iiii]
            temp1 = [(k, temp[k]) for k in sorted(temp, key=temp.get, reverse=True)]
            thistop = int(np.sum(targets[iii]))
            hit = 0.0

            for ii in temp1[0:max(thistop, topk)]:
                if targets[iii][ii[0]] == 1.0:
                    hit = hit + 1
            if thistop != 0:
                recall.append(hit / thistop)
    y_true = np.concatenate(y_true, axis=0)
    y_scores = np.concatenate(y_scores, axis=0)
    y_true = y_true.T
    y_scores = y_scores.T
    temptrue = []
    tempscores = []
    for col in range(0, len(y_true)):
        if np.sum(y_true[col]) != 0:
            temptrue.append(y_true[col])
            tempscores.append(y_scores[col])
    temptrue = np.array(temptrue)
    tempscores = np.array(tempscores)
    y_true = temptrue.T
    y_scores = tempscores.T
    y_pred = (y_scores > 0.5).astype(int)
    # print ('test loss', np.mean(lossestest))
    # print ('top-',topk, np.mean(recall))
    # print ('macro AUC', roc_auc_score(y_true, y_scores,average='macro'))
    # print ('micro AUC', roc_auc_score(y_true, y_scores,average='micro'))
    # print ('macro F1', f1_score(y_true, y_pred, average='macro'))
    # print ('micro F1', f1_score(y_true, y_pred, average='micro'))
    test_loss = np.mean(lossestest)
    test_recall = np.mean(recall)
    test_mac_auc = roc_auc_score(y_true, y_scores, average='macro')
    test_mic_auc = roc_auc_score(y_true, y_scores, average='micro')
    test_mac_f1 = f1_score(y_true, y_pred, average='macro')
    test_mic_f1 = f1_score(y_true, y_pred, average='micro')

    return test_loss, test_recall, test_mac_auc, test_mic_auc, test_mac_f1, test_mic_f1
