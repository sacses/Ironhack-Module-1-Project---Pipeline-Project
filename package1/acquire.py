import pandas as pd
from sqlalchemy import create_engine


def acquire():
    sql = \
    "SELECT rank_info.id, rank_info.name as fullName, rank_info.position,personal_info.lastName,\
    personal_info.age, personal_info.gender, personal_info.country, personal_info.image,\
    business_info.Source as source, business_info.worth, business_info.worthChange,\
    business_info.realTimePosition \
    FROM rank_info \
    LEFT JOIN personal_info \
    ON rank_info.id = personal_info.id \
    LEFT JOIN business_info \
    ON rank_info.id = business_info.id \
    ORDER BY rank_info.position DESC"

    engine = create_engine('sqlite:///../data/raw/frantamarit.db')

    df_master = pd.read_sql_query(sql, engine)
    return df_master


if __name__ == "__main__":
    df_master()
