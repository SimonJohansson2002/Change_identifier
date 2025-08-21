from features import classifier, extract_txt, structure_output
from scraping import stoex
from structure import databases, tables

if __name__=='__main__':
    table_name = 'screener'
    #mydb, mycursor = databases.init_db('jfyu_1&ofQnsp1^d6FJ')
    mydb, mycursor = databases.access_db('jfyu_1&ofQnsp1^d6FJ', 'deltalert')
    #databases.show_dbs(mycursor)

    #tables.add_table(mycursor, 'screener', ['Date', 'Time', 'Company ID', 'Country', 'Exchange', 'Market', 'Industry', 'Sentiment', 'Strategy', 'Refinancing', 'Spinoff', 'Sale', 'Merger', 'Major cost reduction', 'Bankruptcies', 'Unknown', 'Price change'])
    #tables.show_tables(mycursor)

    #tables.content_table(mycursor, 'screener')
    tables.add_column(mydb, mycursor, table_name, )
    cols = tables.get_col_names(mycursor, table_name)
    print(cols)