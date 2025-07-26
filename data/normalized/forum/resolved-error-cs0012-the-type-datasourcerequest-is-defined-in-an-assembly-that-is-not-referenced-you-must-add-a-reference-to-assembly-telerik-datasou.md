# [RESOLVED] Error CS0012: The type 'DataSourceRequest' is defined in an assembly that is not referenced. You must add a reference to assembly Telerik.DataSource, Version=2.1.3.0

## Question

**And** asked on 15 Mar 2023

I am using Telerik.UI.for.Blazor version 4.1.0. I recently cleared my nuget cache, and started getting the error noted below. I have already followed the procedure to clear nuget cache and re-install Telerik.UI.for.Blazor, but I keep getting this build error. This is happening on pages that are using Grid, at line: var datasourceResult=folderStructure.ToDataSourceResult(args.Request); error CS0012: The type 'DataSourceRequest' is defined in an assembly that is not referenced. You must add a reference to assembly 'Telerik.DataSource, Version=2.1.3.0, Culture=neutral, PublicKeyToken=29ac1a93ec063d92'.

### Response

**ivo** commented on 15 Mar 2023

Same problem pipeline also fails to build. When reverting back to my backupped packages it builds again, but after nuget cache clearing and just installing the package with dotnet restore it fails. Since the devops pipeline cannot use my local backupped packages i would like a solution for this.

### Response

**Niels** commented on 15 Mar 2023

Having the same problem with CompositeFilterDescriptor. A bitwise comparison between the NuGet package for Telerik.Datasource, v2.1.3 that I had downloaded before I cleared my NuGet cache and the one I just downloaded shows that the packages are DIFFERENT, including, I guess, the public key token. Copying the old version of the Telerik.Datasource, v2.1.3 NuGet package back into the NuGet cache makes the problem go away again.

### Response

**Anders** commented on 15 Mar 2023

We got the same issue and using the cache local works. But our pipeline is dead and right before release day. This needs to get fixed fast. Like yesterday fast

### Response

**Ron Hary** commented on 16 Mar 2023

Have the same problem after updating to 4.1.0

### Response

**Adam** commented on 16 Mar 2023

Any further update? We didn't upgrade at all and are on 4.0.1 but we are getting this issue. Serious problem

### Response

**Tjieco** commented on 16 Mar 2023

This has been blocking us for over 24 hours too now from building anything on Azure. Any indication when we can start being operational again?

### Response

**Tjieco** commented on 16 Mar 2023

It works again, thanks :)

### Response

**RAY** commented on 27 Mar 2023

This problem totally screwed me. I already loaded the corrupt package into our local Nuget Feed. I cannot load in the corrected package because it has the same version number.

### Response

**Yeongseok** commented on 27 Mar 2023

Clear the nuget cache of 4.1.0 and try again. In my case, the local build works, but the dockerfile build doesn't work, so I deleted 4.1.0 and reinstalled 4.0.1.

### Response

**RAY** commented on 28 Mar 2023

Unfortunately, the package was already loaded into our local DevOps Artifact repository. There is no way reload a new version of the package with the same version number. Until Telerik distributes the package with a new version number, I cannot use the product.

### Response

**Jon** commented on 18 Apr 2023

Add me to the affected list. I still haven't been able to work around it either. Cleared cache, using the package from the installer, even the supposedly fixed one from the downloads section.

### Response

**Dimo** commented on 19 Apr 2023

Jon - until version 4.2.0 is released next week, please use NuGet packages from our private NuGet feed (nuget.telerik.com).

## Answer

**Dimo** answered on 15 Mar 2023

Hello everyone, We aim to resolve the problem today, March 16. I am updating this post with the latest information.===@14:25 UTC The Telerik.DataSource package problem should be resolved for everyone now. Please do the following: Clean your apps. Clear the NuGet cache (or at least remove the telerik.datasource folder from the cache) to load the new package from the server. Use the Telerik NuGet feed and not local feeds that are created by the 4.1.0 installer. Local installer feeds will be possible to use with version 4.2.0, which will be released in late April. We are still monitoring the NuGet server performance just in case. Thanks everyone for your patience!===@14:10 UTC The correct Telerik.DataSource NuGet package was successfully restored on our NuGet server. A small number of customers may still download an outdated cache, which should be a temporary issue. The NuGet server itself is rebuilding its cache now, which will result in degraded performance. We expect this to complete in about an hour or in the worst case scenario, in several hours.===We experienced two separate and unrelated problems yesterday - The NuGet server was down, which is already resolved. You can bookmark our Telerik Status page for future reference, if you haven't already. The published Telerik.DataSource package has a different public key token, so the build processes reject it. We uploaded the package by mistake, as a result of a completely revamped release infrastructure that we used for the first time with UI for Blazor 4.1.0. We know what caused the new package to go live and we will adjust our release process to not allow the same problem again. Our current goal is to fix the issue in such a way, so that you don't have to change anything in your setup ( except clearing the NuGet cache where applicable ). In other words, we will try to re-upload the old correct Telerik.DataSource package to the NuGet server. Please excuse us for the trouble with the broken builds. You can keep an eye on this forum thread for updates, or follow this

