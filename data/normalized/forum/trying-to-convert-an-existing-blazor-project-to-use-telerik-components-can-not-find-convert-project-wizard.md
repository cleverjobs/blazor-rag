# Trying to convert an existing Blazor project to use Telerik components. Can not find Convert Project Wizard.

## Question

**Joh** asked on 17 May 2024

I'm trying to convert an existing Blazor project to use Telerik components. Following this article Convert Project Wizard but the Telerik UI for Blazor> Convert to Telerik Application menu option doesn't show up on either the project context menu or Extensions Menu in the Solution Explorer. VS2022 V17.9.7 The fully licensed Telerik Extensions are installed in VS2022 The project file includes the package reference <PackageReference Include="Telerik.UI.for.Blazor" Version="6.0.0" /> How do I get the Convert Project Wizard? Thanks

## Answer

**Misho** answered on 22 May 2024

Hello John, Blazor Convert Project Wizard is currently available for client-side projects, for server-side projects, and for hybrid projects for NET6 and NET7 applications. Please note that to enable the wizard you need to click on the project (not the Solution itself) and use either the Extensions menu in VS or the context menu. In case your project is targeting .NET8, currently the wizard doesn't support .NET 8 projects and there is a feedback item for.NET 8 support in Blazor Convert wizard in our public portal where you could observe its status, comment and vote. [https://feedback.telerik.com/blazor/1635212-add-net-8-support-in-blazor-convert-wizard](https://feedback.telerik.com/blazor/1635212-add-net-8-support-in-blazor-convert-wizard) The feature request is scheduled for the next official 2024 Q3 release scheduled for Aug 7th 2024. In the meantime you could follow the steps described in this article to manually add Telerik UI for Blazor components to .NET 8 Blazor Web App project: [https://docs.telerik.com/blazor-ui/getting-started/web-app](https://docs.telerik.com/blazor-ui/getting-started/web-app) You could use also create a new Telerik Web App through the VS Extension New project wizard and use it as a reference for modifying your existing project: [https://docs.telerik.com/blazor-ui/getting-started/vs-integration/new-project-wizard](https://docs.telerik.com/blazor-ui/getting-started/vs-integration/new-project-wizard) I hope this helps. Please try these steps and let us know if further assistance is needed. Best Regards, Misho Progress Telerik

### Response

**Francis** commented on 22 Aug 2024

Miso, it is still not there in 2024 Q3!

### Response

**Misho** commented on 23 Aug 2024

Hello, There are some requirements for the Telerik UI for Blazor Converter to appear as a command in the menu. They are as follows: - The project should not have any Telerik UI for Blazor references - The project should have a package reference to Microsoft.AspNetCore.Components.WebAssembly.Server - The project should have an App.razor file present In addition to that the Converter works when the Interactive render mode is WebAssembly or Auto. If the project has Server or None render modes the conversion will not succeed. Please check these requirements are fulfilled in your project and let us know if further assistance is needed. Best Regards, Mihail

### Response

**Francis** commented on 23 Aug 2024

Thanks, Miso. My project was Server interactive so it did not appear. The conversion menu item would appear when the interactive is WebAssembly or Auto. I created a new Blazor Web App in Auto mode and I saw the convert option in both the Extension as well as project context menu. Thanks.

### Response

**Nikola** commented on 26 Aug 2024

Hello, I am glad you were able to resolve the issue. Please get back to us in case you have further questions. Regards.
