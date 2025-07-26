# VS hangs creating Telerik project.

## Question

**CAR** asked on 05 Aug 2024

Hi, I'm trying to create a new project using the telerik blazor project template. When I click the Create button, VS hangs and nothing is created. Using: DOTNET 8 Microsoft Visual Studio Community 2022 (64-bit) - Current Version 17.10.5 Telerik Blazor 6.1.0 Thanks

### Response

**CARLOS** commented on 05 Aug 2024

meant to write VS Hangs,

### Response

**Nikola** commented on 08 Aug 2024

Hi Carlos, Depending on your screen size, resolution, and DPI settings the Telerik UI for Blazor New Project Wizard may appear behind the main Visual Studio window or any other windows. In this case, Visual Studio looks like it hangs while it is waiting for input from the wizard. Please check if this is the case by Alt-Tab-ing through the opened windows for example. If not, please send us an Activity Log from Visual Studio by following the steps in this article.
