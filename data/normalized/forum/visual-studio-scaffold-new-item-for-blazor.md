# Visual Studio Scaffold New Item, for Blazor?

## Question

**Jon** asked on 24 Jul 2024

Visual Studio has this Feature. Create Blazor Web Project Right click Project, select "Add" and "New Scaffolded Item..." You get a list of templates, I believe from here GitHub - dotnet/Scaffolding: Code generators to speed up development. Does Telerik plan on adding any templates for New Scaffolded Item? I have imagined I chose "EF Core API to Telerik Grid" as a template. I select the DbContext and Entity from a wizard and press Go. Then it will scaffold for me, with wonderfully crafted models and dependency injection repository pattern, service pattern, controller patterns: Server Side DTO Model or database model Mapping from Entity to DTO Repository Pattern: Entity Repository with CRUD Service to Call Repository Controller to call Service Client Side View Model Mapping from DTO to View Model HTTP Service to call Controller Razor Page with Telerik Grid Using View Model to build default columns Default Telerik Editor features Or a choice between in-line and modal editors Razor.cs calls HTTP Service Razor.cs has all CRUD functions Why? Because I've done this cookie-cutter, boilerplate type of thing so many times I think it should become a candidate for integration into Visual Studio as "Add New Scaffolded Item". Does Telerik plan to work on this? Perhaps I could help contribute

## Answer

**Svetoslav Dimitrov** answered on 29 Jul 2024

Hello Jonathan, We already provide page scaffolding with Telerik UI for Blazor components. In the case of the Grid, you can specify the model and its configuration parameters through an interface. The Telerik UI for Blazor components are data agnostic, meaning they depend on an already-created data layer. Regards, Svetoslav Dimitrov

### Response

**Jonathan** commented on 29 Jul 2024

Svetoslav, Thank you for answering, but one of the most important parts of this feature would be the ability for me to customize the scaffold templates. Does the Telerik feature allow for end users to customize scaffolding templates (T4)? Do I need to start the Solution as a Telerik Solution to use the scaffolding? I have the Telerik UI for Blazor Extension installed but I do not see the option as is stated here: Quickly Adding Components with Code Scaffolders - Visual Studio Integration - Telerik UI for Blazor Adding New Component Pages Right-click the name of the solution. From the popup menu, select the Telerik UI for Blazor Project Item. From the UI form, select the desired component and set the available parameters. The scaffolded page will be added to the Pages folder.

### Response

**Dimo** commented on 31 Jul 2024

@Jonathan>> Does the Telerik feature allow for end users to customize scaffolding templates (T4)? The Telerik scaffolder allows developers to configure component features. See screenshot step_3.png.>> Do I need to start the Solution as a Telerik Solution to use the scaffolding? No, you just need Telerik UI for Blazor to be added to the app. I think the instructions may be misleading. You need to right-click a project, not a solution. See screenshot step_2_and_4.png. I will confirm with my colleagues and fix the documentation.
