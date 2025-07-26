# Treelist paging design problem

## Question

**Han** asked on 03 Nov 2022

I'm using TelerikTreeList in a Blazor project. However, the paging appears very ugly. As you can see in the attached image, the paging elements are spread over three lines. That also doesn't depend on the width of the TreeList. I cannot influence the appearance via TreeListSettings --> adaptive. Anyone know what the problem is?

## Answer

**Dimo** answered on 08 Nov 2022

Hi Hans, Most likely the app is using an old outdated CSS theme - please check the suggestions in the linked forum thread. On the other hand, if you are using a theme as a static asset from the NuGet package, clear the browser cache. Sometimes this may be necessary in WebAssembly apps - here is a similar phenomenon related to our JSInterop file. Regards, Dimo Progress Telerik
