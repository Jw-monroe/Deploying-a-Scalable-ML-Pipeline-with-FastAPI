# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model was created by Jonathan Monroe on 6/14/25. This is a random forest Classifier model 
## Intended Use
The primary use case is to predict an individual's income above or below $50,000 based on their demographic and employment data.
## Training Data
The training data is from the census.csv fileand is comprised of  80% of the data.
## Evaluation Data
The evaluation data is comprised of a holdout test set from the census.CSV that constitutes the remaining 20% of the original data set.
## Metrics
_Please include the metrics used and your model's performance on those metrics._
Precision: 0.7519 | Recall: 0.6309 | F1: 0.6861
## Ethical Considerations
The ML model is learning from a data set from 1994. This machine learning model may  learn and perpetuate historical societal biases in the 1994s dataset possibly leading to discriminatory or unfair predictions. Additionally, income can be associated with multitude of other factors beyond education, occupation, relationship, and gender.
## Caveats and Recommendations
Performance on datasets, not from 1994 may cause the models performance to degrade. Additionally further year's data should be explored to refine the model.