# Window: Load external razor page

## Question

**Jef** asked on 09 May 2021

Is there a way to load a razor page into the WindowContent section of the Blazor Window? Similar to how this works with RadWindow in Telerik Ajax. Basically the goal is to have a universal Telerik window that we can pass parameters and launch from any page. When the Window launches it would load the relevant content page (passed from one of the parameters). For instance a site privacy document within the window.

## Answer

**Marin Bratanov** answered on 10 May 2021

Hello Jeff, If you want to show a Blazor component in the window you can do this like any other component. Whether it will have a @page directive will not make a difference in such a case. Perhaps the new dynamic component that would come in .NET 6 might help you do that more easily if you can wait until it comes out officially. Until then, there are a few other ways outlined nicely in this thread in StackOverflow: How to create Components dynamically. If you are looking to load an external page, though, you will need an <iframe> element. Blazor is an SPA (single-page-application) framework and so built-in facilities let it load components (pages) only from within its own app. Since this is the primary design of the framework, the Telerik Window component does not have a built-in <iframe> mode like 20 years ago in WebForms when frames were one of the few ways to load content on demand dynamically. With Blazor you can do load on demand in many ways that do not require frames. If you need it, you can add it to the content like any other components or markup and reuse parameters, components, code and their events from the Blazor app. Regards, Marin Bratanov

### Response

**Jeff** commented on 10 May 2021

Thank you Marin - we'll give that a try
