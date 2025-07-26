# tabstrip-- is there a way to put an entire page and it's associated code-behind file as part of a tabstriptab content?

## Question

**Law** asked on 03 Jun 2021

Is there a way to put an entire page and it's associated code-behind file as part of a tabstriptab content? I'm having a problem styling the entire "page" since it has a component containing a tab strip and it always ends up on the left side of the page and the content ends up on the right side of the page. The best thing would be to put the content in the tab content itself but i don't want to put all that html and code into one file that contains the tabstriptab. Thanks, Lawrence.

## Answer

**Eric R | Senior Technical Support Engineer** answered on 07 Jun 2021

Hi Lawrence, This can definitely be achieved in Blazor. This is a major feature in Razor Components which is the underlying technology behind Blazor. Let me review a sample of how to do this below. Example Using the default Telerik UI for Blazor Visual Studio Project Template, I moved the content of the Index page into a new component named HelloWorld and moved it into into a Components folder below the Shared folder along with the FetchData and Counter pages as shown in the below screenshot. This enabled using the Index.razor page as a TabStrip which can output the following within the control. Essentially, it will allow composing components within the TasbStrip as desired. The TabStrip on the Index.razor page is shown in the below code snippet. Note that it references each component individually. @page "/" <h1> Dashboard </h1> <TelerikTabStrip> <TabStripTab Title="Hello World!"> <HelloWorld> </HelloWorld> </TabStripTab> <TabStripTab Title="Fetch Data"> <FetchData> </FetchData> </TabStripTab> <TabStripTab Title="Counter"> <Counter> </Counter> </TabStripTab> </TelerikTabStrip> Wrapping Up For additional reference, attached is a sample that illustrates the above implementation. To run the sample locally, ensure the Telerik NuGet Feed is Configured in Visual Studio. For more information on nesting Blazor components in advanced scenarios, see the Blazor University - Components section. Alternatively, I encourage taking some time to review our Video On-Demand Training which will provide an excellent foundation for developing with UI for Blazor. Please let me know if you need any additional information. Thank you for being a valued UI for Blazor developer. Regards, Eric R | Senior Technical Support Engineer

### Response

**Martin Herløv** commented on 05 Nov 2021

When will a tab component be loaded? Will the FetchData component be loaded when the dashboard are loaded?

### Response

**Eric R | Senior Technical Support Engineer** commented on 09 Nov 2021

Tabs are loaded when they are activated. Additionally, tabs initialize their content only when they are activated. Tabs that are not active are unloaded and removed from the render tree and document object model. This means the FetchData component will load only when activated and not when the Dashboard page loads unless the FetchData component tab is activated on page load.
