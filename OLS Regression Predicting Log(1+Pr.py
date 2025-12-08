# --- OLS Regression Predicting Log(1+Price) ---
import statsmodels.formula.api as smf

# Example formula: include numeric + categorical predictors
formula = "log_price ~ availability_365 + days_since_last_review + description_length + C(room_type) + C(neighbourhood_group)"

ols_model = smf.ols(formula=formula, data=df).fit(cov_type='HC3')

print(ols_model.summary())
