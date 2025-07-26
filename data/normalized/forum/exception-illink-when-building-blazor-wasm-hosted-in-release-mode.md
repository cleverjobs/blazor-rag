# exception ILLink when building Blazor WASM hosted in Release mode

## Question

**Ste** asked on 24 Jun 2021

Hi, I am trying to publish a blazor WASM hosted app in Release and while building is gives below exception: nuget\packages\microsoft.aspnetcore.components.webassembly.build\3.2.1\targets\Blazor.MonoRuntime.targets(326,5): error : Unhandled exception. Mono.Linker.LoadException: Error while processing references of 'Telerik.Blazor, Version=2.24.0.0, Culture=neutral, PublicKeyToken=20b4b0547069c4f8'
62> ---> Mono.Cecil.AssemblyResolutionException: Failed to resolve assembly: 'Telerik.Documents.Spreadsheet, Version=2021.2.507.20, Culture=neutral, PublicKeyToken=5803cfa389c90ce7'
62> ---> Mono.Cecil.AssemblyResolutionException: Failed to resolve assembly: 'Telerik.Documents.Spreadsheet, Version=2021.2.507.20, Culture=neutral, PublicKeyToken=5803cfa389c90ce7'
62> at Mono.Cecil.BaseAssemblyResolver.Resolve(AssemblyNameReference name, ReaderParameters parameters)
62> at Mono.Linker.AssemblyResolver.Resolve(AssemblyNameReference name, ReaderParameters parameters)
62> at Mono.Linker.LinkContext.Resolve(IMetadataScope scope)
62> at Mono.Linker.LinkContext.Resolve(IMetadataScope scope)
62> at Mono.Linker.LinkContext.ResolveReferences(AssemblyDefinition assembly)
62> at Mono.Linker.Steps.LoadReferencesStep.ProcessReferences(AssemblyDefinition assembly)
62> at Mono.Linker.Steps.LoadReferencesStep.ProcessReferences(AssemblyDefinition assembly)
62> --- End of inner exception stack trace ---
62> at Mono.Linker.Steps.LoadReferencesStep.ProcessReferences(AssemblyDefinition assembly)
62> at Mono.Linker.Steps.LoadReferencesStep.ProcessAssembly(AssemblyDefinition assembly)
62> at Mono.Linker.Steps.BaseStep.Process(LinkContext context)
62> at Mono.Linker.Pipeline.ProcessStep(LinkContext context, IStep step)
62> at Mono.Linker.Pipeline.Process(LinkContext context)
62> at Mono.Linker.Driver.Run(ILogger customLogger)
62> at Mono.Linker.Driver.Execute(String[] args, ILogger customLogger)
62> at Mono.Linker.Driver.Main(String[] args) Is the Telerik blazor package not compatible in some way with ILLinker?

## Answer

**Marin Bratanov** answered on 27 Jun 2021

Hi Stefan, Can you confirm you are targetting .NET 5? The .NET Core 3.2.1 flavor of WebAssembly has been deprecated by Microsoft (see more here ) and there might be issues with building against it. I'm attaching here a small sample you can compare against that seems to work fine for me (both from the VS GUI - build in release mode, and publish, and from the CLI - build in release mode and publish). Regards, Marin Bratanov Progress Telerik
