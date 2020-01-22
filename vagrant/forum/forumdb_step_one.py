import psycopg2
import bleach


DBNAME = "forum"

def get_posts():
    """Return all posts from the 'database' """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select content , time from posts order by time desc")
    posts = c.fetchall()
    db.close()
    return posts

def add_post(content):
    """Add a post to the 'database' """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("insert into posts values (%s)",  (bleach.clean(content, strip=True),))
    db.commit()
    db.close()