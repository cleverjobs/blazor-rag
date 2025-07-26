# Unable to use Telerik UI for Blazor

## Question

**Sam** asked on 02 Sep 2021

Hi Telerik Team After several attempts to clear up the nuget feed and install the Telerik UI for Blazor I am writing to you. I am getting the following login failed message. I have tried with both encrypted and plain-text password in the nuget.config file. [nuget.telerik.com] The V2 feed at '[https://nuget.telerik.com/nuget/Search()?$filter=IsLatestVersion&searchTerm=''&targetFramework='net5.0'&includePrerelease=false&$skip=0&$top=26&semVerLevel=2.0.0'](https://nuget.telerik.com/nuget/Search()?$filter=IsLatestVersion&searchTerm=''&targetFramework='net5.0'&includePrerelease=false&$skip=0&$top=26&semVerLevel=2.0.0') returned an unexpected status code '401 Logon failed.'. The nuget.config file looks as below <? xml version="1.0" encoding="utf-8"?> <configuration> <packageSources> <add key="nuget.telerik.com" value="[https://nuget.telerik.com/nuget"](https://nuget.telerik.com/nuget") /> <add key="nuget.org" value="[https://api.nuget.org/v3/index.json"](https://api.nuget.org/v3/index.json") protocolVersion="3" /> </packageSources> <packageRestore> <add key="enabled" value="True" /> <add key="automatic" value="True" /> </packageRestore> <bindingRedirects> <add key="skip" value="False" /> </bindingRedirects> <packageManagement> <add key="format" value="0" /> <add key="disabled" value="False" /> </packageManagement> <packageSourceCredentials> <nuget.telerik.com> <add key="Username" value=<username> /> <add key="Password" value=<password> /> </nuget.telerik.com> </packageSourceCredentials> </configuration> Looking forward to your help!

## Answer

**Marin Bratanov** answered on 03 Sep 2021

Hi, Could you try the idea from this section that seems quite similar to the error you are facing: [https://docs.telerik.com/blazor-ui/troubleshooting/nuget-feed#error-401-login-failed?](https://docs.telerik.com/blazor-ui/troubleshooting/nuget-feed#error-401-login-failed?) If the online feed does not get running with that, try making an offline feed in a local folder on the disk to trial the Blazor components, here's how to do that: [https://docs.telerik.com/blazor-ui/installation/zip.](https://docs.telerik.com/blazor-ui/installation/zip.) Regards, Marin Bratanov Progress Telerik
