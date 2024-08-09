# lib/models/buckets.py
from models.__init__ import CURSOR, CONN

class Bucket:
    
    all = {}

    def __init__(self, name, id=None):
        self.name = name
        self.id = id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("name must be letters only and not empty")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS buckets (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS buckets;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql= """
            INSERT INTO buckets (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name):
        bucket = cls(name)
        bucket.save()
        return bucket
    
    def update(self):
        sql = """
            UPDATE buckets
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM buckets
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        bucket = cls.all.get(row[0])
        if bucket:
            bucket.name = row[1]
        else:
            bucket = cls(row[1])
            bucket.id = row[0]
            cls.all[bucket.id] = bucket
        return bucket
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM buckets
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM buckets
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM buckets
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def items(self):
        from models.item import Item
        sql = """
            SELECT * FROM items
            WHERE bucket_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        return [Item.instance_from_db(row) for row in rows]
