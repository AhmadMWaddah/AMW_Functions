class MeanSquaredError:
    def __init__(self, actual_data, predicted_data):
        self.
# Mean Squared Error.
def mean_square_error(self):
    """
    Function Takes 2 Parameters lists of data, making counter and add to it and zipping lists.
    :param actual_data:
    :param predicted_data:
    :return: Mean Squared Error Of Both Data Actual and Predicted.
    """
    # Starter Counter.
    counter = 0
    # Combining BOth List With Zipping Function.
    data_combined = zip(actual_data, predicted_data)
    # Loop For Each cell in both data.
    for (each_actual, each_predicted) in data_combined:
        # Adding Results To Starter Counter.
        counter += (each_actual - each_predicted) ** 2
    return counter / len(actual_data)

# -------------------- #
def data_mean(data_values):
    """
    Getting The Mean Number For Data.
    :param data_values: Set Of Data
    :return: Mean Of Data Values.
    """
    mean_of_data = sum(data_values) / len(data_values)
    return mean_of_data

# -------------------- #
def data_variance(data_values, mean_of_data):
    """
    Getting The Variance Number For Data.
    :param data_values: Set Of Data
    :param mean_of_data: Mean Of Data From Previous Function.
    :return: Variance Of Data.
    """
    starter_counter = 0
    for data_cells in data_values:
        starter_counter += (data_cells - mean_of_data) ** 2
    variance_of_data = starter_counter / len(data_values)
    return variance_of_data

# -------------------- #
def data_covariance(features_values, labels_values, features_mean, labels_mean):
    """
    It measures the degree of change in the variables, i.e. when one variable changes, will there be the same/a similar change in the other variable.
    :param features_values: (X) Weights and Features Of Data
    :param labels_values: (Y) Predictions and Labels Of Data
    :param features_mean: Measured Mean Of Features For Data
    :param labels_mean: Measured Mean Of Labels For Data
    :return: Measure of relationship between 2 variables.
    """
    # Labels and Features Added and Multiplied.
    features_labels_sum_multiply = 0
    # Combine Both Features and Labels In One Object.
    feature_label_combined = zip(features_values, labels_values)
    for (features_values, labels_values) in feature_label_combined:
        features_labels_sum_multiply += ((features_values - features_mean) * (labels_values - labels_mean))
    covariance_of_data = features_labels_sum_multiply / len(features_values)
    return covariance_of_data

# -------------------- #
def data_coefficient(features_values, labels_values):
    """
    Measure of correlation overcomes the scale dependency of covariance by standardizing the measures.
    :param features_values: (X) Weights and Features Of Data
    :param labels_values: (Y) Predictions and Labels Of Data
    :return: Beta One And Beta Zero.
    """
    features_mean = data_mean(features_values)
    labels_values = data_mean(labels_values)
    features_variance = data_variance(features_values, features_mean)
    labels_variance = data_variance(labels_values, labels_values)
    print(features_variance)
    beta_one = data_covariance(features_values, labels_values, features_mean, labels_values) / features_variance
    beta_zero = labels_values - (beta_one * features_mean)
    return beta_one, beta_zero

# -------------------- #
def simple_linear_regression(features_train, labels_train, features_test):
    """
    Using a linear regression model will allow you to discover whether a relationship between variables exists at all.
    :param features_train:
    :param labels_train:
    :param features_test:
    :return: prediction_of_data
    """
    beta_one_train, beta_zero_train = data_coefficient(features_train, labels_train)
    prediction_of_data = beta_one_train * features_test + beta_zero_train
    return prediction_of_data

# -------------------- #
def evaluate_model(features_train, labels_train, features_test, labels_test):
    """
    Evaluate Model anc Compare Train Data With Test Data.
    :param features_train:
    :param labels_train:
    :param features_test:
    :param labels_test:
    :return:    mean_square_error
    """
    prediction_data = simple_linear_regression(features_train, labels_train, features_test)
    return mean_square_error(prediction_data, labels_test)
