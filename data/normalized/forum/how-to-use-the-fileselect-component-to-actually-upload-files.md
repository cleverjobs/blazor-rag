# How to use the FileSelect component to actually upload files?

## Question

**imw** asked on 27 Jan 2022

Hi, Where can we find an actual sample/example of how to use this to obtain a file from the stream? Something like file.Stream.GetAllBytes() throws an exception of not being implemented and so far we have not been able to get any other methods to work either. Non of the demos here [https://demos.telerik.com/blazor-ui/fileselect/overview](https://demos.telerik.com/blazor-ui/fileselect/overview) seem to actually implement a file upload method, where the stream is used. The validation demo does not even have server side validation. Thanks.

### Response

**imwise** commented on 27 Jan 2022

This is the closes we have found but that does not seem to work even on the Preview tab [https://docs.telerik.com/blazor-ui/components/fileselect/events](https://docs.telerik.com/blazor-ui/components/fileselect/events)

## Answer

**Alex** answered on 27 Jan 2022

This is fully-working example (well, it'll fully work after you apply the hack mentioned in the post or if they fix the bug). Just download the index.razor file in the post and then apply the MaximumReceiveMessageSize as mentioned in the post in wherever you configure your services. [https://www.telerik.com/forums/fileselect-upload-scenario-is-broken---stream-has-no-data](https://www.telerik.com/forums/fileselect-upload-scenario-is-broken---stream-has-no-data)

### Response

**imwise** commented on 01 Feb 2022

Thanks, but that looks like the same as I linked to in my first comment which, as you have found out also, seem to have quite a few problems and isn't even working on Teleriks on trial page. It seems like the FileSelect control still isn't ready for prime time so I guess we will stick with the standard Blazor one for the time being although far from ideal.

### Response

**Hristian Stefanov** answered on 01 Feb 2022

Hi all, I discussed the topic with our development team. As a result, the problem turns out to be a mismatch with the default value we use for the SignalR in the FileSelect implementation. We are actually using in our demos the configuration you are aware of that avoids the problem: services.AddServerSideBlazor().AddHubOptions(o=>
{
o.MaximumReceiveMessageSize=4 * 1024 * 1024; // 4MB }); It turns out the framework requires the above configuration in VS project when you use FilterSelect. We will put this specification in the FilterSelect documentation very soon with more details. Thank you for noticing and reporting. Regards, Hristian Stefanov

### Response

**imwise** commented on 01 Feb 2022

Hi, Did you perhaps have some answers for the original question here about not implemented methods and a working sample please?

### Response

**Hristian Stefanov** commented on 01 Feb 2022

Hi Patrik, You are testing the documentation example in PREVIEW mode. There is an issue with the PREVIEW mode. We have it in our backlog to fix. I'm sorry for not addressing the first question previously. The example you refer to should work well outside of the PREVIEW mode and seems to cover the scenario. Please test it in a real project to see the result. Thank you.

### Response

**imwise** commented on 01 Feb 2022

Thanks. What about those "not implemented" methods that were still exposed, are they supposed get implemented or is CopyToAsync the only method to be used? Documentation isn't to detailed on this either.

### Response

**Hristian Stefanov** commented on 04 Feb 2022

Hi Patrick, You can take a look at our FileSelect API reference. The article shows what the component exposes. Everything exposed should work as expected. If some of the things there don't work in your example, please point them out. Thank you.
