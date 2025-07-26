# Telerik.UI.for.Blazor 2.1.0 publish fails

## Question

**Geo** asked on 30 Sep 2019

Hi I have created a brand new Blazor Server project .NET Core 3.0 (released version) and added Telerik.UI.for.Blazor 2.1.0. When I go to publish the app (Self-contained to a folder) it fails. There are numerous errors that relate to "package downgrade detected xxx from 4.3.0 to 4.0.1" Is this a known issue? Here's an example of one of the errors: SeverityCodeDescriptionProjectFileLineSuppression State ErrorDetected package downgrade: System.IO.FileSystem.Primitives from 4.3.0 to 4.0.1. Reference the package directly from the project to select a different version.

## Answer

**Marin Bratanov** answered on 30 Sep 2019

Hi George, This is not a known issue and my best guess is that the hosting environment does not yet support .NET Core 3. The fact that deploying requires you to downgrade packages indicates that the newer packages are not available on the hosting server. I just tried to publish two apps to folders (a server one and a client one) and things went well. What I did was to right click on the Server project and select Publish, then choose a folder on my machine. In both cases I get the .exe file for the server project that I can run and it effectively hosts the app so I can access it in the browser. I am attaching those projects here so you can compare against them. Regards, Marin Bratanov

### Response

**George** answered on 30 Sep 2019

Thanks. Looks to be a VS issue. I closed it down, and cleared obj and bin folders. It then worked.

### Response

**Marin Bratanov** answered on 30 Sep 2019

It's good to hear you have solved this, George. I marked your post as an answer as well, because it solves the problem too. Regards, Marin Bratanov

### Response

**George** answered on 30 Sep 2019

Unfortunately the problem returned. I resolved it by installing the Microsoft.Extensions.DependencyModel 3.0.0 package directly in my project. Telerik.DataSource 1.2.0 has a dep on Microsoft.Extensions.DependencyModel>=2.1.0. If The 2.1.0 package is used it causes a kind of diamond dependency problem.

### Response

**Marin Bratanov** answered on 30 Sep 2019

Hello George, Thank you for bringing this up and for posting your solution. I have added an item in our backlog to investigate those reference and to, probably, update them to the latest. It is not an easy decision because we have to consider whether we need to always be at the latest and how that could affect other projects and packages. I fear that in the end there will be no correct answer, and some issue with dependencies will always exist. We are, after all, in the dependency hell phase of software development. Regards, Marin Bratanov

### Response

**George** answered on 30 Sep 2019

No problem. The way Transitive deps are handled now makes this difficult to spot. It might be worth including a packages.lock.json file with example projects. It takes away one (of the many) pain point at least.

### Response

**Marin Bratanov** answered on 30 Sep 2019

Thank you for the idea, George. I have added it in the discussion explicitly so it can be considered by the dev team. Regards, Marin Bratanov
