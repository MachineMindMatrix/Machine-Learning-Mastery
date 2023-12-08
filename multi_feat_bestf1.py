#this function extracts the n features for best f1 score in log regression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS



def mult_feat_f1(modeling, X_train, y_train, X_test, y_test, average="macro", min_features=1, max_features=1,
                 print_progress=True, show_corr=True):
    if min_features == 1 and max_features == 1:
        arrays_Xtrain = iter_df(X_train)
        arrays_Xtest = iter_df(X_test)
        score = []

        for i in range(4):
            model.fit(arrays_Xtrain[i].T, y_train)
            y_pred = model.predict(arrays_Xtest[i].T)
            score.append(f1_score(y_test, y_pred, average="macro"))
        best_index = X_train.columns[score.index(max(score))]
        print(f" your maximum score is: {max(score)}" + f"for the Feature {best_index}")

    else:
        modeling = model
        efs = EFS(model, min_features, max_features, print_progress=True)

        efs = efs.fit(X_train, y_train)
        # print(efs.best_idx_)
        best_feature_indices = list(efs.best_idx_)
        print(X_train.columns[best_feature_indices])

        # Train a model using the best features
        best_features_X_train = X_train.iloc[:, best_feature_indices]
        best_features_X_test = X_test.iloc[:, best_feature_indices]

        model.fit(best_features_X_train, y_train)
        y_pred = model.predict(best_features_X_test)

        f1_sc = f1_score(y_test, y_pred, average='macro')

        # print(f'Best Features: {efs.best_idx_}')
        print(f'Best F1 Score: {f1_sc}')

    if show_corr == True:
        correlation_matrix = X_train.corr()
        fig, ax = plt.subplots()
        cax = ax.matshow(correlation_matrix, vmin=-1, vmax=1)

        fig.colorbar(cax)
        plt.show()