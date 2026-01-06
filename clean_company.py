import pandas as pd
import re

def normalize_company_name(company_name):
    # Handle empty or NaN values
    if pd.isna(company_name) or not str(company_name).strip():
        return ""

    # Convert to lowercase and remove extra spaces
    name = re.sub(r"\s+", " ", str(company_name).lower()).strip()

    # Normalize CAF company variations
    if "caf" in name:
        return "CAF SoftSol India Pvt Ltd."

    # Default fallback
    return str(company_name).strip().title()


# -------- MAIN EXECUTION --------
if __name__ == "__main__":
    # Read Excel file
    df = pd.read_excel("employee.xlsx")

    # Apply normalization on CompanyName column
    df["CompanyName"] = df["CompanyName"].apply(normalize_company_name)

    # Save cleaned Excel
    df.to_excel("employee_cleaned.xlsx", index=False)

    print("✅ Company names cleaned successfully!")
    print("📁 Output file created: employee_cleaned.xlsx")