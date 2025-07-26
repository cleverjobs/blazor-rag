# How to do multiple file Blazor Upload with metadata template

## Question

**BobBob** asked on 17 Jun 2021

Hi all, How does one do the same type of upload as shown in this kendo dojo, but with Blazor upload component? Is template option available with Blazor Upload like they are with kendo Upload? Please advise if anyone knows. Thx...,Bob Baldwin Fluent Consultants

## Answer

**Dimo** answered on 22 Jun 2021

Hi Bob, I have to admit that the Blazor Upload does not provide a file item template at this point. I have logged a feature request on your behalf. If the feature is important to you immediately, you can use the Upload events to populate a custom file list with the needed meta data. You may even hide the default file list with CSS (.k-upload-files ), if that will make sense in your scenario. Regards, Dimo
