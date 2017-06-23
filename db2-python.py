
# coding: utf-8

# In[ ]:

# date modified: 6/22/2017
import ibm_db
import pandas as pd


# In[ ]:

ibm_db_conn = ibm_db.connect("DATABASE=xx;HOSTNAME=xx;PORT=60000;PROTOCOL=TCPIP;UID=xx;PWD=xx;", "", "")


# In[ ]:

# to see the tables under a schema called SNICKERDOODLE
import ibm_db_dbi
conn=ibm_db_dbi.Connection(ibm_db_conn)
conn.tables('SNICKERDOODLE', '%')


# In[ ]:

# to run a query
sql = "SELECT INGREDIENT_ID FROM SNICKERDOODLE.INGREDIENTS WHERE TYPE='REGULAR';"
stmt = ibm_db.exec_immediate(ibm_db_conn,sql)
tuple_t = ibm_db.fetch_tuple(stmt)
while tuple_t != False:
    print tuple_t
    tuple_t = ibm_db.fetch_tuple(stmt)


# In[ ]:

# to save the result of query as a Pandas dataframe
df_ingredients = pd.DataFrame(columns=('INGREDIENT_ID', 'INGREDIENT_NAME'))
sql ="SELECT INGREDIENT_ID, INGREDIENT_NAME FROM SNICKERDOODLE.INGREDIENTS WHERE TYPE='REGULAR';"
i =0
while tuple_t != False:
    df_ingredients.loc[i] = list(tuple_t)
    if i%10 == 0:
        print i, ' rows have been added to dataframe'
    i = i + 1
    tuple_t = ibm_db.fetch_tule(stmt)


# In[ ]:

#sources:
#https://stackoverflow.com/questions/6044326/how-to-connect-python-to-db2
#https://www.ibm.com/support/knowledgecenter/en/SSSNY3_10.1.0/com.ibm.swg.im.dbclient.python.doc/doc/t0054388.html
#https://www.ibm.com/support/knowledgecenter/en/SSEPGG_9.5.0/com.ibm.db2.luw.apdv.python.doc/doc/t0054368.html
#https://stackoverflow.com/questions/10715965/add-one-row-in-a-pandas-dataframe

