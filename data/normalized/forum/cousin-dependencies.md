# Cousin dependencies

## Question

**Zwa** asked on 21 Aug 2022

I am designing an application (C#) with plug-ins (Blazor server-side application with RCLs as "plugins"). Each plugin contain its own reference to "Telerik UI for Blazor" and other common libraries. The r eason is that e.g. "Plugin 1" could live for some time without being touched and thus reference an older version of Telerik components (e.g. 3.3.0), while "Plugin 2" is updated more often and can therefore get newer versions of Telerik. I know the above results in conflicts like "Cousin dependency" or "Nearest Wins". I need to strictly load all assemblies and their dependencies as they were compiled with their respective dependencies. T he final product is being released in a highly regulated environment which is why you just dont update all plugins to support the latest and greatest :-) Any idea on how to accomplish this? Project specs: Blazor server side,.NET 6+, Telerik UI for Blazor

### Response

**Marin Bratanov** commented on 21 Aug 2022

I don't think you can do that in any tooling I am aware of, neither .NET, nor node.js or other similar package manger solutions. Ultimately, all your dependencies must be resolved and point to the same version of the dependency (Telerik components in this case). The only way I can think of is if those are two separate applications and the second one is actually loaded inside of an <iframe> of the first. Or, some sort of autoupgrade of the dependencies but that defeats the idea of attempting to have an old version somewhere.

### Response

**ZwapSharp** commented on 22 Aug 2022

I think I will look into AssemblyLoadContext in .NET Understanding AssemblyLoadContext - .NET | Microsoft Docs Hoping it will solve my problem
