# Manually rendering a cell's content in a grid column

## Question

**Ste** asked on 24 Nov 2021

Hi, This might be a bit of a strange question and it is hard for me to explain why I'm trying to achieve this, so please don't ask why, but here's a short summary of what I'm trying to achieve: - I've created my own GridColumn class which inherits from the Telerik GridColumn class. - In this class, I want to somehow be able to manually edit the column's cell content through C# code. I found some info on how to manually manipulate components and elements here: [https://docs.microsoft.com/en-us/aspnet/core/blazor/advanced-scenarios?view=aspnetcore-6.0](https://docs.microsoft.com/en-us/aspnet/core/blazor/advanced-scenarios?view=aspnetcore-6.0) - The thing is, I'm not sure how to use the RenderTreeBuilder to access the column cell and edit its contents, for example with a custom template or a simple string. - I'm well aware I can simply provide a template to the GridColumn in Razor, but I'm trying to find a programmatic approach where I can do it in C# code. public class GridColumn: Telerik.Blazor.Components.GridColumn { protected override void BuildRenderTree ( RenderTreeBuilder builder ) { base.BuildRenderTree(builder); //logic goes here }
} Would this be possible? Thank you!

## Answer

**Marin Bratanov** answered on 25 Nov 2021

Hello Stefan, You can define RenderFragment code in C# to generate templates, and so easily point the appropriate template parameter to that method. This can help you get started: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-dynamic-column-template](https://docs.telerik.com/blazor-ui/knowledge-base/grid-dynamic-column-template) Regards, Marin Bratanov Progress Telerik

### Response

**Stefan** commented on 26 Nov 2021

Hi Martin, Thank you, this has helped me a lot so far. I was trying the child component solution that's being mentioned in that tutorial, but I can't seem to get it to work. Could you provide me with an example on how to add a child component to the GridColumn and pass the context to it? That would probably solve my problem completely. Thank you!
