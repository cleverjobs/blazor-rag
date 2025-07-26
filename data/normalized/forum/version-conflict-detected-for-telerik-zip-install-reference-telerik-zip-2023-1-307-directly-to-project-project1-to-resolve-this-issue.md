# Version conflict detected for Telerik.Zip. Install/reference Telerik.Zip 2023.1.307 directly to project Project1 to resolve this issue

## Question

**Anu** asked on 08 Oct 2024

Severity Code Description Project File Line Suppression State Error (active) NU1107 Version conflict detected for Telerik.Zip. Install/reference Telerik.Zip 2023.1.307 directly to project Project1 to resolve this issue. Project1 -> Telerik.UI.for.Blazor 4.1.0 -> Telerik.Documents.SpreadsheetStreaming 2023.1.307 -> Telerik.Zip (=2023.1.307) Project1 -> Telerik.Documents.Spreadsheet.FormatProviders.OpenXml 2023.1.104 -> Telerik.Zip (=2023.1.104). Project1 C:\Work\Projects\Project1 \Project1.csproj 1 My project is referenced to <PackageReference Include="Telerik.Documents.Spreadsheet.FormatProviders.OpenXml" Version="2022.2.613" /> <PackageReference Include="Telerik.Documents.SpreadsheetStreaming" Version="2022.2.613" /> <PackageReference Include="Telerik.UI.for.Blazor" Version="3.4.0" /> But I am not able to find them in Nuget

## Answer

**Dimo** answered on 10 Oct 2024

Hi Anup, Please check our KB article about Version conflict detected for Telerik.Zip. Currently your account is associated with a license with a subscription period starting from April 24, 2023. That's why you have access to Telerik UI for Blazor 4.2.0 or newer versions. I can see that the license holder at your company owns licenses with an older subscription period too. Regards, Dimo Progress Telerik
