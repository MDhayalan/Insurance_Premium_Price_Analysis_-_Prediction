Problem statement:
From the given dataset, need to do the EDA and predict the premium price.

Steps involved:
1. Preliminary analysis of the dataset

2. Outlier detection

3. Visual analysis
	i. Univariate analysis
	ii. Multi-variate Analysis

4. Statistical analysis

5. ML Model
	i. ML preprocessing
	ii. Model training & evalution
	iii.Exporting pickle file - Final model for deployment

6. Overall insights
	👉 Older - Obese and overweight people are got higher premium price. 

	👉 Younger - Normal and underweight people are got lower premium price.

	👉 Those people have gone for any transplants surgery, got the higher premium price.

	👉 People who are more than 60years old have gone through 3 major surgeries. And their premium prices are same 28K.

	👉 For 2 major surgeries, around the age of 50 to 60 years old, their premium amount is also same 28K.

	👉 Age and premium price are highly co-related.

	👉 From the statistical test, except the Known Allergies all other Diabetes, Blood pressure, Transplants, Chronic diseases and History of Cancer in Family have significant difference in Premium Price, which means they are the factors impacting the premium price.

	👉 Both BMI and Age groups have significant impact on the premium price.

	👉 Except the known allergies, then the rest are have significant association with the Premium price.

7. Streamlit deployment