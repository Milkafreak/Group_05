"""System module."""
def add_emission(data):
    '''
    Add column emssions that contain emission which is the total C02 emissions in tonnes of C02
    Parameters
    ------------
    Datafame
    Returns
    ---------
    Nothing
    Example
    ---------
    emission(data)
    with data being a dataframe.
    '''
    emission_list = {
    "Biofuel":1450,
    "Coal":1000,
    "Gas":455,
    "Hydro":90,
    "Nuclear":5.5,
    "Oil":1200,
    "Solar":53,
    "Wind":14
    }
    if "emissions" not in data.columns:
        data["emissions"] = data["biofuel_consumption"] * emission_list["Biofuel"] \
        + data["coal_consumption"] * emission_list["Coal"] \
        + data["gas_consumption"] * emission_list["Gas"] \
        + data["hydro_consumption"] * emission_list["Hydro"] \
        + data["nuclear_consumption"] * emission_list["Nuclear"] \
        + data["oil_consumption"] * emission_list["Oil"] \
        +data["solar_consumption"] * emission_list["Solar"] \
        + data["wind_consumption"] * emission_list["Wind"]
        data["emissions"] = data["emissions"] * 1e3
    else:
        print("Column emissions already exists")
        