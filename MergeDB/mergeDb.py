import sqlite3

# 拿出指定表的所有行数据
def select_all_fromtable(tablename, dbpath):
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    result_list = []
    tablename = '"' + tablename + '"'
    
    sql = '''
    select * from (%s)
    '''%tablename
    result = cur.execute(sql)
    for item in result:
        result_list.append(item)
    
    cur.close()
    conn.close()
    
    return result_list

# 将pyhon字符串转换成sql能识别的字符串
def trans2sql(datalist):
    for index in range(len(datalist)):
        datalist[index] = '"' + str(datalist[index]).replace('"', '""').replace("'", "''") + '"'
    return datalist

def merge2Db(targetdb, selectdb):
    conn = sqlite3.connect(targetdb)
    
    cur = conn.cursor()
    actors_list = select_all_fromtable("actors", selectdb)
    editors_list = select_all_fromtable("editors", selectdb)
    basic_list = select_all_fromtable("basic", selectdb)
    comments_list = select_all_fromtable("comments", selectdb)
    reviews_list = select_all_fromtable("reviews", selectdb)
    
    for actors in actors_list:
        actors = trans2sql(list(actors))
        sqlactors = '''
        insert into actors (
            IMDb,
            actor_name
        )values (%s)
        '''%",".join(actors)
        cur.execute(sqlactors)
    
    for editors in editors_list:
        editors = trans2sql(list(editors))
        sqleditors = '''
        insert into editors (
            IMDb,
            editor_name
        )values (%s)
        '''%",".join(editors)
        cur.execute(sqleditors)
    
    for basic in basic_list:
        basic = trans2sql(list(basic))
        sqlbasic = '''
        insert into basic (
            IMDb,
            cname,
            fname,
            pic_link,
            director,
            classes,
            location,
            language,
            uptime,
            length,
            other_name,
            score,
            rated,
            instruction,
            comments_count,
            reviews_count
        )values (%s)
        '''%",".join(basic)
        cur.execute(sqlbasic)
    
    for comments in comments_list:
        comments = trans2sql(list(comments))
        sqlcomments = '''
        insert into comments (
            IMDb,
            nickname,
            commenttime,
            content,
            count_useful
        )values (%s)
        '''%",".join(comments)
        cur.execute(sqlcomments)
    
    for reviews in reviews_list:
        reviews = trans2sql(list(reviews))
        sqlreviews = '''
        insert into reviews (
            IMDb,
            nickname,
            commenttime,
            content,
            count_useful,
            count_useless,
            count_response
        )values (%s)
        '''%",".join(reviews)
        cur.execute(sqlreviews)
        
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    merge2Db("movie_total.db", "./moviedb/movie_total11000-11999.db")
    print("合并成功")
    
    
    
    
    
    