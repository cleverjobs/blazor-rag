# Not able to select tabs

## Question

**KenKen** asked on 15 Mar 2025

I am new to using the UI for Blazor products. I added the code from [https://www.telerik.com/blazor-ui/documentation/components/tabstrip/overview](https://www.telerik.com/blazor-ui/documentation/components/tabstrip/overview) The control renders but I am not able to select the 3d tab, the control remains on the first tab. Any help on why would be appreciated. Here is the code from the razor page. @page "/Reports/report-main" @using Telerik.Reporting; @using Telerik.Blazor.Components; <h3>Report Main</h3> <!-- Tabs --> <div> <TelerikTabStrip> <TabStripTab Title="First"> First tab content. </TabStripTab> <TabStripTab Title="Second" Disabled="true"> Second tab content. This tab is disabled and you cannot select it. </TabStripTab> <TabStripTab Title="Third"> Third tab content. </TabStripTab> </TelerikTabStrip> </div> @code { }

### Response

**Dimo** commented on 19 Mar 2025

@Ken - make sure that the TabStrip is placed in an interactive . razor file. If the problem persists, send me your test app.

## Answer

**Anislav** answered on 16 Mar 2025

Hi Ken, The provided code sample works as expected, and you can verify this by running it here: [https://blazorrepl.telerik.com/GTEnPKlg37PuAzs130.](https://blazorrepl.telerik.com/GTEnPKlg37PuAzs130.) It seems that the issue may be related to your application's setup. To troubleshoot, check your browser's development tools for any errors. Additionally, try clearing your project's bin and obj folders and rebuilding the project. This often resolves various project-related issues. Regards, Anislav Atanasov

### Response

**Ken** commented on 19 Mar 2025

I added @rendermode InteractiveServer to the web page and I am able to select the tabs. Do I need to add the rendermode to all pages? I am learning both Telerik and Blazor.

### Response

**Dimo** commented on 20 Mar 2025

@Ken - we recommend using a Global interactivity location, so that you don't have to deal with @rendermode at all. If this is not possible, then you need interactive render mode wherever you are using Telerik Blazor components.

### Response

**Ken** commented on 21 Mar 2025

Sorry, but I am not getting what needs to be done from the link. When I added <Routes @rendermode="InteractiveServer" /> it caused the application to refresh the page over and over. Is there a link to a minimal application I can compare to?

### Response

**Dimo** commented on 24 Mar 2025

@Ken>> When I added <Routes @rendermode="InteractiveServer" /> it caused the application to refresh the page over and over. This suggests that the TabStrip is placed in an app section, which must remain static, for example, the Account section of a Microsoft Identity project template. In this case, setting a global unconditional interactive render mode is not possible, because Microsoft Identity requires static render mode. Referring to our linked interactive render mode documentation....>> The Account section in the Blazor Web App template with identity is static by design. Most Telerik Blazor components cannot work in this section. I am sending a simple app with a working TabStrip.
