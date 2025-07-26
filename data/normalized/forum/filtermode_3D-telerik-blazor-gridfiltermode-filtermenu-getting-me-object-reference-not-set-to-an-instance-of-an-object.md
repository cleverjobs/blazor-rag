# FilterMode="Telerik.Blazor.GridFilterMode.FilterMenu" getting me Object reference not set to an instance of an object

## Question

**Med** asked on 19 Dec 2019

Adding FilterMode to TelerikGrid is not working for me, it is returning Null reference exception, I don't understand what it means. <TelerikGrid Data=@Grid FilterMode="Telerik.Blazor.GridFilterMode.FilterMenu" Pageable=true> An unhandled exception occurred while processing the request. System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.RootComponent.TelerikRootComponentFragmentBase.Dispose() at Microsoft.AspNetCore.Components.Rendering.ComponentState.Dispose() at Microsoft.AspNetCore.Components.RenderTree.Renderer.Dispose(Boolean disposing) --- End of stack trace from previous location where exception was thrown --- Thank you in advance for your help

## Answer

**Marin Bratanov** answered on 19 Dec 2019

Hi, With the available information I can only suggest you compare against our demos that work fine: [https://demos.telerik.com/blazor-ui/grid/filter-menu.](https://demos.telerik.com/blazor-ui/grid/filter-menu.) If this does not help I suggest you open a support ticket where you can send a zipped project so I can investigate and avoid further guesswork. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 19 Dec 2019

To add the information from the sample from the ticket here as well - the project was missing the required bits that enable the Telerik components. You can see what you need in this article or in this tutorial. --Marin

### Response

**Medhanie** answered on 19 Dec 2019

Thank you I was missing to add @using statements in the Imports file to add Blazor.Components files and include <TelerikRootComponent> inside MainLayout. Problem is now fixed. thank you
