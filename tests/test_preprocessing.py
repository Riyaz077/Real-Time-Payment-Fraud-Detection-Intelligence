import pandas as pd, pytest
from src.sentinelpay.preprocessing import validate_transactions
def test_missing_columns_raise():
    with pytest.raises(ValueError):
        validate_transactions(pd.DataFrame({"amount":[10]}))
