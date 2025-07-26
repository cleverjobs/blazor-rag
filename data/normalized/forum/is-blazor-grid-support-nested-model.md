# is Blazor grid support nested model ?

## Question

**Saj** asked on 17 Apr 2020

Hello Team, Just want to check with regarding Blazor Grid. is it support nested models? basically I want to bind a Object2.Object2.Property Eg: <GridColumn Field=@nameof(ExcelColumn.Settings.Order ) Title="Order" /> Thanks, Sajid

## Answer

**Marin Bratanov** answered on 17 Apr 2020

Hello Sajid, It will, in the upcoming 2.11.0 release: [https://feedback.telerik.com/blazor/1432615-support-for-nested-complex-models.](https://feedback.telerik.com/blazor/1432615-support-for-nested-complex-models.) Note that using the nameof() operator will not work, because it does not provide the object hierarchy, you will need to set the Field as a string you type in. You can preview the explanations on how this will work in the following file in our documentation repo: [https://github.com/telerik/blazor-docs/blob/master/knowledge-base/grid-bind-navigation-property-complex-object.md](https://github.com/telerik/blazor-docs/blob/master/knowledge-base/grid-bind-navigation-property-complex-object.md) Regards, Marin Bratanov

### Response

**Bob** answered on 22 Dec 2020

Hello Marin, Following your example, I am able to get nested property to display in the grid. However, I cannot make it work where I have an object that has 2 instances of NestedObject. For example, I have UpdatedUser and CreatedUser that are both type NestedObject. I cannot display UpdatedUser.Field1 and CreatedUser.Field1 in the same grid. I get the following error: Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100] Unhandled exception rendering component: Arg_AmbiguousMatchException System.Reflection.AmbiguousMatchException: Arg_AmbiguousMatchException at System.RuntimeType.GetPropertyImpl(String name, BindingFlags bindingAttr, Binder binder, Type returnType, Type[] types, ParameterModifier[] modifiers) at System.Type.GetProperty(String name, BindingFlags bindingAttr) at System.Type.GetProperty(String name) at Telerik.Blazor.Extensions.ReflectionExtensions.GetPropertyValue(Object target, String propertyName) at Telerik.Blazor.Extensions.ReflectionExtensions.GetNestedPropertyValue(Object target, String propertyName) at Telerik.Blazor.Components.Grid.GridContentCell`1[[TBS.UI.ViewModels.CaseReviewVM, TBS.UI, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]].get_Value() at Telerik.Blazor.Components.Grid.GridContentCell`1[[TBS.UI.ViewModels.CaseReviewVM, TBS.UI, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]].get_FormattedValue() at Telerik.Blazor.Components.Grid.GridContentCell`1[[TBS.UI.ViewModels.CaseReviewVM, TBS.UI, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]].BuildRenderTree(RenderTreeBuilder __builder) at Microsoft.AspNetCore.Components.ComponentBase.<.ctor>b__6_0(RenderTreeBuilder builder) at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment) at Microsoft.AspNetCore.Components.RenderTree.Renderer.RenderInExistingBatch(RenderQueueEntry renderQueueEntry) at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessRenderQueue()

### Response

**Marin Bratanov** answered on 23 Dec 2020

Hello Bob, Here's a snippet I tried and it seems to work fine for me (I am testing on the latest version which is 2.20.0 at the moment). I'm also attaching a wasm app with it that seems to work fine for me so you can compare against it. <TelerikGrid Data="@myData" Pageable="true" Sortable="true" FilterMode="@GridFilterMode.FilterRow" Groupable="true">
<GridColumns>
<GridColumn Field="@nameof(SampleComplexObject.ID)" Title="ID"></GridColumn>
<GridColumn Field="@nameof(SampleComplexObject.Name)" Title="The Name"></GridColumn>
<GridColumn Title="Field1 from CreatedUser" Field=" CreatedUser. Field1 " />
<GridColumn Title="Field1 from UpdatedUser" Field=" UpdatedUser. Field1 " />
</GridColumns>
</TelerikGrid>

@code { public class SampleComplexObject { public int ID { get; set; } public string Name { get; set; } public User CreatedUser { get; set; } public User UpdatedUser { get; set; } public SampleComplexObject ( ) {
CreatedUser=new User();
UpdatedUser=new User();
}
} public class User { public string Field1 { get; set; } public string OtherField { get; set; }
} public IEnumerable<SampleComplexObject> myData=Enumerable.Range( 1, 50 ).Select(x=> new SampleComplexObject
{
ID=x,
Name="Name " + x,
CreatedUser=new User
{
Field1="created 1 " + x,
OtherField="created 2 " + x % 6 },
UpdatedUser=new User
{
Field1="updated 1 " + x,
OtherField="updated 2 " + x % 6 }
}
);
} Regards, Marin Bratanov

### Response

**Bob** answered on 23 Dec 2020

Hi Marin, Thanks for looking into this. When I changed my code to use ViewModels on the UI, this works fine. When I bind directly to data returned from my web api, I get the AmbiguousMatchException. My best guess is that this is related to EF Core and navigation properties. I've seen other odd issues in webassembly when binding to those objects.

### Response

**Marin Bratanov** answered on 23 Dec 2020

Hello Bob, With WebAssembly you should perform database calls on the server, so the blazor front-end should not use entities, and you would usually bind directly to view-models anyway. These sample projects can help you offload those operations to the server: [https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server](https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server) Regards, Marin Bratanov

### Response

**Bob** answered on 23 Dec 2020

Hi Marin, Do you have any examples using .NET 5 Blazor WebAssembly and an ASP.NET Core Web API?

### Response

**Marin Bratanov** answered on 23 Dec 2020

Hi Bob, The sample I linked before showcases the main concept, it will work with .NET5 too, just upgrade the projects to use .NET 5. Another thing you can do is to generate a new telerik blazo project with our VS extensions - the "CRUD, Form, Chart" sample project with WebAssembly an API controller from the server ASP.NET Core project to work with the data. Regards, Marin Bratanov
