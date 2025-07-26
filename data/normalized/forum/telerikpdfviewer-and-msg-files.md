# TelerikPdfViewer and .msg files

## Question

**Tob** asked on 30 Mar 2023

Hello, I have a blazor app which consumes an API that sends documents as byte arrays. In the header is the file name, so I can determine what sort of file it is. I am currently using the following: DocxFormatProvider DocFormatProvider TxtFormatProvider RtfFormatProvider Which works great, for me to get a byte array that can be used with the TelerikPdfViewer. The issue I have is, that some of the documents are email messages, specifically .msg files. There isn't a provider for Msgs, so I wondered if anyone had a work around, to be able to show the file in the browser? I cannot save the file as a .msg, I can only use the byte array. Thanks

### Response

**Dimo** commented on 04 Apr 2023

@Toby - the way I see it, you can select some third-party tool to read (parse) the msg file, or do that manually, based on the specification. Once you have the parsed content, import it to one of our format providers.

### Response

**Toby** commented on 04 Apr 2023

Thanks for your reply. The issue I have is, the .msg is a byte array, I do not have it as a file saved on disk, so reading it isn't a possibility without saving, which is what I was hoping to avoid. It could be that I have no other option, but to save it, and then parse it. I just wondered if anyone had solved the issue, as the Telerik tools are great, in that they allow me to just use the byte array I receive, without the need to save them.

### Response

**ReverseBLT** commented on 21 Jun 2024

Hello Toby - I apologize as I have nothing to help you but I was actually wondering if you could help me haha. I was wondering if you could share your implementation of reading Doc, Txt, etc. files and viewing them in the PDF viewer. Currently trying the same thing but the PDF viewer just remains blank, not quite sure what I am doing wrong.
