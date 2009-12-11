import flickrapi

API_KEY = 'a8bfcd0834305fc8f2d51b401adbb87f'
SECRET_KEY = '353b6174d6aa4795'

flickr = flickrapi.FlickrAPI(API_KEY,SECRET_KEY)
(token,frob) = flickr.get_token_part_one(perms='write')
if not token:
    raw_input('enter')
flickr.get_token_part_two((token,frob))

flickr.upload("/home/laihj/workspace/photoTool/flickr/example.JPG")
