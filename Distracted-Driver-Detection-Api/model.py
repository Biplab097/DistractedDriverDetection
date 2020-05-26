import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
from google.colab import drive
drive.mount('/content/gdrive')
















# # Auto-iterate through all files that matches this query
# file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
# for file1 in file_list:
#     print('title: %s, id: %s' % (file1['title'], file1['id']))
# //{
# //  "type": "service_account",
# //  "project_id": "groovy-electron-275208",
# //  "private_key_id": "3370332633c8cc66f928c9eedc55de3aaa440cdf",
# //  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC+GttUJkMPEgoZ\nRZCurRwV9rqd5sZ+ZqK5mI7EbdVEPVNgd6Jc0T4RZYFoA6UjyYWo0u9VYtkT+RHr\nx2GEU1mCNvw9PeFGuUxRYxuUesrTepLv9Na3+az/4gC1wgluiVGbQuJxk4Rm1+4g\nl7TlAX1jjpumfOUjD8GEQdRdF8yGO0eYSrmgVNZyi+N4O20wTbHS7jfekVABqL0Z\n64vqP9yJTjzqQ/2sxqWSko2VUW9ri/mMDSB9ARuDuEwAxuT50PO8gtCJjfNofZ9a\no+bUdz3pTV2t62XRJaqDCsmSx5AtyN+dU5EUbAxTDIGBuINlMxu8kxRRwWr2KwnY\nN8C4YP8pAgMBAAECggEAAdK3HMD7LqdRInnoz8wIM2u40W/XonmwgNAmOlsFSxC9\nfnTXQUWeb0NGcO1sBYJWvk47jlmS1F60ncq9NCwqdRW66Ilx4iA/y54EMzHURR/t\nTdDOyFfkIVYVBKk2NvGpLzB+hHFSOTxD49sgmHuhrLU+5+NVvTbW98I726KxSu49\nX1EHIXVcZez57QHYOXLSZmutTcbo+4IYWSvJjGSsFAfi7u1Bu+gkQovRWtBUIcBN\nYHm0xUmEC+7hR4mn26PbKK9dMJ5YWqi05mYxy6QTWzrZ7P/iTxqFT+G6JtVxoiCS\nAFoPwz92nFrAFNfEn54LZwfxNqwBhKFpQYaJLmj96QKBgQDjdMkRd9NJgi1ihwsU\nyMGY60l4QlIS+801GpcKnVV5+ExJsRSu11fk2KvUq1qlBjMbAJUI5pmz5+f7heJS\njZAf4e+S4lWN+unOAtJp45/XohfmKKr4vAAmRubmgAdUcHLbqsMNmYYtS2hc+4L3\n6mWJKlyML99M+FuCxaLhLVaCxQKBgQDV9iGNE7x3cB1ko+RJNtqRX10sLfroIVHq\ndc4AG1Yh7HcRpQwCZRAv2QeNRvYzp8RZcSnJYo7HWXNb6yK7CMe7Zd5xL6hriUAW\n85RPl3zFq4dGS7GI/S8fdpMSTCTaxMnYZWcfw7dKbr/d0QN1U9XqHSwLpmBPBI9r\nztkD0QeBFQKBgCMz7PaeI/5Jfnq0SdvComvnZmyNXyR/AiiI3/2NkjAZZL03Aet5\neqn5esakapgF2J0CPw6smfdFGhtMglWigT7d+fUywGkD/3GZ8DThPNjjxm0huCxc\n9Gz4Jj5gbEH+UVh8Gkodi62w8QsLBh8WkPZkrwQnWJkSCx+3NNlC6hO9AoGBAIth\ntMeXlM3lznASSBPd1RKgoiy2o1323sszBQiSxlCBH6vx7dndhmb1JfNFx/ssjj+J\n9aPIPaTlw72cdtqKxLpyiS8I0dmD5qlM8k/LKrAGprAHfVb1QG5pqzNfQR721VrP\n7BcIQ24MqZbRo0QaYh8J8/h+4Px4xwl/DWZsFExlAoGBALiq20IEWEcJWSkht3kf\nOqHfdhTnIVMkWlvTFpyuwwJTpkW3N/FKX7fVRTeUOHXlJgR05wm+q6IyAScWS5dt\n1KbkJ9cE6YtKyjhLSJLJ/Yop4pXRDZ6qvjmmwpCUscbXl+GqRnAAB39cdNLt18Cy\ndIMntWv6snXS6IDj78D7qzk4\n-----END PRIVATE KEY-----\n",
# //  "client_email": "distracteddriver@groovy-electron-275208.iam.gserviceaccount.com",
# //  "client_id": "118152704239202210189",
# //  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
# //  "token_uri": "https://oauth2.googleapis.com/token",
# //  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
# //  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/distracteddriver%40groovy-electron-275208.iam.gserviceaccount.com"
# //}