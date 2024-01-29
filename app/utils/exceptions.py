from fastapi import HTTPException

NOT_AUTHORIZED = HTTPException(401, "Not authorized.")
NOT_ALLOWED = HTTPException(405, "Method not allowed.")
NOT_FOUND = lambda item_id="item_id": HTTPException(404, f"Item with {item_id} not found.")