from intasend import APIService

API_PUBLISHABLE_KEY = 'ISPubKey_test_ae77275c-1ebd-43fe-aff8-f26efab9b237'
API_TOKEN = 'ISSecretKey_test_d3a541ce-9bb6-4f79-bd8b-9f6eb94e6e8a'

service = APIService(token=API_TOKEN, publishable_key=API_PUBLISHABLE_KEY, test=True)

create_order = service.collect.mpesa_stk_push(phone_number='254712345678', email='test@gmail.com', amount=100,
                                              narrative='Purchase of items')

print(create_order)