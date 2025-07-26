# Chart not displaying

## Question

**GioGio** asked on 24 Jul 2019

Hi, I just couldn't make the chart to show even with your demo codes here -> [https://docs.telerik.com/blazor-ui/components/chart/types/column](https://docs.telerik.com/blazor-ui/components/chart/types/column) Could this be a bug? I'm using the following: .NET Core version 3.0.100-preview7-012821 VS 2019 Enterprise 16.2.0 Preview 3 Telerik.UI.for.Blazor version 1.3.0

## Answer

**Marin Bratanov** answered on 24 Jul 2019

Hi Gio, Our demos work fine for me, I'm attaching a screenshot below. Can you confirm all network requests to our server are successful on your end? Do you get any errors? As for a local run - our latest version (1.3.0 at the moment) is compatible with Preview 6. We are working on a compatibility with Preview 7 and it will be available as soon as possible. You can subscribe to the following thread where I'll post an update when that happens: [https://www.telerik.com/forums/net-core-3-preview-7-support.](https://www.telerik.com/forums/net-core-3-preview-7-support.) The showstopper at the moment is that the VS 2019 Preview update that will make it compatible with Preview 7 is still unavailable and we need to wait for that. Regards, Marin Bratanov

### Response

**Gio** answered on 24 Jul 2019

Thanks Marin. There's indeed an error (see attached) Could not find 'TelerikBlazor' in 'window'. I've switched to 3.0.100-preview6-012264 this time.

### Response

**Marin Bratanov** answered on 25 Jul 2019

Hi Gio, This indicates that our JS Interop file has not loaded. Can you confirm you have it referenced as explained here: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#client-assets?](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#client-assets?) On the reference numbers - the correct ones for Preview 6 were <PackageReference Include="Microsoft.AspNetCore.Blazor" Version="3.0.0-preview6.19307.2" /> <PackageReference Include="Microsoft.AspNetCore.Blazor.DevServer" Version="3.0.0-preview6.19307.2" /> and for a client app they were <PackageReference Include="Microsoft.AspNetCore.Blazor" Version="3.0.0-preview6.19307.2" /> <PackageReference Include="Microsoft.AspNetCore.Blazor.Build" Version="3.0.0-preview6.19307.2" PrivateAssets="all" /> which indicates that the 3.0.100-preview6-012264 packages are incorrect references and can also lead to issues. With that said, I'd suggest you wait out for the upcoming 1.4.0 release that will be compatible with Preview7 and upgrade to both. You can subscribe to this thread where I will post an update once it becomes available: [https://www.telerik.com/forums/net-core-3-preview-7-support.](https://www.telerik.com/forums/net-core-3-preview-7-support.) Regards, Marin Bratanov

### Response

**Gio** answered on 25 Jul 2019

Yup I missed those! I guess I was too excited. Thanks so much Marin. I'll be testing the new stuff and monitoring the progress against the previews. Perhaps, it's better to at least mention in the demo page, that some steps need to be done in order to make things work.

### Response

**Marin Bratanov** answered on 26 Jul 2019

Hello Gio, The full set of instructions are available in the documentation, as the demos should showcase specific features only. Here are the most relevant articles for getting started and configuring a project: client-side Blazor project walkthrough: [https://docs.telerik.com/blazor-ui/getting-started/client-blazor](https://docs.telerik.com/blazor-ui/getting-started/client-blazor) server-side Blazor project walkthrough: [https://docs.telerik.com/blazor-ui/getting-started/server-blazor](https://docs.telerik.com/blazor-ui/getting-started/server-blazor) more condensed and technical information: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need](https://docs.telerik.com/blazor-ui/getting-started/what-you-need) Regards, Marin Bratanov
