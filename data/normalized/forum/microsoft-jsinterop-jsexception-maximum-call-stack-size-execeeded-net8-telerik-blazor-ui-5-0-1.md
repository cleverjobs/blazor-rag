# Microsoft.JSInterop.JSException: Maximum call stack size execeeded ( .NET8 + Telerik Blazor UI 5.0.1)

## Question

**Chr** asked on 01 Feb 2024

Hi, Recently, I just updated my Blazor project to .NET8 and facing the following issue every time rendering Telerik Components. This issue doesn't appear when using .NET7 and Telerik Blazor UI 5.0.1. Please let me know if you have been facing this issue before. My current packages: <ItemGroup> <PackageReference Include="Microsoft.AspNetCore.Diagnostics.EntityFrameworkCore" Version="8.0.1" /> <PackageReference Include="Microsoft.AspNetCore.Identity.EntityFrameworkCore" Version="8.0.1" /> <PackageReference Include="Microsoft.AspNetCore.Identity.UI" Version="8.0.1" /> <PackageReference Include="Microsoft.CodeAnalysis" Version="4.8.0" /> <PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer" Version="8.0.1" /> <PackageReference Include="Microsoft.EntityFrameworkCore.Tools" Version="8.0.1"> <PrivateAssets> all </PrivateAssets> <IncludeAssets> runtime; build; native; contentfiles; analyzers; buildtransitive </IncludeAssets> </PackageReference> <PackageReference Include="Newtonsoft.Json" Version="13.0.3" /> <PackageReference Include="Telerik.DataSource" Version="3.0.0" /> <PackageReference Include="Telerik.Documents.Core" Version="2023.3.1106" /> <PackageReference Include="Telerik.Documents.SpreadsheetStreaming" Version="2023.3.1106" /> <PackageReference Include="Telerik.Recurrence" Version="0.2.1" /> <PackageReference Include="Telerik.UI.for.AspNet.Core" Version="2023.2.718" /> <PackageReference Include="Telerik.UI.for.Blazor" Version="5.0.1" /> <PackageReference Include="Telerik.Zip" Version="2023.3.1106" /> </ItemGroup>

## Answer

**Dimo** answered on 02 Feb 2024

Hello Chris - please clear the browser cache. If the issue persists, open a private ticket and send us a project for inspection.

### Response

**Chris** commented on 02 Feb 2024

Thanks, Dimo.
