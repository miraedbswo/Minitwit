def make_parameter(name: str, discription: str, param_type='str', required=True):
    return {
        'name': name,
        'description': discription,
        'in': 'json',
        'type': param_type,
        'required': required
    }


SAMPLE_ACCESS_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDA5Njc2MzYsIm5iZiI6MTU0MDk2NzYzNiwianRpIjoiZjh'
SAMPLE_REFRESH_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDA5Njc2MzYsIm5iZiI6MTU0MDk2NzYzNiwianRpIjoiND'

jwt_header = {
    'name': 'Authorization',
    'description': 'JWT Token(Bearer ***)',
    'in': 'header',
    'type': 'str',
    'required': True
}
