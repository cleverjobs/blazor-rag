# Errors when compiling in release mode of Visual Studio but Debug mode is fine.

## Question

**Dav** asked on 26 May 2021

We wanted to see if the Telerik controls like the Masked Input performed any faster when running in release mode as opposed to debug mode of Visual Studio 2019. But when I switch to release mode and tried to build the app I got the following three errors which do not occur in debug mode. Can you help me? Severity Code Description Project File Line Suppression State Error CS0006 Metadata file 'C:\Projects\VSWorkspace\BlazerDemo\Client\bin\Release\netstandard2.1\BlazorDemo.Client.dll' could not be found BlazorDemo.Server C:\Projects\VSWorkspace\BlazerDemo\Server\CSC 1 Active Severity Code Description Project File Line Suppression State Error Unhandled exception. Mono.Linker.LoadException: Error while processing references of 'Telerik.Blazor, Version=2.24.0.0, Culture=neutral, PublicKeyToken=20b4b0547069c4f8' BlazorDemo.Client C:\Users\david\.nuget\packages\microsoft.aspnetcore.components.webassembly.build\3.2.1\targets\Blazor.MonoRuntime.targets 326 Severity Code Description Project File Line Suppression State Error ILLink failed with exit code -532462766. BlazorDemo.Client C:\Users\david\.nuget\packages\microsoft.aspnetcore.components.webassembly.build\3.2.1\targets\Blazor.MonoRuntime.targets 326

## Answer

**Svetoslav Dimitrov** answered on 26 May 2021

Hello David, From the stack trace, I can see that you are using .NET 3.1. The issue stems from the combination of .NET 3.1 and the WebAssembly application. Microsoft ended the support for WASM applications with .NET 3.1 and thus our support also ended. As a next step, you should upgrade the .NET version to 5 and try to publish the application anew. You can find more information on the supported .NET framework version from our documentation. Regards, Svetoslav Dimitrov

### Response

**David** answered on 26 May 2021

Thanks!!!!

### Response

**David** answered on 26 May 2021

ok so I changed the server to 5.0 target and updated my packages and also the client to net5.0. But when it runs I get this error: Unhandled Exception: System.TypeLoadException: Could not resolve type with token 0100003e from typeref (expected class 'System.Runtime.CompilerServices.IAsyncStateMachine' in assembly 'System.Runtime, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a')>>>mono_wasm_get_loaded_files 'iisexpress.exe' (CoreCLR: clrhost): Loaded 'C:\Program Files\dotnet\shared\Microsoft.NETCore.App\5.0.6\System.Buffers.dll'. mono_wasm_runtime_ready fe00e07a-5519-4dfe-b35a-f867dbaf2e28 this is the client project file: <Project Sdk="Microsoft.NET.Sdk.Web"> <PropertyGroup Label="Globals"> <SccProjectName>SAK</SccProjectName> <SccProvider>SAK</SccProvider> <SccAuxPath>SAK</SccAuxPath> <SccLocalPath>SAK</SccLocalPath> </PropertyGroup> <PropertyGroup> <TargetFramework>net5.0</TargetFramework> <UserSecretsId>0b6f3c39-3c61-4441-8849-322865985c5a</UserSecretsId> </PropertyGroup> <ItemGroup> <PackageReference Include="log4net" Version="2.0.12" /> <PackageReference Include="Microsoft.AspNetCore.Components.WebAssembly" Version="5.0.6" /> <PackageReference Include="Microsoft.AspNetCore.Components.WebAssembly.Build" Version="3.2.1" PrivateAssets="all" /> <PackageReference Include="Microsoft.AspNetCore.Components.WebAssembly.DevServer" Version="5.0.6" PrivateAssets="all" /> <PackageReference Include="Microsoft.Extensions.Logging" Version="5.0.0" /> <PackageReference Include="Microsoft.Extensions.Logging.Log4Net.AspNetCore" Version="5.0.1" /> <PackageReference Include="System.Net.Http.Json" Version="5.0.0" /> <PackageReference Include="Telerik.UI.for.Blazor" Version="2.24.0" /> </ItemGroup> <ItemGroup> <ProjectReference Include="..\SPOT Services\SPOT Services.csproj" /> <ProjectReference Include="..\SPOTShareCode\SPOT Shared Code.csproj" /> </ItemGroup> <ItemGroup> <None Update="log4net.xml"> <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory> </None> </ItemGroup> </Project>

### Response

**Svetoslav Dimitrov** commented on 28 May 2021

Hello David, You should remove the <PackageReference Include="Microsoft.AspNetCore.Components.WebAssembly.Build" Version="3.2.1" PrivateAssets="all" /> as it is a leftover from the template of the WASM project under .NET 3.2.x and it is no longer needed in .NET 5. Let me know if removing it solved the issue.
