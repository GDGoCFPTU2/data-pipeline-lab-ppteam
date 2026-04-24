from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp). 
    TODO: Khai báo các trường với kiểu dữ liệu str ở dưới.
    """
    document_id: str = Field(..., description="Unique identifier of the source document")
    source_type: str = Field(..., description="Data source type, e.g. PDF or Video")
    author: str = Field(..., description="Document/video author or creator")
    category: str = Field(..., description="Content category label")
    content: str = Field(..., description="Normalized content body")
    timestamp: str = Field(..., description="Creation or publish timestamp")
