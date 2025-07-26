# POST firing before completion

## Question

**Min** asked on 08 Sep 2020

Unsure if this is related to uploading large files considering the issue is not seen when uploading <500mb files but when attempting to upload a 600mb file, the POST method is firing before the file even reaches 50% upload resulting in a null IEnumerable<IFormFile>. When the file does finish its upload, the completion handler fires immediately. Thanks, Minh

## Answer

**Minh** answered on 08 Sep 2020

Image attached which hopefully explains the issue a lot easier.

### Response

**Minh** answered on 08 Sep 2020

Looks like I was hasty with this post. Adding a the "MultipartBodyLengthLimit" attribute to the POST method fixed the issue. [RequestFormLimits(ValueLengthLimit=int.MaxValue, MultipartBodyLengthLimit=int.MaxValue)]
