from scripts import transform as script

def test_data_colums():
    assert script.csv_data.columns == ['Country', 'Country_code', 'Date', 'Population_Value']
