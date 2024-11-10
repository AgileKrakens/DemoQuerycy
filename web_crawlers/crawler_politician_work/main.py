from prop_data import fetch_data
from database import init_db, insert_data

if __name__ == "__main__":
    init_db()
    
    url = 'https://camarasempapel.camarasjc.sp.gov.br//api/publico/proposicao/'
    autor_ids = [1137,1140,1141,1144,1145,1148,1151,1152,1156,1160,1274,3702,3703,3704,3705,3706,3707,3708,3709,3710,4140]
    anos = [2020,2021,2022,2023,2024]

    data=fetch_data(url, autor_ids, anos)
    
    insert_data(data)
