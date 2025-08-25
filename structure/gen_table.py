from features import classifier, extract_txt, structure_output
from scraping import stoex
from structure import databases, tables
from datetime import datetime

if __name__=='__main__':
    table_name = 'screener'
    #mydb, mycursor = databases.init_db('jfyu_1&ofQnsp1^d6FJ')
    mydb, mycursor = databases.access_db('jfyu_1&ofQnsp1^d6FJ', 'deltalert')
    #databases.show_dbs(mycursor)

    #tables.drop_table(mycursor, table_name)
    #tables.add_table(mycursor, 'screener', ['Date', 'Time', 'Company ID', 'Country', 'Exchange', 'Market', 'Industry', 'Summary', 'Guidance', 'Strategy', 'Refinancing', 'Spin-off', 'Sale', 'Merger', 'Major Cost Reduction', 'Bankruptcy', 'Other', 'Price change'])
    #tables.show_tables(mycursor)

    #print(tables.get_columns(mycursor, 'screener'))

    #tables.add_column(mydb, mycursor, table_name, 'Summary')
    #tables.add_column(mydb, mycursor, table_name, 'Guidance')
    #tables.delete_column(mydb,mycursor,table_name,'Unknown')

    cols = tables.get_col_names(mycursor, table_name)
    #print(cols)

    with open('classification.txt', 'r', encoding='utf-8') as classification:
        s, r = structure_output.structure_output(classification.read())

    #print(s)
    
    now = datetime.now()
    current_date = now.date()
    current_time = now.strftime("%H:%M:%S")
    
    row = (current_date, current_time, 'Lindex 4', 'Finland', 'Helsinki', 'Mid Cap', 'Retail')
    for col in cols[7:-1]:
        row += (s[col],)
    #print(row)
    row += (5,)
    tables.insert(mydb, mycursor, table_name, [row])

    #print(tables.get_columns(mycursor,table_name, ['Summary', 'Guidance', 'Spin-off']))

    rows = tables.get_limited_rows(mycursor, table_name, 5, columns=['Date', 'Summary', 'Guidance'])

    print(rows)