import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.api as sm
from sklearn import preprocessing
import matplotlib.pyplot as plt

data = pd.DataFrame()
rank_data = pd.read_csv("Conjoint_white_final.csv")
data = rank_data
X = data[["LetterThickness_200","LetterThickness_150","LetterThickness_100","LetterThickness_75","LetterSize_200","LetterSize_150","LetterSize_100","SpaceBetweenLetter_200","SpaceBetweenLetter_150","SpaceBetweenLetter_100","NumberofStation_3","NumberofStation_2","NumberofStation_1"]]
X = sm.add_constant(X)
Y = data["Rank"]
linearRegression = sm.OLS(Y,X).fit()
print(linearRegression.summary())

conjoint_attributes = ["LetterThickness_200","LetterThickness_150","LetterThickness_100","LetterThickness_75","LetterSize_200","LetterSize_150","LetterSize_100","SpaceBetweenLetter_200","SpaceBetweenLetter_150","SpaceBetweenLetter_100","NumberofStation_3","NumberofStation_2","NumberofStation_1"]
level_name = []
part_worth = []
part_worth_range = []
end = 1
for item in conjoint_attributes:
    nlevels = len(list(set(data[item])))
    level_name.append(list(set(data[item])))
    begin = end
    end = begin + nlevels - 1
    new_part_worth = list(linearRegression.params[begin:end])
    new_part_worth.append((-1) * sum(new_part_worth))
    part_worth_range.append(max(new_part_worth) - min(new_part_worth))
    part_worth.append(new_part_worth)
    # end set to begin next iteration

attribute_importance = []
for item in part_worth_range:
    attribute_importance.append(round(100 * (item / sum(part_worth_range)),2))


effect_name_dict = {"LetterThickness_200":"LetterThickness_200","LetterThickness_150":"LetterThickness_150","LetterThickness_100":"LetterThickness_100","LetterThickness_75":"LetterThickness_75","LetterSize_200":"LetterSize_200","LetterSize_150":"LetterSize_150","LetterSize_100":"LetterSize_100","SpaceBetweenLetter_200":"SpaceBetweenLetter_200","SpaceBetweenLetter_150":"SpaceBetweenLetter_150","SpaceBetweenLetter_100":"SpaceBetweenLetter_100","NumberofStation_3":"NumberofStation_3","NumberofStation_2":"NumberofStation_2","NumberofStation_1":"NumberofStation_1"}



#print out parthworth's for each level
estimates_of_choice = []
index = 0
for item in conjoint_attributes :
    print ("\n Attribute : " , effect_name_dict[item])
    print ("\n Importance : " , attribute_importance[index])
    print('    Level Part-Worths')
    for level in range(len(level_name[index])):
        print('       ',level_name[index][level], part_worth[index][level])
    index = index + 1

