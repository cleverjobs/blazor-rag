# Error trying to use Loader component

## Question

**Jav** asked on 26 Oct 2020

I inserted a Loader component to my project: <TelerikButton ButtonType="@ButtonType.Button" OnClick="@CancelForm">Cancel</TelerikButton> <TelerikButton ButtonType="@ButtonType.Submit" Primary="true" Enabled="@Activado"> <TelerikLoader Visible="@IsGeneratingReport" ThemeColor="light"></TelerikLoader> @( Activado ? "Creando recogida" : "Recogida creada" ) </TelerikButton> But it makes me mistake: "Found Markup element with unexpected name 'TelerikLoader'. If this is intended to be a component , add @using directive for its namespace". Download the TelerikBlazorAppLibManSample project and it has the same error. In the project I have referenced Telerik for Blazor and I use other components: TelerikTabStrip, TelerikTextBox, etc. and i don't have this problem. Thank you. Juan

## Answer

**Marin Bratanov** answered on 26 Oct 2020

Hello Juan, This error means that the framework does not recognize the TelerikLoader tag. This means that your project is using a version that does not have it, so you should upgrade to the latest. Regards, Marin Bratanov

### Response

**Javier** answered on 26 Oct 2020

At this moment we are using version 2.14.1

### Response

**Marin Bratanov** answered on 26 Oct 2020

Hi Juan, The loader came out with 2.17.0, and right now we're at 2.18.0 with more releases coming soon. Regards, Marin Bratanov

### Response

**Javier** answered on 26 Oct 2020

We have already updated to version 2.18.0 but we cannot find how to update the references in the project. Since the Nuget package manager does not appear version 2.18.0, we can only see 2.14.1. What should we do? Juan

### Response

**Javier** answered on 26 Oct 2020

It already appears in the NugetPackage, but now it throws us the following error: Failed to retrieve information about "Telerik.UI.for.Blazor" from remote source "[https://nuget.telerik.com/nuget/FindPackagesById()?id='Telerik.UI.for.Blazor'&semVerLevel=2.0.](https://nuget.telerik.com/nuget/FindPackagesById()?id='Telerik.UI.for.Blazor'&semVerLevel=2.0.) 0 ". The response status code does not indicate a successful result: 401 (Logon failed.)

### Response

**Marin Bratanov** answered on 26 Oct 2020

Hi, Check the Troubleshooting section of the NuGet Feed article to see how to resolve this: [https://docs.telerik.com/blazor-ui/installation/nuget#troubleshooting](https://docs.telerik.com/blazor-ui/installation/nuget#troubleshooting) Regards, Marin Bratanov
