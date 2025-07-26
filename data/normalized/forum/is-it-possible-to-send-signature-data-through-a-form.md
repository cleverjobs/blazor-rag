# Is it possible to send Signature data through a Form?

## Question

**Kez** asked on 20 Feb 2023

Basically I'm using the Signature component inside of the Form component, so of course I want the signature to be sent to my database. The only problem is, the string is way too long and causing the error 414. Does anyone know of a way to resolve this?

### Response

**Hristian Stefanov** commented on 23 Feb 2023

Hi Kezi, I'm ready to help. Based on the error type ( 414 ), I assume that you are using somehow GET request upon submission. Can you please confirm? If that is the case, you need to change it to a POST method because the GET is not designed to handle such long queries. The server of the project also needs its settings configured to support large files. Here are some examples (that you may know) of common server settings: IIS maxAllowedContentLength (also check the requestLimits article and this StackOverflow thread ) ASP.NET Core MultipartBodyLengthLimit Kestrel web server MaxRequestBodySize Additionally, here are some more articles that I found on the internet regarding error 414 you may find helpful: How to Fix the 414 Request-URI Too Large Error 414. The request URL is too long. asp.net I look forward to hearing your feedback.

### Response

**Kezi** commented on 23 Feb 2023

Thank you! I figured it out. If I may ask a follow up question, do you know how I would add the signature back to a Telerik Report in it's image format (not base64)?

### Response

**Hristian Stefanov** commented on 28 Feb 2023

Hi Kezi, I'm glad to see that you've figured it out. Now let me cover the last question as well. To add the signature in image format to a Telerik Report, here is an article from our documentation that gives you all the needed information to achieve the desired result: PictureBox Report Item Overview. Kind Regards, Hristian
