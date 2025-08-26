from features import classifier, extract_txt, structure_output
from scraping import stoex
from structure import databases, tables
from datetime import datetime

if __name__=='__main__':
    table_name = 'screener'

    columns = ['Date', #remove this after changing structure_output
               'Time', 
               'Company ID', 
               'Exchange', 
               'Market', 
               'Industry', 
               'Summary', 
               'Guidance', 
               'Strategy', 
               'Refinancing', 
               'Spin-off', 
               'Sale', 
               'Merger', 
               'Major cost reduction', 
               'Bankruptcy', 
               'Other', 
               'Price change',
               'Revenue',
               'Gross profit',
               'Operating profit',
               'Net profit',
               'Operating cash flow',
               'Cash and equivalents',
               'Debt']
    
    columns = ['Date', 
               'Time', 
               'Company ID', 
               'Exchange', 
               'Market', 
               'Industry', 
               'Summary', 
               'Guidance', 
               'Strategy', 
               'Restructurings', 
               'Price change',
               'Revenue',
               'Gross profit',
               'Operating profit',
               'Net profit',
               'Operating cash flow',
               'Cash and equivalents',
               'Debt']
    
    news_cols = ['Date', 
               'Time', 
               'Company ID', 
               'Exchange', 
               'Market', 
               'Industry', 
               'Summary']
    
    screener_cols = ['Date', 
               'Time', 
               'Company ID', 
               'Exchange', 
               'Market', 
               'Industry', 
               'Guidance', 
               'Strategy', 
               'Restructurings']
    
    mydb, mycursor = databases.access_db('jfyu_1&ofQnsp1^d6FJ', 'deltalert')

    #tables.drop_table(mycursor, table_name)
    #tables.add_table(mycursor, 'screener', columns)

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

    rows = tables.get_limited_rows(mycursor, table_name, 5, columns=news_cols)

    #print(rows)