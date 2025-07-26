# NuGet Warning & Error with v 0.3.0

## Question

**Art** asked on 07 Apr 2019

Hi I'm using version 03.0 of the Telerik.UI.for.Blazor component with .NET Core 3.0.100-preview3-010431 and get the following: WarningNU1603: Telerik.UI.for.Blazor 0.3.0 depends on Microsoft.Extensions.DependencyInjection (>=3.0.0-preview3-19153-02) but Microsoft.Extensions.DependencyInjection 3.0.0-preview3-19153-02 was not found. An approximate best match of Microsoft.Extensions.DependencyInjection 3.0.0-preview4.19121.1 was resolved. and ErrorNU1605: Detected package downgrade: Microsoft.NETCore.Platforms from 3.0.0-preview4.19120.16 to 3.0.0-preview3.19128.7. Reference the package directly from the project to select a different version. Please Advise Arthur

## Answer

**Pavlina** answered on 08 Apr 2019

Hi Arthur, Indeed the warning and the error you encounter can be observed with version 0.3.0. However, I am happy to let you know that they are already fixed and the fix will be included in the upcoming Telerik UI for Blazor 0.4.0 release which is scheduled for tomorrow. This new version will also contain several new components: Charts, DropDownList, Calendar, TextBox, DateInput, and Animation Container. In addition to that, we will provide integration with the validation framework, which means that all Input components will work with the default Blazor EditContext out of the box. Please give it a try once it is available for download in your account and let us know if everything works as expected. Regards, Pavlina
