def findBestConfidenceScore(input: dict[list[int]], recallThreshold = 0.9, best = "recall"):
    """
    A function that finds the BEST confidence score with recall >= 0.9. The BEST is defined by the maximum 
    recall by default, but you can also use precision or accuracy for it.
    Args:
        input:  dict of lists of integers. 
                Each key in the dict is the confidence score in interval (0.0; 1.0]. 
                Each list contains 4 integers.

    Returns:
        float number equal to the BEST threshold
    """
    bestMetric = 0
    bestThreshold = None
    for threshold, arr in input.items():
        if not isinstance(threshold, float) or threshold > 1 or threshold <= 0:
            raise ValueError("Invalid threshold in dict " + str(threshold))
        if len(arr) != 4:
            raise ValueError("Invalid number of elements in confidence matrix " + str(len(arr)))
        if not all(isinstance(x, int) for x in arr):
            raise TypeError("All values should be integer")
        tn, fp, fn, tp = arr
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        accuracy = (tp + tn) / (tp + tn + fp + fn)
        if best == "recall":
            if recall >= recallThreshold and recall > bestMetric:
                bestMetric = recall
                bestThreshold = threshold
        elif best == "precision":
            if recall >= recallThreshold and precision > bestMetric:
                bestMetric = precision
                bestThreshold = threshold
        elif best == "accuracy":
            if recall >= recallThreshold and accuracy > bestMetric:
                bestMetric = accuracy
                bestThreshold = threshold
        else:
            raise ValueError("Invalid BEST definition "+ best)
    return bestThreshold
