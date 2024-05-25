
def jwt_response_payload_handler(token, user=None, request=None):
    """
    Custom payload handler for JWT authentication.
    Modify the payload as needed.
    """
    return {
        
        # Include any additional data you want in the payload
        'id': id,
        
    }