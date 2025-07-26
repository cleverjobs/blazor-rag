# uirHelper NavigateTo Problem

## Question

**Oli** asked on 28 May 2019

Hoping you can help with this? Running Blazor Server side and the Telerik controls. When I call (any navigateTo) uriHelper.NavigateTo($"/qutes/view/" + quoteId); I see the URL change in the browser, but in the console get. Only throws errors on the Telerik Controls. Debug System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.Grid.TelerikGridRowBase`1.ExecuteCommand(String name) at Microsoft.AspNetCore.Components.EventCallbackWorkItem.InvokeAsync[T](MulticastDelegate delegate, T arg) at Microsoft.AspNetCore.Components.ComponentBase.Microsoft.AspNetCore.Components.IHandleEvent.HandleEventAsync(EventCallbackWorkItem callback, Object arg) at Microsoft.AspNetCore.Components.Rendering.Renderer.DispatchEventAsync(Int32 eventHandlerId, UIEventArgs eventArgs) Microsoft.AspNetCore.Components.Server.ComponentHub: Warning: Unhandled Server-Side exception Web Server VisualBlazor> warn: Microsoft.AspNetCore.Components.Browser.Rendering.RemoteRenderer[100] VisualBlazor> Unhandled exception rendering component: Object reference not set to an instance of an object. VisualBlazor> System.NullReferenceException: Object reference not set to an instance of an object. VisualBlazor> at Telerik.Blazor.Components.DropDownList.TelerikDropDownListBase`2.OnParametersSet() VisualBlazor> at Microsoft.AspNetCore.Components.ComponentBase.CallOnParametersSetAsync() VisualBlazor> at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync() VisualBlazor> warn: Microsoft.AspNetCore.Components.Server.ComponentHub[0] VisualBlazor> Unhandled Server-Side exception

## Answer

**Marin Bratanov** answered on 28 May 2019

