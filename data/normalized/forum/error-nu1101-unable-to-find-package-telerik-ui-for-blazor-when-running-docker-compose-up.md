# [Error NU1101] Unable to find package Telerik.UI.for.Blazor when running docker-compose up

## Question

**Ric** asked on 17 Mar 2023

I'm running docker-compose up --force-recreate --build and obtaining the following error: [+] Building 20.8 s ( 17 / 17 ) FINISHED=> [ int ernal ] load build definition from Dockerfile 0.0 s=>=> transferring dockerfile: 32 B 0.0 s=> [ int ernal ] load .dockerignore 0.0 s=>=> transferring context: 2 B 0.0 s=> [ int ernal ] load metadata for mcr.microsoft.com/dotnet/sdk: 7.0 0.2 s=> [ 1 / 13 ] FROM mcr.microsoft.com/dotnet/sdk: 7.0 @sha256:e049e6a153619337ceb4edd040fb60a220d420414d41d6eb39708d6c 0.0 s=> [ int ernal ] load build context 0.1 s=>=> transferring context: 9.98 MB 0.1 s=> CACHED [ 2 / 13 ] WORKDIR /app 0.0 s=> CACHED [ 3 / 13 ] RUN apt install -y curl 0.0 s=> CACHED [ 4 / 13 ] RUN curl -sL [https://deb.nodesource.com/setup_14.x](https://deb.nodesource.com/setup_14.x) | bash - 0.0 s=> CACHED [ 5 / 13 ] RUN apt -get install -y nodejs 0.0 s=> CACHED [ 6 / 13 ] RUN curl -L [https://www.npmjs.com/install.sh](https://www.npmjs.com/install.sh) | sh 0.0 s=> CACHED [ 7 / 13 ] RUN apt install -y sshpass 0.0 s=> CACHED [ 8 / 13 ] WORKDIR /app 0.0 s=> [ 9 / 13 ] COPY. . 0.3 s=> [ 10 / 13 ] WORKDIR /app/wwwroot 0.1 s=> [ 11 / 13 ] RUN npm install 9.9 s=> [ 12 / 13 ] WORKDIR /app 0.0 s=> ERROR [ 13 / 13 ] RUN dotnet publish -r ubuntu. 18.04 -x64 -c Release -o./deploy/release 10.1 s ------> [ 13 / 13 ] RUN dotnet publish -r ubuntu. 18.04 -x64 -c Release -o./deploy/release: #0 0.574 MSBuild version 17.5.0+6f08c67f3 for .NET #0 1.134 Determining projects to restore... #0 1.137 Skipping project "/monitorix-server/monitorix-server.csproj" because it was not found. #0 1.139 Skipping project "/monitorix-server/monitorix-server.csproj" because it was not found. #0 9.653 /app/monitorix-ui.csproj : error NU1101: Unable to find package Telerik.UI.for.Blazor. No packages exist with this id in source(s): nuget.org #0 9.722 Failed to restore /app/monitorix-ui.csproj (in 8.35 sec). ------ failed to solve: executor failed running [/ bin / sh - c dotnet publish - r ubuntu.18.04 - x64 - c Release - o. / deploy / release ]: exit code: 1 I've included the necessary credentials in NuGet.config at %appdata%/roaming/nuget and the corresponding package sources with the following feed url [https://nuget.telerik.com/v3/index.json:](https://nuget.telerik.com/v3/index.json:) <?xml version="1.0" encoding="utf-8"?> <configuration> <packageSources> <add key="Microsoft Visual Studio Offline Packages" value="C:\Program Files (x86)\Microsoft SDKs\NuGetPackages\" /> <add key="nuget.org" value="[https://api.nuget.org/v3/index.json"](https://api.nuget.org/v3/index.json") /> <add key="Telerik" value="[https://nuget.telerik.com/nuget"](https://nuget.telerik.com/nuget") /> </packageSources> <packageSourceCredentials> <Telerik> <add key="Username" value="******@******.pt" /> <add key="ClearTextPassword" value="**********" /> </Telerik> </packageSourceCredentials> <packageRestore> <add key="enabled" value="True" /> <add key="automatic" value="True" /> </packageRestore> <bindingRedirects> <add key="skip" value="False" /> </bindingRedirects> <packageManagement> <add key="format" value="0" /> <add key="disabled" value="False" /> </packageManagement> <disabledPackageSources> <add key="pbanuget" value="true" /> </disabledPackageSources> </configuration> The following is the .csproj file. <Project Sdk="Microsoft.NET.Sdk.Web">

<PropertyGroup>
<TargetFramework>net7.0 </TargetFramework>
<Nullable>enable</Nullable>
<ImplicitUsings>enable</ImplicitUsings>
<RootNamespace>monitorix-ui</RootNamespace>
<UserSecretsId> 532751b e -63e3 -425b -807f -72 d212ce24ca</UserSecretsId>
</PropertyGroup>

<ItemGroup>
<PackageReference Include="BlazorMonaco" Version="3.0.0" />
<PackageReference Include="Telerik.UI.for.Blazor" Version="4.0.1" />
</ItemGroup>

</Project> And finally my dockerfile: FROM mcr.microsoft.com/dotnet/sdk:7.0 # Needed to install the web-ui dependencies WORKDIR /app
RUN apt install -y curl
RUN curl -sL [https://deb.nodesource.com/setup_14.x](https://deb.nodesource.com/setup_14.x) | bash -
RUN apt-get install -y nodejs
RUN curl -L [https://www.npmjs.com/install.sh](https://www.npmjs.com/install.sh) | sh # SSH tools RUN apt install -y sshpass # Copy app WORKDIR /app
COPY . . # Install web-ui dependencies WORKDIR /app/wwwroot
RUN npm install # dotnet core app restore/build and launch WORKDIR /app
RUN dotnet publish -r ubuntu.18.04-x64 -c Release -o ./deploy/release

EXPOSE 80
ENTRYPOINT [ "./app/deploy/monitorix-ui" ] What seems to be the problem here? Thank you

## Answer

**Dimo** answered on 21 Mar 2023

Hello Ricardo, This error...>> No packages exist with this id in source(s): nuget.org ...means that your NuGet.Config file is not used - notice that the "Telerik" feed is not mentioned at all in the error message. The most common reason is that the file is not copied together with the project. Regards, Dimo
