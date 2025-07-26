# Unhandled exception in telerik-blazor.js when DropDownList collection is empty

## Question

**Dou** asked on 10 Oct 2024

I came across this when I was loading a collection bound to a DropDownList from an API and when I clicked the drop down before the API call had completed I received the exception below in telerik-blazor.js: I then created a new project from the stand alone blazor app template, pulled in the Telerik nuget package and added a drop down list which was bound to an empty collection. As soon as I click the drop down I get the same exception. The obvious workaround is to initialize the list with a blank item so at least there's something there before the API completes, but it seems like this is an issue that should be handled better as it took me a fair amount of time to figure out what was going on. Shouldn't a drop down be allowed to have no items? Here's the code but I've also attached the project as a zip file: <TelerikDropDownList Data="@DropDownListData" @bind-Value="DropDownListValue" /> @code { private List<string> DropDownListData=new List<string>();// { "first", "second", "third" }; private string DropDownListValue { get; set; }=string.Empty; }

## Answer

**Dimo** answered on 14 Oct 2024

Hi Doug, Thanks for the provided runnable app. I can observe the described error only if I...: Enable caught exceptions in the browser, or Run an example with an empty DropDownList in debug mode in Visual Studio So the workaround with the blank item should not be necessary. Nevertheless, I agree we can optimize the code a bit, so I have already sent a proposal for a fix to the developers. I also awarded you some Telerik points. Regards, Dimo Progress Telerik

### Response

**Doug** commented on 14 Oct 2024

Dimo, It is certainly true that if you run the app without attaching the debugger in Visual Studio (Ctrl+F5) you don't get the error, however 99% of the time I'm running with the debugger attached so until your fix is released I'll need to use the work around. Thanks for the response.

### Response

**Dimo** commented on 15 Oct 2024

Sure, I agree it can be inconvenient if Visual Studio halts the app execution in developer environment without a reason. I didn't express myself clearly - when I mentioned the workaround, I was referring to production environment.

### Response

**David** answered on 22 Nov 2024

I'm having a similar problem. My DropDownList bound collection does have values and the list is filterable. When the information entered into the filter box doesn't match any entry in the collection I get the same error. As stated above, running outside of the VS debugger (i.e. Production) it works as expected. Still, this seems like something that should be fixed. Dave

### Response

**Dimo** commented on 22 Nov 2024

@Dave - the JavaScript error when opening an empty dropdown in debug mode is already fixed in Telerik UI for Blazor 7.0.

### Response

**David** commented on 03 Dec 2024

Dimo, Since upgrading to Telerik for Blazor 9.0 I get the following error a lot when running in debug. "Cannot read properties of null (reading 'firstChild') TypeError: Cannot read properties of null (reading 'firstChild') at it.addAll" I do not get this error when I run without being in debug mode. But most of the time I want/need to be debugging. I this the same issue as reported above, or is it something new? Is anybody working to fix it? Thanks Dave

### Response

**Dimo** commented on 04 Dec 2024

@Dave - the error might be similar in nature, but the component and scenario are surely different. Please submit a separate forum thread or ticket with a runnable test page, so that we can see where exactly the problem is coming from. On a side note, Telerik UI for Blazor doesn't have version 9, so please: Specify which version you are using. Clear the browser cache just in case.

### Response

**David** commented on 04 Dec 2024

Dimo, Sorry, I meant to say we were using Telerik for Blazor UI 7.0. I asked if other members of my team were experiencing this issue. The response was to clear the browser cache to resolve it. Also, another team member recently implementing cache busting into our application and I have not seen the error since. If the error occurs again, and I can consistently reproduce it, I will open a new forum thread. Thanks Dave

### Response

**Claudio** commented on 17 Jan 2025

same problem here!
