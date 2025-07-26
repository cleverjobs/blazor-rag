# FileSelect Upload Scenario is Broken - Stream has no data

## Question

**Ale** asked on 25 Jan 2022

The problem happens for "large" files. I re-produced it for files as small as 123,260 bytes (123 kilobytes!) even when FileSelect.MaxFileSize=223260 or MaxFileSize=int.MaxValue! Is this by design in the FileSelect component to not support files greater than a hundred kilobytes, or am I doing something wrong? There is nothing in the documentation warning about such tiny file limits. Update: I can upload files of any size when I add this line to the code. It of course is a hack and the real problem is in the design of FileSelect and should be fixed there. builder.Services.Configure<HubOptions>(options=> { options.MaximumReceiveMessageSize=null; }); Was this setting enabled by the Telerik engineers who tested the control? Because it is not in the default VS project and anyone creating a vanilla VS project and using FileSelect will not be able to use it with anything> 10-20kb or so :/ Another problem: (sometimes?) even when the file is uploaded successfully using all-default code, the uploaded file cannot be re-written because it remains locked despite the upload process finishing successfully. There is a place in the Telerik code that is opening the destination file and NOT disposing it properly.

### Response

**Hristian Stefanov** commented on 27 Jan 2022

Hi Alex, Thank you for describing us in such detail the situation. This sounds indeed like some file size problem. Currently, I'm further testing the scenario with our development team. I will get back to you here as soon as we come up with a conclusion. I appreciate the patience while we investigate the matter.

## Answer

**Hristian Stefanov** answered on 01 Feb 2022

Hi Alex, I discussed the topic with our development team. As a result, the problem turns out to be a mismatch with the default value we use for the SignalR in the FileSelect implementation. We are actually using in our demos the configuration you are aware of that avoids the problem: services.AddServerSideBlazor().AddHubOptions(o=>
{
o.MaximumReceiveMessageSize=4 * 1024 * 1024; // 4MB }); I'm sorry for the inconvenience. It turns out the framework requires the above configuration in VS project when you use FilterSelect. We will put this specification in the FilterSelect documentation very soon with more details. Thank you for the effort. Regards, Hristian Stefanov

### Response

**Alex** commented on 19 Feb 2022

Its been almost three weeks and you still haven't updated the documentation yet. The control is not usable without the updated documentation.

### Response

**Hristian Stefanov** commented on 23 Feb 2022

Hi Alex, The pull request with the updates in the documentation is already pushed into our repository. It will be very soon in production. Thank you for your patience.
