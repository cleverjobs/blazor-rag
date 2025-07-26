# How to add GridColumn from an Object on an Object with the same key

## Question

**Rog** asked on 16 Jan 2020

I am trying to use the Telerik Grid but am getting an error: Microsoft.AspNetCore.Components.Server.Circuits.RemoteRenderer: Warning: Unhandled exception rendering component: An item with the same key has already been added. Key: Title Version=2.6.0 I have a List called skills that holds a list of Skill objects The Skill object has a string property called Title The Skill object has an object property called Department The Department object has a string property called Title as well. In the grid I want to show the Title from the Skill and the Title from the Department...here is the code <TelerikGrid Data="@skills" Height="calc(100vh - 150px)" Pageable="false" Sortable="true" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="false" Reorderable="true"> <GridColumns> <GridColumn Field="@(nameof(Skill.Title))"></GridColumn> <GridColumn Field="@(nameof(Skill.Department.Title))" Title="Department"></GridColumn> </GridColumns> </TelerikGrid> But I am getting this error and I can't seem to find a way to work around it without creating a custom class. Microsoft.AspNetCore.Components.Server.Circuits.RemoteRenderer: Warning: Unhandled exception rendering component: An item with the same key has already been added. Key: Title System.ArgumentException: An item with the same key has already been added. Key: Title at System.Collections.Generic.Dictionary`2.TryInsert(TKey key, TValue value, InsertionBehavior behavior) at Telerik.Blazor.Components.Grid.Extensions.ColumnExtensions.GroupTitles(IEnumerable`1 columns) at Telerik.Blazor.Components.TelerikGridBase`1.GetGroupTitles() at Telerik.Blazor.Components.TelerikGrid`1.<BuildRenderTree>b__0_1(RenderTreeBuilder __builder2) at Microsoft.AspNetCore.Components.Rendering.RenderTreeBuilder.AddContent(Int32 sequence, RenderFragment fragment) at Microsoft.AspNetCore.Components.CascadingValue`1.Render(RenderTreeBuilder builder) at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment) at Microsoft.AspNetCore.Components.RenderTree.Renderer.RenderInExistingBatch(RenderQueueEntry renderQueueEntry) at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessRenderQueue() Microsoft.AspNetCore.Components.Server.Circuits.CircuitHost: Error: Unhandled exception in circuit 'nYpuCoL1tuhOnJfvQJicLrdf3xOuc3npfnJ-aZdQ7EA'.

## Answer

**Marin Bratanov** answered on 17 Jan 2020

Hello Roger, The direct cause is that the nameof() operator returns only the property name, without the class name before it, so you end up with two columns that point to a Title field. Right now, for this to work you'd need to flatten the models - aAt the moment, nested models don't work yet, please click the Follow button on this page to get email notifications on when it becomes possible (I have added your Vote for you to raise its priority, even though it is already in our sights): [https://feedback.telerik.com/blazor/1432615-support-for-nested-complex-models.](https://feedback.telerik.com/blazor/1432615-support-for-nested-complex-models.) Once this gets implemented, you should be able to use the nested model, but it will likely have to be a hardcoded string or a different operator because nameof() does not fit the bill. Regards, Marin Bratanov

### Response

**Roger** answered on 17 Jan 2020

Thank you for the information.
