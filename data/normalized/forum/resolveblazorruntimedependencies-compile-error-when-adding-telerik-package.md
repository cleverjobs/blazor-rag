# ResolveBlazorRuntimeDependencies compile Error when adding Telerik Package

## Question

**Nic** asked on 05 Dec 2019

Hi, I'm getting an odd compile error having upgraded to the latest .Net 3.1. I've recreated the issue by simply creating a new Blazor (client) project and adding the Telerik package, it goes away when I remove it. VS 2019 16.5 preview 1. In the upgrade scenario I upgraded all the packages to 3.1.0-preview4.19579.2, obviously it picked these up when I created a new project as well. The error is: Severity Code Description Project File Line Suppression State Error MSB4018 The "ResolveBlazorRuntimeDependencies" task failed unexpectedly. System.InvalidOperationException: Multiple assemblies found with the same assembly name 'Microsoft.CodeAnalysis.resources': Microsoft.CodeAnalysis.resources C:\Users\NickWhymark\.nuget\packages\microsoft.codeanalysis.common\3.4.0\lib\netstandard2.0\de\Microsoft.CodeAnalysis.resources.dll at Microsoft.AspNetCore.Blazor.Build.ResolveBlazorRuntimeDependencies.<ResolveRuntimeDependenciesCore>g__CreateAssemblyLookup|17_1(IEnumerable`1 assemblyPaths) at Microsoft.AspNetCore.Blazor.Build.ResolveBlazorRuntimeDependencies.ResolveRuntimeDependenciesCore(String entryPoint, IEnumerable`1 applicationDependencies, IEnumerable`1 monoBclAssemblies) at Microsoft.AspNetCore.Blazor.Build.ResolveBlazorRuntimeDependencies.Execute() at Microsoft.Build.BackEnd.TaskExecutionHost.Microsoft.Build.BackEnd.ITaskExecutionHost.Execute() at Microsoft.Build.BackEnd.TaskBuilder.<ExecuteInstantiatedTask>d__26.MoveNext() BlazorApp1.Client C:\Users\xxx\.nuget\packages\microsoft.aspnetcore.blazor.build\3.1.0-preview4.19579.2\targets\Blazor.MonoRuntime.targets 252 It's a bit odd as it seems to be something to do with Analyzers and I'm not sure why that should break the build or what Telerik has to do with it? Thanks, Nick.

## Answer

**Nick** answered on 05 Dec 2019

I forgot to say that I have tried with both 2.4 and 2.5 versions of the Telerik controls!

### Response

**Marin Bratanov** answered on 05 Dec 2019

Hi Nick, The Linker in Preview 4 is very aggressive and needs explicit configuration. Could you try applying the updated information from this section of the documentation: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#client-side-project-considerations?](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#client-side-project-considerations?) In our tests adding the Linker.xml file with such a content let us run WASM apps. It fails on our assembly because we have extension methods, and they have been problematic for the linker since day 1. Regards, Marin Bratanov

### Response

**Nick** answered on 05 Dec 2019

Hi Marin, I tried that and it didn't seem to make a difference. I currently have <BlazorLinkOnBuild>false</BlazorLinkOnBuild> in the project file, so I'm not sure if the linker is running anyway? Thanks Nick.

### Response

**Marin Bratanov** answered on 05 Dec 2019

Try removing that line, Nick, we removed it from the docs as well. Regards, Marin Bratanov

### Response

**Nick** answered on 05 Dec 2019

That did the trick - thanks Marin. I suspect I'm going to have problems with my own references now, but you've pointed me in the right direction! Thanks again!

### Response

**Marin Bratanov** answered on 05 Dec 2019

Hello Nick, I just went through the steps to make sure things are ok, and I had missed adding an instruction for actually telling the linker to use this configuration file, you need to also add the following in your project file: <ItemGroup> <BlazorLinkerDescriptor Include="Linker.xml" /> </ItemGroup> I will put it live in the docs as soon as possible. Regards, Marin Bratanov

### Response

**Nick** answered on 05 Dec 2019

Thanks Marin, luckily I spotted that from the MSFT documention!

### Response

**Marin Bratanov** answered on 05 Dec 2019

Good catch, Nick! Since it's still better to have all the manual steps in one place - they are live now. --Marin
