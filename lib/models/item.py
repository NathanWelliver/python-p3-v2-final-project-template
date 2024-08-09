# lib/models/items.py
from models.__init__ import CURSOR, CONN
from models.bucket import Bucket

class Item:

    all ={}

    def __init__(self, title, description, bucket_id, id=None):
        self.id = id
        self.title = title
        self.description = description
        self.bucket_id = bucket_id

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError("title must be letters only and not empty")
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if (1 <= len(description) <= 40):
            self._description = description
        else:
            raise ValueError("description cant be blank")
    
    @property
    def bucket_id(self):
        return self._bucket_id
    
    @bucket_id.setter
    def bucket_id(self, bucket_id):
        if type(bucket_id) is int and Bucket.find_by_id(bucket_id):
            self._bucket_id = bucket_id
        else:
            raise ValueError("bucket_id must reference a bucket")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            bucket_id INTEGER,
            FOREIGN KEY (bucket_id) REFERENCES buckets(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS items;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO items (title, description, bucket_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.description, self.bucket_id))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE items
            SET title = ?, description = ?, bucket_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.description, self.bucket_id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM items
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    
    @classmethod
    def create(cls, title, description, bucket_id):
        item = cls(title, description, bucket_id)
        item.save()
        return item
    
    @classmethod
    def instance_from_db(cls, row):
        item = cls.all.get(row[0])
        if item:
            item.title = row[1]
            item.description = row[2]
            item.bucket_id = row[3]
        else:
            item = cls(row[1], row[2], row[3])
            item.id = row[0]
            cls.all[item.id] = item
        return item
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM items
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM items
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_title(cls, title):
        sql = """
            SELECT *
            FROM items
            WHERE title = ?
        """
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None