import json
from websocket import create_connection
import ssl
import time
import pyautogui

thought = ""
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6ImNvbS56YWJpcl9uYWJpbC5icmFpbmVjdCIsImFwcFZlcnNpb24iOiIxLjAiLCJleHAiOjE1NjY0OTM3OTcsImxpY2Vuc2VJZCI6ImZlMWZmMGU3LTc5YzgtNDEzZC1hOGVhLTg4Mzg2OTEyYWMxOCIsIm5iZiI6MTU2NjIzNDU5NywidXNlcklkIjoiMGFiOWY3OTUtNWFhZS00MTMxLWE1MTAtMTJlOTYzNzY4MTM4IiwidXNlcm5hbWUiOiJ6YWJpcl9uYWJpbCIsInZlcnNpb24iOiIyLjAifQ==.HAiIVLj4h9GrsioJ7E8+PXB/ItfBup79pap4dkzIt6g="