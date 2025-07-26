# Code works find, but getting warning while using all kendo component

## Question

**Yas** asked on 04 Aug 2023

Hi, I am using Kendo blazor component and getting below warning while using all the components. Please see attached screenshot for snippet. Warning Message: "Found markup element with unexpected name "TelerikGrid". If this is intended to be a component, add a using directive for its namespace" Can you tell what namespace should I add in razor file to resolve this issue? -- Thanks, Yash

### Response

**Georgi** commented on 07 Aug 2023

Hi Yash, If the code compiles successfully and can be run in the browser then the problem most likely comes from a cache problem with either the NuGet, Visual Studio or the Visual Studio Extension for Blazor. I would like to suggest two possible solutions: Restart Visual Studio and delete the application's bin and obj folders. Update the Visual Studio Extension for Blazor to the latest version. It will require a restart of the Visual Studio as well. Lastly, if the issue persists, it would be helpful if you could send me a runnable sample where the issue could be reproduced. This way, I could investigate locally and come up with solutions accordingly. Looking forward to your reply
