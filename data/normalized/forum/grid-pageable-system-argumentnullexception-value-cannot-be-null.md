# Grid Pageable System.ArgumentNullException: Value cannot be null

## Question

**Ald** asked on 07 Sep 2020

Hi replicate your demo in my project but adding pageable=true result in nullreferenceexception <TelerikGrid Data="@MyData" Height="400px" Pageable="true" PageSize="10" Page="1" Sortable="true" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="true" Reorderable="true"> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Width="120px" /> <GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Groupable="false" /> <GridColumn Field="@(nameof(SampleData.Team))" Title="Team" /> <GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" /> </GridColumns> </TelerikGrid> @code { public IEnumerable<SampleData> MyData=Enumerable.Range(1, 30).Select(x=> new SampleData { Id=x, Name="name " + x, Team="team " + x % 5, HireDate=DateTime.Now.AddDays(-x).Date }); public class SampleData { public int Id { get; set; } public string Name { get; set; } public string Team { get; set; } public DateTime HireDate { get; set; } } } System.ArgumentNullException: Value cannot be null. (Parameter 'format') at System.String.FormatHelper(IFormatProvider provider, String format, ParamsArray args) at System.String.Format(String format, Object arg0, Object arg1, Object arg2) at Telerik.Blazor.Components.TelerikPager.<BuildRenderTree>b__104_0(RenderTreeBuilder __builder2) at Microsoft.AspNetCore.Components.Rendering.RenderTreeBuilder.AddContent(Int32 sequence, RenderFragment fragment) at Microsoft.AspNetCore.Components.CascadingValue`1.Render(RenderTreeBuilder builder) at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment) at Microsoft.AspNetCore.Components.RenderTree.Renderer.RenderInExistingBatch(RenderQueueEntry renderQueueEntry) at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessRenderQueue()

## Answer

**Marin Bratanov** answered on 07 Sep 2020

Hello Aldo, I am attaching here a small sample built on top of the provided code and it seems to be working fine for me. Could you compare against it and see if you can find the difference causing the problem? If not, could you modify it to showcase the problem you are facing so I can have a look? At this point, my best guess is that perhaps there is some localization service in the problematic project that does not provide the necessary and correct strings for the pager. I'm also attaching a screenshot of the default pager strings with an indication pointing at the most likely culprit for the issue. Regards, Marin Bratanov

### Response

**Aldo** answered on 07 Sep 2020

You're right, missing resources in my .resx Thank you
