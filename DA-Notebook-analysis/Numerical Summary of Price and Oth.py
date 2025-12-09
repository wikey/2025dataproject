# --- Numerical Summary of Price and Other Numeric Features ---
import pandas as pd

numeric_summary = df[['price','availability_365','days_since_last_review','description_length']].describe()
numeric_summary
