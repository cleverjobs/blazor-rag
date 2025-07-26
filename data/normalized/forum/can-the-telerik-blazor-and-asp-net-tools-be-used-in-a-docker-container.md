# Can The Telerik Blazor and ASP.NET tools be used in a Docker Container

## Question

**DonDon** asked on 14 Jun 2022

We are working on a application rewrite and wanted to see if your tools can be used within a Docker Container.

### Response

**Benjamin** commented on 16 Jun 2022

Hey Don, can you specify your question? We dockerize all our blazor and asp.net applications without any problems.

### Response

**Don** commented on 16 Jun 2022

Hi Benjamin, It was more of a general question. The rewrite I am on started over a year before I joined it and there were indications that at the beginning of the rewrite, there were issues with getting Telerik controls working in Docker containers. I am not sure how true that was but just gathering information for my request for licenses for the toolset.

## Answer

**Dimo** answered on 17 Jun 2022

Hello Don, I am posting a similar response that I provided to a colleague of yours in another thread. Developers from our community are welcome to share their experience too.===Generally, the Docker container configuration is independent of UI for Blazor. You can refer to generic articles for Docker and Blazor apps. There is one step that I want to point out, as other developers have stumbled upon it. It concerns private NuGet feeds in Docker. The general recommendation is to copy the NuGet.config file explicitly during build: [https://github.com/dotnet/dotnet-docker/blob/main/documentation/scenarios/nuget-credentials.md#use-a-multi-stage-build-to-protect-nugetconfig-passed-by-build-context](https://github.com/dotnet/dotnet-docker/blob/main/documentation/scenarios/nuget-credentials.md#use-a-multi-stage-build-to-protect-nugetconfig-passed-by-build-context) [https://stackoverflow.com/questions/57462205/how-to-add-private-nuget-source-in-dotnet-dockerfile](https://stackoverflow.com/questions/57462205/how-to-add-private-nuget-source-in-dotnet-dockerfile) [https://www.programmingwithwolfgang.com/restore-nuget-inside-docker/](https://www.programmingwithwolfgang.com/restore-nuget-inside-docker/) In short, the setup for our NuGet feed should be identical to any other private feed. Regards, Dimo Progress Telerik
