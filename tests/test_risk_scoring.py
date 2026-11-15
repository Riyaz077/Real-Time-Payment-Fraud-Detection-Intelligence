from src.sentinelpay.risk_scoring import risk_score
def test_score_bounds():
    assert risk_score(0,0)["risk_score"] == 0
    assert risk_score(1,1)["risk_score"] == 100
def test_high_band():
    assert risk_score(.9,.9)["risk_band"] == "CRITICAL"