### Response

**TacoWombat** commented on 15 Mar 2023

I see that the Telerik Nuget status has been upgraded to "Operational". Does this mean that Azure devops users should be able to build their apps successfully now? [https://status.telerik.com/](https://status.telerik.com/)

### Response

**Floris** commented on 15 Mar 2023

From our side, still broken. Same error messages. The details on the status page also don't reflect the issue we've been having.

### Response

**TacoWombat** commented on 15 Mar 2023

Yeah, it's interesting that they were technically different issues. Fortunately, it seems that a plan is in place for Blazor users: [https://status.telerik.com/incidents/rcg165d4t4zn](https://status.telerik.com/incidents/rcg165d4t4zn)

### Response

**Floris** commented on 15 Mar 2023

Thanks for referencing that, alas it does look like we'll have to wait another 11 hours for the updated package as it mentions 9AM UTC, I can only hope it's tomorrow morning that they mean. For us, that results in a total downtime of more than 24 hours. Not great.

### Response

**Lawrence** commented on 16 Mar 2023

I'm having some issues getting this workaround to work, I am trying to use the Telerik.UI.for.Blazor package which in turn has a dependency on Telerik.DataSource, the publickeytoken of the Telerik.DataSource assembly that I can download from the portal reports a FullName of: Telerik.DataSource, Version=2.1.3.0, Culture=neutral, PublicKeyToken=20b4b0547069c4f8 Which is obviously not the same PKT that the Telerik.UI.for.Blazor package is looking for (29ac1a93ec063d92) I've tried downloading and adding both of the nupkg files manually but I think I'm missing a step here?

### Response

**Anders** answered on 15 Mar 2023

Not an answer but a workaround. Download the nuget package from Product Download | Your Account (telerik.com) and use it in the pipeline

### Response

**ivo** commented on 15 Mar 2023

Got any doc reference how to add nuget package files in devops and then use it inside a pipeline? I only know know the NuGet.config feeds inside the solution. Thanks for your time, hope it is fixed soon.

### Response

**Anders** commented on 15 Mar 2023

for GitHub [https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-nuget-registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-nuget-registry) Azure DevOps [https://learn.microsoft.com/en-us/azure/devops/artifacts/get-started-nuget?view=azure-devops&tabs=windows#download-nuget-packages](https://learn.microsoft.com/en-us/azure/devops/artifacts/get-started-nuget?view=azure-devops&tabs=windows#download-nuget-packages) I do not know of any official documentation from Telerik, but this should work if the nuget files have been downloaded from the link above.

### Response

**ivo** commented on 16 Mar 2023

Thanks! will use this for critical packages from now on :)! I just ran my pipeline and it works again.

### Response

**Floris** answered on 15 Mar 2023

We are having the exact same issue. We did not bump any versions at all, the exact same code that was compiling on our CI yesterday, is failing today with a similar message. EDIT: not an answer, guess I clicked the wrong button.

### Response

**Yeongseok** commented on 16 Mar 2023

When you build the Dockerfile, you'll get an error. error CS0012: The type 'DataSourceRequest' is defined in an assembly that is not referenced. You must add a reference to assembly 'Telerik.DataSource, Version=2.1.3.0, Culture=neutral, PublicKeyToken=29ac1a93ec063d92'.

### Response

**Yeongseok** answered on 16 Mar 2023

When you build the Dockerfile, you'll get an error. error CS0012: The type 'DataSourceRequest' is defined in an assembly that is not referenced. You must add a reference to assembly 'Telerik.DataSource, Version=2.1.3.0, Culture=neutral, PublicKeyToken=29ac1a93ec063d92'.

### Response

**MIS Operations** answered on 16 Mar 2023

Has there been any update with regards to the "Telerik.DataSource, Version=2.1.3.0" issue? This is holding up development and CI/CD pipelines, I dont want to hack them with a temp fix to get things working. Is there a timeline as to when this will be resolved? If not I will probably be forced to hack the pipeline to get things working.

### Response

**Robert** answered on 16 Mar 2023

The download for the pkg is for 4.1.0. We are using 3.7. We do not want to risk breaking chnges across out site for an entire suite update in order o get the DataSource control, and the direct link to the datasource control doesn't seem to be coming down from the link provided.

### Response

**Bart** answered on 16 Mar 2023

There is some progress in the sense that the error changed for the build in BuildKite Failed to download package 'Telerik.DataSource.2.1.3' from '[https://nuget.telerik.com/v3/package/telerik.datasource/2.1.3/telerik.datasource.2.1.3.nupkg'.](https://nuget.telerik.com/v3/package/telerik.datasource/2.1.3/telerik.datasource.2.1.3.nupkg'.)
Response status code does not indicate success: 500 (Internal Server Error). ... but still fails?

### Response

**Jonathan** commented on 16 Mar 2023

We're seeing the exact same thing here. Hopefully its a small step forward for the Telerik team in seeing this issue resolved today.

### Response

**Bart** commented on 16 Mar 2023

@Jonathan: It just started working for us! Maybe give it a retry now...
