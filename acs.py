import json
import ast
test = "[['captcha_key', {'type': 'array', 'value': [{'type': 'string', 'value': 'captcha-required'}]}], ['captcha_sitekey', {'type': 'string', 'value': 'a9b5fb07-92ff-493f-86fe-352a2803b3df'}], ['captcha_service', {'type': 'string', 'value': 'hcaptcha'}], ['captcha_session_id', {'type': 'string', 'value': 'b0ca5338-92c9-4e24-bd0d-f2eaad383621'}], ['should_serve_invisible', {'type': 'boolean', 'value': True}], ['captcha_rqdata', {'type': 'string', 'value': 'vYu9sRqW63svYUhpiinvR7e64UnsSYXvxxE2zw/1h5mOgp556y8v5Cf726HiHPILBkMk1pK1TcfK1OQ3RYaz1hNdKxzRVHZf5exlK2v1ZngztZoiuvzaVmlrCvLFkTXsTc4jqKb8PlEq/OP25cECdAHyRQPM01ee23V1I6yxoZ2OewyYbLgVdicB0XoRalpx7xAn4pu0KbQBjWZa+HKE3Rn4'}], ['captcha_rqtoken', {'type': 'string', 'value': 'IitJeE16QXFobEFJYXRrOThvZHZqait5M1RzS2llQlNDSlhzS3VJSm9sTmZMQVRWQzQzQU9VMXRpUTVxSXlsQWhiRHdzYmc9PTVjdVFzT05CYVE5d3FldEsi.auntUA.AgEBlTV3_SheL4XjIW6pazbHDv0'}]]"
data = ast.literal_eval(test)[5][1]["value"]
print(data)
