"""
Video Model
Mengelola YouTube videos
"""
from app.models.BaseModel import BaseModel

class Video(BaseModel):
    """Video model untuk YouTube videos"""
    
    @classmethod
    def get_all_active(cls):
        """Get all active videos ordered by display_order"""
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT video_id, youtube_id, title, description, display_order, is_active
            FROM youtube_videos
            WHERE is_active = TRUE
            ORDER BY display_order ASC
        """)
        videos = cursor.fetchall()
        cursor.close()
        conn.close()
        return videos
    
    @classmethod
    def get_all(cls):
        """Get all videos (including inactive)"""
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT video_id, youtube_id, title, description, display_order, is_active, created_at, updated_at
            FROM youtube_videos
            ORDER BY display_order ASC
        """)
        videos = cursor.fetchall()
        cursor.close()
        conn.close()
        return videos
    
    @classmethod
    def get_by_id(cls, video_id):
        """Get video by ID"""
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT video_id, youtube_id, title, description, display_order, is_active
            FROM youtube_videos
            WHERE video_id = %s
        """, (video_id,))
        video = cursor.fetchone()
        cursor.close()
        conn.close()
        return video
    
    @classmethod
    def create(cls, youtube_id, title, description, display_order=0, is_active=True):
        """Create new video"""
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO youtube_videos (youtube_id, title, description, display_order, is_active)
            VALUES (%s, %s, %s, %s, %s)
        """, (youtube_id, title, description, display_order, is_active))
        video_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return video_id
    
    @classmethod
    def update(cls, video_id, youtube_id, title, description, display_order, is_active):
        """Update video"""
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE youtube_videos
            SET youtube_id = %s, title = %s, description = %s, 
                display_order = %s, is_active = %s
            WHERE video_id = %s
        """, (youtube_id, title, description, display_order, is_active, video_id))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    
    @classmethod
    def delete(cls, video_id):
        """Delete video"""
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM youtube_videos WHERE video_id = %s", (video_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    
    @classmethod
    def toggle_active(cls, video_id):
        """Toggle video active status"""
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE youtube_videos
            SET is_active = NOT is_active
            WHERE video_id = %s
        """, (video_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
