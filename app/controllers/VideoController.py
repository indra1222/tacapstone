"""
Video Controller
Handle YouTube video management
"""
from flask import jsonify, request
from app.models.Video import Video

class VideoController:
    """Controller untuk mengelola YouTube videos"""
    
    @staticmethod
    def get_all_videos():
        """Get all videos (for public display - active only)"""
        try:
            videos = Video.get_all_active()
            return jsonify({
                'success': True,
                'videos': videos
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Error fetching videos: {str(e)}'
            }), 500
    
    @staticmethod
    def get_all_videos_admin():
        """Get all videos (for admin - including inactive)"""
        try:
            videos = Video.get_all()
            return jsonify({
                'success': True,
                'videos': videos
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Error fetching videos: {str(e)}'
            }), 500
    
    @staticmethod
    def get_video(video_id):
        """Get single video by ID"""
        try:
            video = Video.get_by_id(video_id)
            if not video:
                return jsonify({
                    'success': False,
                    'message': 'Video not found'
                }), 404
            
            return jsonify({
                'success': True,
                'video': video
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Error fetching video: {str(e)}'
            }), 500
    
    @staticmethod
    def create_video():
        """Create new video"""
        try:
            data = request.get_json()
            
            # Validate required fields
            required_fields = ['youtube_id', 'title']
            for field in required_fields:
                if field not in data:
                    return jsonify({
                        'success': False,
                        'message': f'Missing required field: {field}'
                    }), 400
            
            youtube_id = data['youtube_id']
            title = data['title']
            description = data.get('description', '')
            display_order = data.get('display_order', 0)
            is_active = data.get('is_active', True)
            
            video_id = Video.create(youtube_id, title, description, display_order, is_active)
            
            return jsonify({
                'success': True,
                'message': 'Video created successfully',
                'video_id': video_id
            }), 201
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Error creating video: {str(e)}'
            }), 500
    
    @staticmethod
    def update_video(video_id):
        """Update video"""
        try:
            data = request.get_json()
            
            # Check if video exists
            video = Video.get_by_id(video_id)
            if not video:
                return jsonify({
                    'success': False,
                    'message': 'Video not found'
                }), 404
            
            # Validate required fields
            required_fields = ['youtube_id', 'title', 'display_order']
            for field in required_fields:
                if field not in data:
                    return jsonify({
                        'success': False,
                        'message': f'Missing required field: {field}'
                    }), 400
            
            youtube_id = data['youtube_id']
            title = data['title']
            description = data.get('description', '')
            display_order = data['display_order']
            is_active = data.get('is_active', True)
            
            Video.update(video_id, youtube_id, title, description, display_order, is_active)
            
            return jsonify({
                'success': True,
                'message': 'Video updated successfully'
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Error updating video: {str(e)}'
            }), 500
    
    @staticmethod
    def delete_video(video_id):
        """Delete video"""
        try:
            # Check if video exists
            video = Video.get_by_id(video_id)
            if not video:
                return jsonify({
                    'success': False,
                    'message': 'Video not found'
                }), 404
            
            Video.delete(video_id)
            
            return jsonify({
                'success': True,
                'message': 'Video deleted successfully'
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Error deleting video: {str(e)}'
            }), 500
    
    @staticmethod
    def toggle_video_active(video_id):
        """Toggle video active status"""
        try:
            # Check if video exists
            video = Video.get_by_id(video_id)
            if not video:
                return jsonify({
                    'success': False,
                    'message': 'Video not found'
                }), 404
            
            Video.toggle_active(video_id)
            
            return jsonify({
                'success': True,
                'message': 'Video status toggled successfully'
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Error toggling video status: {str(e)}'
            }), 500
