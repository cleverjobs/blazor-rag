# Using Telerik NuGet Server in Docker

## Question

**Mic** asked on 21 Nov 2023

Hi, I try to use Telerik.UI.for.Blazor in Docker. I have added a nuget.config file and also add the corresponding line as explained here [https://docs.telerik.com/aspnet-core/knowledge-base/docker-build-nuget](https://docs.telerik.com/aspnet-core/knowledge-base/docker-build-nuget) But when running the docker build command there is this error "error NU1301: Unable to load the service index for source [https://nuget.telerik.com/v3/index.json."](https://nuget.telerik.com/v3/index.json.") What is wrong ? Best regards.

### Response

**Michel** commented on 21 Nov 2023

You have to copy the nuget.config before trying to restore. So you need to add this command in the dockerfile COPY "nuget.config" . Here is my dockerfile #See [https://aka.ms/customizecontainer](https://aka.ms/customizecontainer) to learn how to customize your debug container and how Visual Studio uses this Dockerfile to build your images for faster debugging.

#Depending on the operating system of the host machines(s) that will build or run the containers, the image specified in the FROM statement may need to be changed.
#For more information, please see [https://aka.ms/containercompat](https://aka.ms/containercompat)

FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
ARG BUILD_CONFIGURATION=Release
WORKDIR /src
# Telerik NuGet Server Setup
# 1. Use ARG or ENV to set build-time variables (these %varibles% should already set on the host environment)
ARG TELERIK_USERNAME=myaccountname@mydomain.com
ARG TELERIK_PASSWORD=mypassword
# 2. Copy the nuget.config file into the work directory
COPY "nuget.config" .
COPY "MyProject.csproj" .
RUN dotnet restore "./MyProject.csproj"
COPY . .
WORKDIR "/src"
RUN dotnet build "MyProject.csproj" -c %BUILD_CONFIGURATION% -o /app/build

FROM build AS publish
ARG BUILD_CONFIGURATION=Release
RUN dotnet publish "MyProject.csproj" -c %BUILD_CONFIGURATION% -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "MyProject.dll"]

### Response

**Michel** commented on 21 Nov 2023

It seems that using nuget keys don't work Dockerfile : #See [https://aka.ms/customizecontainer](https://aka.ms/customizecontainer) to learn how to customize your debug container and how Visual Studio uses this Dockerfile to build your images for faster debugging.

#Depending on the operating system of the host machines(s) that will build or run the containers, the image specified in the FROM statement may need to be changed.
#For more information, please see [https://aka.ms/containercompat](https://aka.ms/containercompat)

FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
ARG BUILD_CONFIGURATION=Release
WORKDIR /src
# Telerik NuGet Server Setup
# 1. Use ARG or ENV to set build-time variables (these %varibles% should already set on the host environment)
ARG TELERIK_USERNAME="mykeyname"
ARG TELERIK_PASSWORD="mykey"
# 2. Copy the nuget.config file into the work directory
COPY "nuget.config" .
COPY "MyProject.csproj" .
RUN dotnet restore "./MyProject.csproj"
COPY . .
WORKDIR "/src"
RUN dotnet build "MyProject.csproj" -c %BUILD_CONFIGURATION% -o /app/build

FROM build AS publish
ARG BUILD_CONFIGURATION=Release
RUN dotnet publish "MyProject.csproj" -c %BUILD_CONFIGURATION% -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "MyProject.dll"] nuget.config file : <?xml version="1.0" encoding="utf-8"?> <configuration> <!-- Use the Telerik NuGet server as a package source --> <packageSources> <clear /> <add key="nuget.org" value="[https://api.nuget.org/v3/index.json"](https://api.nuget.org/v3/index.json") protocolVersion="3" /> <add key="telerikserver" value="[https://nuget.telerik.com/v3/index.json"](https://nuget.telerik.com/v3/index.json") protocolVersion="3" /> </packageSources> <!-- Your Telerik account credentials or Telerik NuGet Key --> <packageSourceCredentials> <telerikserver> <add key="Username" value="mykeyname" /> <add key="ClearTextPassword" value="mykey" /> </telerikserver> </packageSourceCredentials> <!-- ...other config settings, see reference links at bottom of article --> </configuration> The error message when building the docker image is : C:\src\Myproject.csproj : error NU1301: Unable to load the service index for source [https://nuget.telerik.com/v3/index.json.](https://nuget.telerik.com/v3/index.json.) Any suggestions for using nuget keys ? Best regards

### Response

**Svetoslav Dimitrov** commented on 24 Nov 2023

Hello Michel, There are various potential causes for this error such as failing authentication, requesting the incorrect type of packages based on the license type, missing (or wrong) local configuration, or network connectivity issues. To verify if you can access the Telerik NuGet server and the expected packages, open the [https://nuget.telerik.com/v3/search?q=blazor&prerelease=true&skip=0&take=100&semVerLevel=2.0.0](https://nuget.telerik.com/v3/search?q=blazor&prerelease=true&skip=0&take=100&semVerLevel=2.0.0) URL directly in the web browser and enter your Telerik credentials in the prompt. As a result, you will see a JSON output with the NuGet packages and versions that are available for you. If you can access the feed in the browser, but do not see the packages in Visual Studio, most likely the problem is caused by entering wrong credentials or using a different Telerik account. Make sure your saved credentials are correct. Also, you must not have a NuGet.Config file in your project as it may bring in invalid credentials and project-level configuration files override the global ones. I hope this helps. Please let me know if you are still experiencing an issue after completing the above steps.

## Answer

**Brian** answered on 07 Mar 2025

Try this: <?xml version="1.0" encoding="utf-8"?> <configuration> <!-- Use the Telerik NuGet server as a package source --> <packageSources> <clear /> <add key="nuget.org" value="[https://api.nuget.org/v3/index.json"](https://api.nuget.org/v3/index.json") protocolVersion="3" /> <add key="telerikserver" value="[https://nuget.telerik.com/v3/index.json"](https://nuget.telerik.com/v3/index.json") protocolVersion="3" /> </packageSources> <packageSourceMapping> <packageSource key="TelerikServer"> <package pattern="Telerik.*" /> </packageSource> <packageSource key="nuget.org"> <package pattern="Telerik.Licensing" /> <package pattern="*" /> </packageSource> </packageSourceMapping> <!-- Your Telerik account credentials or Telerik NuGet Key --> <packageSourceCredentials> <telerikserver> <add key="Username" value="mykeyname" /> <add key="ClearTextPassword" value="mykey" /> </telerikserver> </packageSourceCredentials> <!-- ...other config settings, see reference links at bottom of article --> </configuration>
