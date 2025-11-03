-- =====================================================
-- ADD YOUTUBE VIDEOS TABLE
-- Tabel untuk mengelola video YouTube yang ditampilkan di Home page
-- =====================================================

USE virtualtour1;

-- Create videos table
CREATE TABLE IF NOT EXISTS youtube_videos (
    video_id INT(10) AUTO_INCREMENT PRIMARY KEY,
    youtube_id VARCHAR(50) NOT NULL COMMENT 'YouTube video ID',
    title VARCHAR(255) NOT NULL COMMENT 'Video title',
    description TEXT COMMENT 'Video description',
    display_order INT(10) NOT NULL DEFAULT 0 COMMENT 'Order of display (0 = first)',
    is_active BOOLEAN NOT NULL DEFAULT TRUE COMMENT 'Whether video is shown',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    INDEX idx_display_order (display_order),
    INDEX idx_active (is_active)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insert default videos
INSERT INTO youtube_videos (youtube_id, title, description, display_order, is_active) VALUES
('dQw4w9WgXcQ', 'Virtual Tour Demo - Museum Experience', 'Lihat bagaimana teknologi virtual tour kami memberikan pengalaman immersive', 1, TRUE),
('dQw4w9WgXcQ', 'Real Estate Virtual Tour', 'Jelajahi properti dengan teknologi 360-degree walkthrough', 2, TRUE),
('dQw4w9WgXcQ', 'Virtual Art Gallery Showcase', 'Pameran seni virtual dengan detail tinggi dan interaktif', 3, TRUE);
