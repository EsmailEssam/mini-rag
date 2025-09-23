from enum import Enum

class ResponseSignal(Enum):
    
    FILE_VALIDATED_SUCCESS = "File validated successfully"
    FILE_TYPE_NOT_SUPPORTED = "File type not supported"
    FILE_SIZE_EXCEEDS = "File size exceeds the maximum allowed size"
    FILE_UPLOAD_SUCCESS = "File uploaded successfully"
    FILE_UPLOAD_FAILED = "File upload failed"
    FILE_PROCESS_FAILED = "File processing failed"
    FILE_PROCESS_SUCCESS = "File processing successful"
    FILE_ID_ERROR = "No file found with the given id"
    NO_FILES_ERROR = "No files found"
    PROJECT_NOT_FOUND_ERROR = "Project not found"
    INSERT_INTO_VECTORDB_FAILED = "Insert into vectordb failed"
    INSERT_INTO_VECTORDB_SUCCESS = "Insert into vectordb successful"
    VECTORDB_COLLECTION_RETRIEVED = "Vectordb collection retrieved"
    VECTORDB_SEARCH_ERROR = "Vectordb search error"
    VECTORDB_SEARCH_SUCCESS = "Vectordb search successful"
    RAG_ANSWER_ERROR = "Rag answer error"
    RAG_ANSWER_SUCCESS = "Rag answer successful"
