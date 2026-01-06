from clean_company import normalize_company_name

def run_tests():
    assert normalize_company_name("CAF softsol") == "CAF SoftSol India Pvt Ltd."
    assert normalize_company_name("CAF solution") == "CAF SoftSol India Pvt Ltd."
    assert normalize_company_name("CAF           softSolution  India Pvt Limited") == "CAF SoftSol India Pvt Ltd."
    assert normalize_company_name("") == ""
    assert normalize_company_name(None) == ""
    assert normalize_company_name("Other Company Pvt Ltd") == "Other Company Pvt Ltd"

    print("✅ All test cases passed successfully!")

if __name__ == "__main__":
    run_tests()
