# ContextMenu requires a TelerikRootComponent

## Question

**gfk** asked on 25 May 2021

Hello, I have been using the TreeView and NumericTextBox components in 2.22 and 2.24 for months now without a problem. Today I added a ContextMenu to the project and carefully followed the instructions for client-side apps. After many hours of solid research, the new component produces nothing but: A Telerik component on the requested view requires a TelerikRootComponent to be added to the root of the MainLayout component of the app. I have checked the documentation and all the obvious files related to this, and they all seem okay, except the sample MainLayout.cs file does not work as written (is it erroneous?). I have pasted mine below. I'm using the single package Telerik.UI.for.Blazor 2.24.0. The project is very large, so I can only paste a few snippets below. I've completely run out of ideas on this problem. Maybe I'm missing a css or js file, or a package -- Thanks, Greg index.html <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme-default/all.css" /> <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js" defer> </script> Program.cs builder.Services.AddTelerikBlazor(); TelerikLayout.razor @inherits LayoutComponentBase <TelerikRootComponent> @Body </TelerikRootComponent> MainLayout.razor @inherits TelerikLayout

@Body

## Answer

**gfkeogh** answered on 05 Jul 2021

I downloaded the sample app and compared it to mine. I noticed that my MainLayout file (shown above) was not the same as the sample. I made my Layout file the same as the sample and now the context menu component is working. So my MainLayout was technically 'wrong' for 6 months and I never noticed, perhaps because this is the first Telerik component I've used that was dependent upon the MainLayout being exactly correct. The description of the MainLayout file in your Project Configuration page section Common Configuration is deficient. It just says "more code will be present here", but you should provide an explanation of what typically is needed. For example, my corrected file is like this: @layout TelerikLayout
@inherits LayoutComponentBase

@Body Thanks, Greg

### Response

**Dimo** commented on 06 Jul 2021

Hi Greg, I am glad to learn that the issue is resolved. By definition, Blazor layout files inherit LayoutComponentBase, so this line is always required. Our documentation suggests to just prepend @layout TelerikLayout as a first line. Nevertheless, I have enhanced the snippet to avoid possible misunderstandings. The change will go live soon.

### Response

**Dimo** answered on 26 May 2021

Hi Greg, Indeed, the provided snippets look OK, but at the same time, I presume they do not reveal the whole picture. Normally, the observed error will occur in one of the following scanarios: The page @Body is not wrapped in a <TelerikRootComponent> The page layout does not include @layout TelerikLayout For example, is it possible that the view with the ContextMenu uses a different layout, and not MainLayout? I am adding a runnable project to this post. It is based on the default client-side Blazor app and includes a TelerikContextMenu. Just restore the NuGet packages, rebuild and run. Please compare with the implementation in your app and try to identify any differences. Let me know of your findings. Regards, Dimo Progress Telerik
