# Adding Telerik Blazor to an existing Blazor App

## Question

**Ind** asked on 05 Jul 2020

Hi I am just learning/testing with Blazor and have created a standard Blazor Server App, using the default template built into VS 2019. Is there a simple way I can convert this to a Telerik Blazor app? For exampe copy over some DLLs or maybe install a nuget package? Or do I have to start from scratch and use the Telerik Blazor built into VS Studio? Manythanks in advance

## Answer

**Marin Bratanov** answered on 05 Jul 2020

Hi Indy, There are two easy ways to add the Telerik Blazor components to your app: use our automated wizard as described here: [https://docs.telerik.com/blazor-ui/getting-started/vs-integration/convert-project-wizard](https://docs.telerik.com/blazor-ui/getting-started/vs-integration/convert-project-wizard) OR, just do it yourself in a few manual steps as described here: [https://docs.telerik.com/blazor-ui/getting-started/server-blazor#step-2---enable-the-telerik-components-in-an-existing-project](https://docs.telerik.com/blazor-ui/getting-started/server-blazor#step-2---enable-the-telerik-components-in-an-existing-project) Regards, Marin Bratanov

### Response

**Indy** answered on 06 Jul 2020

Hi Thanks for the response I installed the latest version from my account (Blazor UI v2.15.0). I installed the msi - restarted VS2019 but I get the below error Error NU1101 Unable to find package Telerik.UI.for.Blazor. No packages exist with this id in source(s): Microsoft Visual Studio Offline Packages Looks like a i need to install it locally after reading the below? Why couldnt this be included in the Wizard? [https://docs.telerik.com/blazor-ui/installation/nuget?_ga=2.250463686.1166314361.1593947150-1398515223.1586966740](https://docs.telerik.com/blazor-ui/installation/nuget?_ga=2.250463686.1166314361.1593947150-1398515223.1586966740)

### Response

**Marin Bratanov** answered on 07 Jul 2020

Hi Indy, We are working on making wizards and automated installers add nuget sources. There are technical difficulties with this related to elevated permissions. For the time being, you do need to add the package source manually. You have two options: our online feed: [https://docs.telerik.com/blazor-ui/installation/nuget](https://docs.telerik.com/blazor-ui/installation/nuget) a local package source: [https://docs.telerik.com/blazor-ui/installation/automated#set-up-a-local-nuget-feed-in-visual-studio](https://docs.telerik.com/blazor-ui/installation/automated#set-up-a-local-nuget-feed-in-visual-studio) Regards, Marin Bratanov
