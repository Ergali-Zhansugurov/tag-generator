from internal.db.postgres import get_connection
from internal.core.interfaces.tag_repo import TagRepositoryInterface

class TagRepositoryPostgres(TagRepositoryInterface):
    def save_tags(self, tags: list[str]):
        """Сохраняет уникальные теги в таблицу tags"""
        query = """
            INSERT INTO tags (tag) 
            VALUES (%s) ON CONFLICT (tag) DO NOTHING
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                for tag in tags:
                    cur.execute(query, (tag,))
                    
    def save_book_tags(self, book_id: int, tags: list[str]):
        """Сохраняет связи книги с тегами"""
        query = """
            INSERT INTO book_tags (book_id, tag_id)
            SELECT %s, id FROM tags WHERE tag = %s
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                for tag in tags:
                    cur.execute(query, (book_id, tag))