# .NET 8 Interactive mode on individual components

## Question

**thi** asked on 15 Dec 2023

Hi, I'm currently evaluating Telerik UI for Blazor using the new .NET 8 capabilities. I'm trying to have static pages (using the default SSR mode) with interactive islands of individual components on the page using RenderMode.InteractiveAuto Looking at the setup documentation here [https://docs.telerik.com/blazor-ui/getting-started/web-app#43-add-the-telerikrootcomponent](https://docs.telerik.com/blazor-ui/getting-started/web-app#43-add-the-telerikrootcomponent) it says that it's possible to set it only for specific pages and components, but then it says that <TelerikRootComponent> needs to wrap the entire view port (i.e. the whole <div class="page"> ) Is there a way to create interactive islands at a component level with Telerik UI for Blazor? Thanks

### Response

**Charles** commented on 28 Dec 2023

Hi All, Bumping this thread up. What we have observed is that there seem to be attributes in some Telerik UI Components that trigger the TelerikRootComponent error. For instance, the "ShowColumnMenu" attribute in TelerikGrid seems to break the app when being set in the razor page. I manage to replicate the problem using the steps mentioned. Steps: 1. Create a Blazor Webapp project using the Telerik Template 2. Configure it to follow the "render mode per page" mode according to the steps on this link: [https://docs.telerik.com/blazor-ui/getting-started/web-app#configure-the-render-mode-per-page](https://docs.telerik.com/blazor-ui/getting-started/web-app#configure-the-render-mode-per-page) 3. Add a TelerikGrid and check the behavior with or without the said attribute. Attaching the code here for reference - Please refer to the Counter.razor page for the scenario. Thanks

### Response

**Svetoslav Dimitrov** commented on 29 Dec 2023

Hello Charles and all viewing this thread, I am happy to see that you have almost implemented the needed behavior you are after. The only thing missing was wrapping the content of the Counter page with the created TelerikLayout. I have modified the application and attached it (TelerikBlazor1) so you can review it and further experiment. On the topic of the "dynamic interactive island" - I have attached another application "TelerikSSR". You can refer to the StaticPageWithInteractiveGrid.razor file to see how I implemented this.

### Response

**Charles** commented on 23 Jan 2024

Hi Svetoslav, Thank you for sending the updated code. I confirm that this is working and is currently being used as reference in our migration to NET8. Regards, Charles
