# Telerik UI for Blazor on new empty Blazor WebAssembly Standalone App (.NET 8) using Times New Roman font

## Question

**Chr** asked on 22 Jul 2024

Hello, I am attempting to install the trial version of Telerik UI for Blazor on a brand new .NET 8 Blazor WebAssembly Standalone App project that has not been setup with the sample pages (an empty project). I have followed the WebAssembly setup tutorial in the Telerik UI for Blazor documentation. However, when I run the application the page is using Times New Roman as the font. Does the default theme (kendo-theme-default) use the Times New Roman font? If not, how can I change my application to use the font that is intended to be used with the default theme (kendo-theme-default)? If neither of these options are available, what is the best practice way of setting the font for the entire application? Thank you!

## Answer

**Svetoslav Dimitrov** answered on 25 Jul 2024

Hello Christopher, In general, our themes inherit the default font-family that the browser, or the Blazor framework through the all.css file set. To override it you have two options: Open the app.css file and change the default font-family there In your global CSS file, target the body element and provide a font-family CSS style Regards, Svetoslav Dimitrov
