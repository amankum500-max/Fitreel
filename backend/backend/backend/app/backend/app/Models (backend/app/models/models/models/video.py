from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    title = Column(String(200), nullable=False)
    description = Column(Text, default="")
    mux_asset_id = Column(String, index=True)
    mux_playback_id = Column(String)
    thumbnail_url = Column(String, default="")
    duration = Column(Integer, default=0)  # seconds
    views = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
