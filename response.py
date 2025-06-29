from fastapi import HTTPException

class Response:

    def return_not_found(self):
        return HTTPException(status_code=404, detail="Icon not found")