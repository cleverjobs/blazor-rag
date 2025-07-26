# Demo "paste-from-excel" generates errors

## Question

**Sté** asked on 12 Jul 2021

Hi, I downloaded the Telerik UI for Blazor Trial (version 2.25.0) and I'm investigating the "paste-from-excel" demo (first one I have to go through) from GitHub paste-from-excel (.Net 5.0). Unfortunately I get the following runtime errors (see screenshot). I'm using: VS 2019 Enterprise 16.10.2 Chrome 91.0.4472.124 Does anyone know how to fix it? I would really appreciate any help because I'm far from saying to upper management that this is the right library for us. Thanks in advance

## Answer

**Marin Bratanov** answered on 12 Jul 2021

Hello Stéphane, If you are using a Trial version, you must replace the references in the project to the trial names of the Telerik packages (amend ".Trial") to them: project ref: [https://github.com/telerik/blazor-ui/blob/master/grid/paste-from-excel/PasteFromExcel.csproj#L8](https://github.com/telerik/blazor-ui/blob/master/grid/paste-from-excel/PasteFromExcel.csproj#L8) should be <PackageReference Include="Telerik.UI.for.Blazor.Trial " Version="2.2 5.0" /> static assets: [https://github.com/telerik/blazor-ui/blob/master/grid/paste-from-excel/Pages/_Host.cshtml#L14-L15](https://github.com/telerik/blazor-ui/blob/master/grid/paste-from-excel/Pages/_Host.cshtml#L14-L15) should be <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor.Trial /css/kendo-theme-default/all.css" /> <script src="_content/Telerik.UI.for.Blazor.Trial /js/telerik-blazor.js" defer> </script> Those samples generally come with the commercial references as that's their most common audience. If this does not help, enable the detailed errors here [https://github.com/telerik/blazor-ui/blob/master/grid/paste-from-excel/Startup.cs#L30](https://github.com/telerik/blazor-ui/blob/master/grid/paste-from-excel/Startup.cs#L30) services.AddServerSideBlazor(opts=> opts.DetailedErrors=true ); to see what the actual error is, and see if it is one of those: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors) Regards, Marin Bratanov

### Response

**Stéphane** answered on 12 Jul 2021

Hi, It's working!!! Thanks a lot

### Response

**Marin Bratanov** commented on 13 Jul 2021

Glad I could help :)
