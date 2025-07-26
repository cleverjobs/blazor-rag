# ChildContent doesn't appear to exist on GridCommandButton

## Question

**Cha** asked on 24 Feb 2022

Hello, per the documentation here: [https://docs.telerik.com/blazor-ui/components/grid/columns/command](https://docs.telerik.com/blazor-ui/components/grid/columns/command) Yet ChildContent doesn't appear to exist? It doesn't come up in IntelliSense. When I try using it anyhow, the text appears in red, or worse, ReSharper thinks it's a constant from some library that hasn't been imported: Your examples don't show how to use ChildContent, so I'm making educated guesses. I can get away from the "red text" by pointing it to a string: <GridCommandButton Command="Test" ChildContent="@test"> </GridCommandButton> and @code {
private string test="Test Content";
} However I get compiler errors, so I don't think that's correct either. It looks like the compiler is expected ChildContent to be a RenderFragment: Error CS0030 Cannot convert type 'string' to 'Microsoft.AspNetCore.Components.RenderFragment' I can use the alternate method of putting the text between the tags: <GridCommandButton Command="Test">Test </GridCommandButton> I initially tried the ChildContent method because I can getting a warning I didn't initially understand when I tried using the text between the tags. I now understand that was a ReSharper warning of no significance. But I thought I'd point out docs for ChildContent appear to be incomplete? Thanks.

### Response

**Rob** commented on 14 Nov 2024

It would be nice to see some example use case of ChildContent in the documentation. I looked into ChildContent to see if it would help me render GridCommandButton dynamic text (for the button) but never was successful. They provide samples here for display of DataItem in command button but it's for Kendo not Blazor. Nothing similar for blazor.

### Response

**Dimo** commented on 15 Nov 2024

@Rob - ChildContent is a standard Blazor RenderFragment, which is used, according to the Microsoft documentation. Our components don't impose any additional specifics or requirements. The linked Kendo UI documentation discusses only Kendo UI API, unlike the case here. The RenderTreeBuilder syntax is cumbersome and not recommended even by Microsoft. I usually find it most effective to create the desired configuration declaratively, enable generated code in the csproj... <PropertyGroup> <EmitCompilerGeneratedFiles> true </EmitCompilerGeneratedFiles> </PropertyGroup> ...and then dive into the generated code in the obj folder to see how it's done. @using System.ComponentModel.DataAnnotations

<TelerikGrid Data="@GridData" EditMode="@GridEditMode.Inline" OnUpdate="@OnGridUpdate"> <GridColumns> <GridColumn Field="@nameof(Product.Name)" /> <GridColumn Field="@nameof(Product.Quantity)" /> <GridCommandColumn Width="400px"> <GridCommandButton Command="Edit" ChildContent="@EditButtonChildContent"> </GridCommandButton> <GridCommandButton Command="Edit" ChildContent="@( (__builder)=> {
__builder.AddContent(0, " Advanced Edit for "); __builder.AddContent ( 1, (( Product ) context ).Name );
} )"> </GridCommandButton> <GridCommandButton Command="Save" ShowInEdit="true"> Save </GridCommandButton> <GridCommandButton Command="Cancel" ShowInEdit="true"> Cancel </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid>

@code {
private List<Product> GridData { get; set; }=new ();

private int LastId { get; set; } private RenderFragment EditButtonChildContent { get; set; }=__builder=> { <text> Simple Edit </text> }; private void OnGridUpdate ( GridCommandEventArgs args ) { var updatedItem=(Product)args.Item; var originalItemIndex=GridData.FindIndex( i=> i.Id==updatedItem.Id); if (originalItemIndex !=- 1 )
{
GridData[originalItemIndex]=updatedItem;
}
}

protected override void OnInitialized ( ) { for (int i=1; i <=5; i++)
{
GridData.Add( new Product ( ) {
Id=++LastId,
Name=$ "Product {LastId}",
Quantity=(short)Random.Shared.Next( 0, 1000 ),
StartDate=DateTime.Now.AddDays(-Random.Shared.Next( 60, 1000 )),
IsActive=LastId % 4> 0 });
}
}

public class Product {
public int Id { get; set; }
[Required]
public string Name { get; set; }=string.Empty;
public decimal Price { get; set; }
public int Quantity { get; set; }
public DateTime StartDate { get; set; }
public bool IsActive { get; set; }
}
}
