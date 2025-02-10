# Campus-Placement-Prediction
**Overview**:
The goal of this project is to predict whether a student will be placed in a job based on academic performance, work experience, and other factors. We will build and evaluate three different classification models to determine the best-performing model.
Dataset:
The dataset contains student records with the following key attributes:
•	Academic Performance: ssc_p (Secondary Education %), hsc_p (Higher Secondary %), degree_p (Degree %), mba_p (MBA %).
•	Education Background: ssc_b (Board type), hsc_b (Board type), hsc_s (Specialization), degree_t (Degree type).
•	Work Experience & Skills: workex (Yes/No), etest_p (Employability Test Score), specialisation (MBA specialization).
•	Target Variable: status (Placed/Not Placed).
•	Salary:  salary -  available only for placed students.

**Model Selection**
**Logistic Regression**:
Simplicity: Logistic regression is a simple model, making it ideal for small datasets. It doesn’t require a large amount of data to produce reliable results and can handle binary classification well.
Efficiency: It's computationally efficient and fast to train, which is beneficial when dealing with smaller datasets where you don't need overly complex models that may overfit. 
Interpretability: Logistic regression produces coefficients that show the direct influence of each feature on the outcome, making it easier to understand and interpret, especially when the number of features is small.

**Decision Tree**:
Non-Linear Relationships: Decision trees can capture complex relationships between features and the target variable. They are particularly useful when the data includes non-linear relationships, which could be the case with academic and categorical data.
Handles Categorical Data Well: Since your dataset includes categorical columns (e.g., HSC stream, work experience), decision trees can efficiently handle this type of data without the need for encoding (although one-hot encoding is used in your case).
Small Dataset Friendly: Decision trees are not prone to overfitting with small datasets, especially when hyperparameters like depth and minimum samples per leaf are tuned properly.

**Random Forest**:
Improved Performance: Random Forest improves on decision trees by averaging multiple trees' predictions, which helps reduce overfitting and increases the robustness of the model, especially with small datasets.
Handles Overfitting: Random Forest can mitigate the risk of overfitting (which small datasets are prone to) by combining multiple trees, each trained on a different subset of the data, which leads to better generalization.
Works with Limited Data: Random Forest performs well even with fewer columns and smaller datasets as it doesn't rely on a single model's performance but aggregates predictions from several models.

**App deployment**: [Visit App](https://campus-placement-prediction.streamlit.app/)
![image](https://github.com/user-attachments/assets/2fccb2cf-2317-4d57-9e72-f4ae693ed761)