Hi Oliver, This is a bug in the grid that we intend to fix very soon (hopefully, as soon as next week). The error is thrown in the innards of the grid, and for a server-side scenario it breaks the SignalR connection, which causes the next view to not be loaded. You can track its status through the Follow button on this page (I already added your vote): [https://feedback.telerik.com/blazor/1406672-application-hangs-during-telerikgridcommandbutton.](https://feedback.telerik.com/blazor/1406672-application-hangs-during-telerikgridcommandbutton.) Regards, Marin Bratanov

### Response

**Oliver** answered on 29 May 2019

Marin, Thank you for the response, now I can stop trying to work around it :). FYI it also occurs in dropdownlist base. System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.DropDownList.TelerikDropDownListBase`2.OnParametersSet() at Microsoft.AspNetCore.Components.ComponentBase.CallOnParametersSetAsync() at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync() Microsoft.AspNetCore.Components.Server.ComponentHub: Warning: Unhandled Server-Side exception

### Response

**Marin Bratanov** answered on 29 May 2019

Is this also in a grid, Oliver? Can you send me a small repro so I can see what's going on? By the way, if you attach the CRUD events of the grid, the original error should go away. You can find an example of how to use them in the following article: [https://docs.telerik.com/blazor-ui/components/grid/editing/overview.](https://docs.telerik.com/blazor-ui/components/grid/editing/overview.) You would need them anyway to perform the actual CUD operations over the real data source/access layer. --Marin

### Response

**Oliver** answered on 02 Jun 2019

Hi Marin, Yep on the grid also. I tried to add the CRUD operations and get a No overload for 'UpdateHandler' matches delegate 'Action<GridCommandEventArgs>'. Am I missing something here? I've pulled Telerik.UI.for.Blazor v0.5.0 from Nuget. Have you guys released some updates in your MSI? I also can't add column filters to the grids.

### Response

**Marin Bratanov** answered on 03 Jun 2019

Hi Oliver, At the moment, the latest release is 1.1.0 and we are planning a 1.2.0 for this week. For 1.0.0 we changed some of the grid events, and then we also made them use EventCallback to allow for async code, and I suspect this is why the current docs can't build on the 0.5.0 version - the docs are for the latest version. You should be able to access 1.1.0 through our NuGet feed too, though, judging from your license info. If you don't see the 1.1.0 version there, delete our feed, restart the PC, and re-add it with storing the credentials in plain text: [https://docs.telerik.com/blazor-ui/installation/nuget.](https://docs.telerik.com/blazor-ui/installation/nuget.) You can, alternatively, try a local feed after downloading the zip archive for the 1.1.0 version from your account: [https://docs.telerik.com/blazor-ui/installation/zip.](https://docs.telerik.com/blazor-ui/installation/zip.) On the dropdown nulll reference issue - I'd suggest reviewing this thread, as we have not yet been able to reproduce such a problem, and the info there may help: [https://www.telerik.com/forums/dropdownlist-in-telerikgrid-editortemplate-throws-nullreferenceexception.](https://www.telerik.com/forums/dropdownlist-in-telerikgrid-editortemplate-throws-nullreferenceexception.) Regards, Marin Bratanov

### Response

**Oliver** answered on 04 Jun 2019

Hi Marin, Updated everything to the latest versions. Still getting the dropdown list issue on two of my lists, but not the datagrid or a dropdown bound to an entity model. Tried setting the binding as per your examples. It does work if I breakpoint oninit() and give it a second or two - using Chrome BTW. You should be able to recreate this issue I suspect. A code snip included below of the guilty dropdown. Also, when I change a list bound to a datagrid, it no longer updates the list on statehaschanged? Is there something else needed to call the refresh? Thank you <TelerikDropDownList bind-Value="@PageData.QuoteState" Width="300px" Data="@states" TextField="stateName" ValueField="stateID"> </TelerikDropDownList> <ValidationMessage For="@(()=> PageData.QuoteState)"></ValidationMessage> public List<statesModel> statesList { get; set; } public class statesModel { public string stateID { get; set; } public string stateName { get; set; } } public IEnumerable<statesModel> states=new List<statesModel> { new statesModel { stateID="Not Selected", stateName="Not Selected" }, new statesModel { stateID="ACT", stateName="ACT" }, new statesModel { stateID="NSW", stateName="NSW" }, new statesModel { stateID="NT", stateName="NT" }, new statesModel { stateID="QLD", stateName="QLD" }, new statesModel { stateID="SA", stateName="SA" }, new statesModel { stateID="TAS", stateName="TAS" }, new statesModel { stateID="VIC", stateName="VIC" }, new statesModel { stateID="WA", stateName="WA" } };

### Response

**Marin Bratanov** answered on 04 Jun 2019

Hi Oliver, It seems there is an issue when binding to a nullable string, I have logged it for further review, and I also added a sample of how this should work: [https://feedback.telerik.com/blazor/1411763-binding-to-a-null-string-value-throws-nullreferenceexception.](https://feedback.telerik.com/blazor/1411763-binding-to-a-null-string-value-throws-nullreferenceexception.) The change from the snippet you posted is in how the hint is provided and that it needs to be null for required validation to work. As to how this plugs in a grid - I suspect that some rows have a null value for the field that the dropdown should use, and this is why you get a similar problem. Such cases are to be handled through a default item, which is why its value should be null. Regards, Marin Bratanov

### Response

**tomas** answered on 19 Jul 2019

With version 1.3.0 & preview 6 I am still receiving following error blazor.server.js:1 [2019-07-19T22:53:51.316Z] Information: Normalizing '_blazor' to '[http://localhost:52288/_blazor'.](http://localhost:52288/_blazor'.) scripts.js:352 expand scroll menu scripts.js:352 expand scroll menu blazor.server.js:1 [2019-07-19T22:53:51.689Z] Information: WebSocket connected to ws://localhost:52288/_blazor?id=2os3Otdyz1khuUTbAQr-lQ. blazor.server.js:15 [2019-07-19T22:54:29.821Z] Error: System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.Grid.TelerikGridContentCellBase.get_PropInfo() at Telerik.Blazor.Components.Grid.TelerikGridContentCellBase.get_PropType() at Telerik.Blazor.Components.Grid.TelerikGridContentCell.BuildRenderTree(RenderTreeBuilder builder) at Microsoft.AspNetCore.Components.ComponentBase.<.ctor>b__5_0(RenderTreeBuilder builder) at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment) at Microsoft.AspNetCore.Components.Rendering.Renderer.RenderInExistingBatch(RenderQueueEntry renderQueueEntry) at Microsoft.AspNetCore.Components.Rendering.Renderer.ProcessRenderQueue() e.log @blazor.server.js:15 blazor.server.js:1 [2019-07-19T22:54:29.822Z] Information: Connection disconnected. scripts.js:352 expand scroll menu Navigation to the first form is OK, navigation to second form with followin command cause erorr message. Example: <TelerikGridCommandButton Command="Edit" Icon="edit" OnClick="TriggerEdit">Edit</TelerikGridCommandButton> void TriggerEdit(Telerik.Blazor.Components.Grid.GridCommandEventArgs args) { ................. uriHelper.NavigateTo("/plovakdetail"); }

### Response

**Marin Bratanov** answered on 22 Jul 2019

Hi Tomas, Does this happen for you when you use a custom command and not the built-in Edit command? The Edit command is designed so you have an event and the chance to react to the user action, not to unload the view - the grid has still a bunch of work to do at the moment the event fires. If you want to implement some custom logic instead of handle the edit event, you should use a custom command. I am attaching below an example that seems to work fine for me with the 1.3.0 version and Preveiw 6. I am also attaching a short video of the experiment so you can see if this is the behavior you are looking for. I am also attaching an experiment with the Edit command that also seems to work as expected for me so you can compare against it. If this does not help you resolve the problem, please modify my sample to showcase the problem you are facing so I can inspect it. Regards, Marin Bratanov

### Response

**tomas** answered on 22 Jul 2019

When I use Command="CusotomEdit" everything is ok. Problem is in case, when there is a Command="Edit" Thanks for help.

### Response

**Marin Bratanov** answered on 23 Jul 2019

Hello Tomas, Please modify my sample to showcase this, because it works fine for me with our latest version (1.3.0 at the time of writing). Once I can see the problem, I can better understand what is going on and we can see whether it is something we can fix. Regards, Marin Bratanov
