class Table:
    def __init__(self, name):
        self.name = name


class Field:
    def __init__(self, name_, type_, is_null_):
        self.name = name_
        self.type = type_
        self.is_null = is_null_


main_table = Table("WeatherTable")
Longitude = Field("Longitude", "Double", "NOT NULL")
Latitude = Field("Latitude", "Double", "NOT NULL")
forecast_time = Field("forecast_time", "datetime", "NOT NULL")
Precipitation_Rate_in_hr = Field("Precipitation_Rate_in_hr", "Double", "")
Temperature_Celsius = Field("Temperature_Celsius", "Double", "")


def create_table():
    query = f"""CREATE TABLE {main_table.name}(
                {Longitude.name} {Longitude.type} {Longitude.is_null},
                {Latitude.name} {Latitude.type} {Latitude.is_null},
                {forecast_time.name} {forecast_time.type} {forecast_time.is_null},
                {Precipitation_Rate_in_hr.name} {Precipitation_Rate_in_hr.type},
                {Temperature_Celsius.name} {Temperature_Celsius.type},
                 PRIMARY KEY ( {Longitude.name}, {Latitude.name}, {forecast_time.name} )
            )"""
    return query


def insert_to_db():
    query = "INSERT INTO {} VALUES (?,?,?,?,?)".format(main_table.name)
    return query


def forecast_by_loc():
    query = "select {} , {} , {} from {} " \
            "WHERE {} = ? and {} = ? ".format(forecast_time.name, Precipitation_Rate_in_hr.name,
                                              Temperature_Celsius.name, main_table.name, Longitude.name,
                                              Latitude.name)
    return query


def summarize_forecast():
    query = "select max({0}) , max({1})," \
                       "min({0}) , min({1})," \
                       "avg({0}) , avg({1}) " \
                       "from {2} " \
                       "WHERE {3} = ? and {4} = ? ".format(Temperature_Celsius.name,
                                                           Precipitation_Rate_in_hr.name,
                                                           main_table.name,
                                                           Longitude.name,
                                                           Latitude.name
                                                           )
    print("query: ", query)
    return query
