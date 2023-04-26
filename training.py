import numpy as np
import copy


def trainmodel(model, sim, topk, max_epochs, batchtraining_data, batchval_data, wikivec, loss_function, optimizer):
    modelsaved = []
    modelperform = []

    bestresults = -1
    bestiter = -1
    for epoch in range(max_epochs):
        model.train()

        lossestrain = []
        recall = []
        for mysentence in batchtraining_data:
            model.zero_grad()

            targets = mysentence[2].cuda()
            tag_scores = model(mysentence[0].cuda(), mysentence[1].cuda(), wikivec.cuda(), sim)
            loss = loss_function(tag_scores, targets)
            loss.backward()
            optimizer.step()
            lossestrain.append(loss.data.mean())
        print(f"epoch = {epoch}")
        modelsaved.append(copy.deepcopy(model.state_dict()))
        model.eval()

        recall = []
        for inputs in batchval_data:

            targets = inputs[2].cuda()
            tag_scores = model(inputs[0].cuda(), inputs[1].cuda(), wikivec.cuda(), sim)

            loss = loss_function(tag_scores, targets)

            targets = targets.data.cpu().numpy()
            tag_scores = tag_scores.data.cpu().numpy()

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

        print('validation recall @ top-', topk, np.mean(recall))

        modelperform.append(np.mean(recall))
        if modelperform[-1] > bestresults:
            bestresults = modelperform[-1]
            bestiter = len(modelperform) - 1
            print(f"Update the best model to epoch {bestiter}")

        if (len(modelperform) - bestiter) > 5:
            print(modelperform, bestiter)
            return modelsaved[bestiter]

    print(f"Reach the max epochs, return the best model at epoch {bestiter}")
    return modelsaved[bestiter]
