'''
Created on Dec 23, 2016

@author: qs
'''
# -*- coding: utf-8 -*- 




from ql.parse import lexer
from ql.parse import parser
from ply.lex import  lex
from ply.yacc import yacc




from ql.dsl.Query import Query
from ql.dsl.Response import response
import sys
import json



def exec_stmt(stmt):
    
    my_lexer=lex(module=lexer,optimize=True,debug=True)
       
    my_parser=yacc(debug=True,module=parser)
    
    val = my_parser.parse(lexer=my_lexer.clone(),debug=False,input=sql)
    
    query = Query(val)
            
    from elasticsearch import Elasticsearch
    
    es = Elasticsearch([{'host':"10.68.23.81","port":9201}])
    
    
    print(json.dumps(query.dsl()))
    
    res = es.search(index=query._index, doc_type = query._type, body=query.dsl(), request_timeout=100)
    
#     print(json.dumps(res,indent=4))
    
    stmt_res = response(res)
    
    print(json.dumps(stmt_res,indent=4))




if __name__ == "__main__":
    


    if len(sys.argv) < 2:
        sqls = [
            
#         '''create table my_tb (
#             a text,b integer, 
#             c object as (
#                 raw string (index=yes,ppp=yes),
#                 obj object as (
#                     ddd string (index=yes,ppp=yes)
#                 )
#             )
#         ) with meta (
#             _parent (type='people')
#         ) with option (
#             index.number_of_shars=10,
#             index.flush_inteval='10s'
#         );''',
#          
#          
#        '''select * from test.info where a = hello or b between 10 and 20 and ( b = 20 or c = 10) limit 0,10 order by a asc,b,c desc;''',
#         '''select * from my_index02;''',       
        '''select count(*) as c,count(*) as cc ,sum(dd) as dd,moving_avg({buckets_path=c,window=30,model=simple}), moving_avg({buckets_path=dd,window=30,model=simple})  from my_index02 group by name,date_histogram({field=ts,interval='1h'});''',
#        '''select * from my_index where a = hello;''',
#         '''select * from my_index where city is not null and city = '\\'my_hello\\'hello'  and city between 3717 and 3718 order by city group by 
#         data_range(a,{format='MM-yyyy'},{ranges=[{to = 'now-10M/M' },{from =  'now-10M/M'}]}),b limit 1000;''',
        
#        '''select * from my_index group by date_range(timestamp,{ranges=[{'to'='now+10M'},{'from'='now'}]});''',
      
#        '''select * from my_index group by date_range(timestamp,'{"ranges":[{"to":"now+10M"},{"from":"now"}]}');''',
#        '''select * from my_index group by date_range({field=timestamp,'ranges'=[{'to'='now+10M'},{'from'='now'}]});''',

        
#        '''select sum(a) as tt from  my_index@beijing group by date_histogram({field=timestamp},{interval=day});''',
        
#        '''select sum(a) as tt,moving_avg({buckets_path=tt,window=30,model=simple}) as the_move  from  my_index group by date_histogram({field=timestamp},{interval=day});''',
        
#        '''select sum(a) as tt,derivative({buckets_path=tt}) as the_derivative  from  my_index group by date_histogram({field=timestamp},{from=day});''',
        
#          '''select sum.a(id) as sum,a as b from test.info group by a,date_histogram(my_date,{interval='1d'},['test','ttt'],'hello world',10);''',
#   
#   
#         '''insert into my_index (name,age,address,message) values ('zhangsan',24,{address='zhejiang',postCode='330010'},['sms001','sms002']);''',
#   
#         '''bulk into my_index(name,age,address,message) values 
#             [('zhangsan',24,{address='zhejiang',postCode='330010'},['sms:001','sms:002']),
#             ('zhangsan',25,{address='zhejiang',postCode='330010'},['sms:001','sms:002'])];''',
#   
#         '''update my_index set name = 'lisi' ,age = 30,address={address='shanghai',postCode='330010'} where _id = 330111111;''',
#           
#         '''upsert into my_index (_id,name,age,address,message) values (330001,'zhangsan',24,{address='zhejiang',postCode='330010'},['sms:001','sms:002']);''',
#           
#         '''delete from my_test.info where _id = 330111111;''',
#         
#         
#         '''explain create table my_tb (
#             a text,b integer, 
#             c object as (
#                 raw string (index=yes,ppp=yes),
#                 obj object as (
#                     ddd string (index=yes,ppp=yes)
#                 )
#             )
#         ) with meta (
#             _parent (type='people')
#         ) with option (
#             index.number_of_shars=10,
#             index.flush_inteval='10s'
#         );''',
        ]

        for sql in sqls:
            exec_stmt(sql)
                
    else: 
        sql = sys.argv[1]
        exec_stmt(sql)
        
        
