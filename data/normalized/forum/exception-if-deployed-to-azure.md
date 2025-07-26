# Exception if deployed to Azure

## Question

**Bru** asked on 03 Sep 2019

I added a chart to my application and it runs locally. When I deploy it to Azure, nothing is displayed and an error is logged on the browser console.

## Answer

**Marin Bratanov** answered on 03 Sep 2019

Hello Bruno, The error (and what I see in the response) is that the main index file is returned instead of our script. My best guess on the reason is that static files are not enabled on the ASP.NET Core project that hosts the Blazor app: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#static-assets.](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#static-assets.) My second best guess is that something goes wrong with the deployment and the container that is used does not support static files at all. There was a similar issue in the framework and you can see the details here: [https://feedback.telerik.com/blazor/1414447-error-with-static-assets-after-updating-from-1-1-1-to-1-2-0-when-hosted-on-azure-app-service.](https://feedback.telerik.com/blazor/1414447-error-with-static-assets-after-updating-from-1-1-1-to-1-2-0-when-hosted-on-azure-app-service.) I'd suggest testing with a sample project that has a static asset (other than our project of course) to see if that works. All that said, you can try using our CDN instead (make sure to upgrade the version in the URL to match the package version): <script src="[https://kendo.cdn.telerik.com/blazor/1.6.0/telerik-blazor.min.js"](https://kendo.cdn.telerik.com/blazor/1.6.0/telerik-blazor.min.js") defer> </script> Regards, Marin Bratanov

### Response

**Bruno** answered on 03 Sep 2019

Yes, Bingo, "static files are not enabled on the ASP.NET Core project". Because I did not work like recommended: The method Configure() has another signature in the newest preview: public void Configure(IComponentsApplicationBuilder app) { app.AddComponent<App>("app"); app.UseStaticFiles(); -> Does not compile }

### Response

**Bruno** answered on 03 Sep 2019

Using <script src="[https://kendo.cdn.telerik.com/blazor/1.6.0/telerik-blazor.min.js"](https://kendo.cdn.telerik.com/blazor/1.6.0/telerik-blazor.min.js") defer> </script> works! Thanks! I did not find a ways to use app.UseStaticFiles()

### Response

**Marin Bratanov** answered on 03 Sep 2019

Hi Bruno, Is this an ASP.NET Core Hosted type of project? If yes, then you need to enable the static files on the server project, not where the actual Blazor app is. In case you are using a purely client-side project, then I am not aware of ways to get static files working with it, unless you manually copy them over to the hosting server. Regards, Marin Bratanov

### Response

**Bruno** answered on 03 Sep 2019

When I add it the the server parts it gets deployed everything is working fine. Thanks!

### Response

**Marin Bratanov** answered on 03 Sep 2019

That's good to hear, Bruno, thanks for letting me know. I marked the relevant posts as answers for clarity. If you are OK with this, I would move this thread to the public forum (I would remove the link to your site if you wish) so other people can find it. Regards, Marin Bratanov

### Response

**Bruno** answered on 03 Sep 2019

Yes, it's ok, and please remove the link to my site.

### Response

**Marin Bratanov** answered on 03 Sep 2019

Thanks, the thread is now public at [https://www.telerik.com/forums/exception-if-deployed-to-azure](https://www.telerik.com/forums/exception-if-deployed-to-azure) Regards, Marin Bratanov
