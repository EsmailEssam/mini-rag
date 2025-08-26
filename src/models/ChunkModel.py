from .BaseDataModel import BaseDataModel
from .db_schemas.data_chunk import DataChunk
from .enums.DataBaseEnum import DataBaseEnum
from bson.objectid import ObjectId
from pymongo import InsertOne

class ChunkModel(BaseDataModel):
    def __init__(self, db_client:object):
        super().__init__(db_client)

        # set the collection
        self.collection = self.db_client[DataBaseEnum.COLLECTION_CHUNK_NAME.value]

    async def create_chunk(self, chunk: DataChunk):
        # create the chunk
        result = await self.collection.insert_one(chunk.model_dump(by_alias=True, exclude_none=True))

        # set the id
        chunk.id = result.inserted_id
        return chunk
    
    async def get_chunk(self, chunk_id:str):
        # get the chunk
        result = await self.collection.find_one({
            '_id': ObjectId(chunk_id)
        })

        if result is None:
            return None
        
        return DataChunk(**result)
    
    async def insert_many_chunks(self, chunks: list, batch_size: int=100):
        # insert chunks in batches
        for i in range(0, len(chunks), batch_size):
            # get the batch of chunks
            batch = chunks[i:i+batch_size]

            # create the operations
            operations = [InsertOne(chunk.model_dump(by_alias=True, exclude_none=True)) for chunk in batch]
            
            # insert the batch
            await self.collection.bulk_write(operations)
        
        return len(chunks)
    
    async def delete_chunks_by_project_id(self, project_id: ObjectId):
        # delete the chunks
        result = await self.collection.delete_many({
            "chunk_project_id": project_id
        })
        return result.deleted_count



