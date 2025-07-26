# Default HeaderTemplate

## Question

**Pon** asked on 17 Feb 2022

Hi guys, In the following code snippet I'm using a HeaderTemplate for my grid. This is working like expected. However I want to use this header template on practically all my columns. Is there an easy way to extract the HeaderTemplate and use that on multiple columns by just setting the HeaderTemplate property? Or can I create some sort of custom GridColumn which has this template automatically implemented? <GridColumn Field="OrderMetadata.CustomerReference"> <HeaderTemplate> <label class="k-checkbox-label"> <TelerikCheckBox ValueChanged="@((bool result)=> OnColumnSelect(result, nameof(WarehouseDocumentListItem.OrderMetadata.CustomerReference)))" /> Customer reference </label> </HeaderTemplate> </GridColumn> Thanks in advance! Regards, Guido

## Answer

**Pondres** answered on 18 Feb 2022

Never mind! Got it to work. For future reference and to help others here's the complete source: public class SelectableGridColumn: GridColumn {
[ Parameter ] public EventCallback<SelectableGridColumn> SelectionChanged { get; set; } public bool IsSelected { get; private set; } private async Task CheckChangedAsync ( bool isSelected ) {
IsSelected=isSelected; await SelectionChanged.InvokeAsync( this );
} protected override void OnParametersSet () { base.OnParametersSet();
HeaderTemplate=GetHeaderTemplate();
} public RenderFragment GetHeaderTemplate () {
RenderFragment headerTemplate=builder=>
{
builder.OpenElement( 1, "label" );
builder.AddAttribute( 1, "class", "k-checkbox-label" );
builder.OpenComponent( 2, typeof (TelerikCheckBox<bool>));
builder.AddAttribute( 2, "ValueChanged", EventCallback.Factory.Create<bool>( this, CheckChangedAsync));
builder.CloseComponent();
builder.AddContent( 3, Title);
builder.CloseElement();
}; return headerTemplate;
}
} Usage within a Grid: <GridColumns> <GridCheckboxColumn CheckBoxOnlySelection="true" /> <SelectableGridColumn Field="DocumentId" Title="Document" SelectionChanged="@OnColumnSelect" /> </GridColumns>

### Response

**Marin Bratanov** answered on 17 Feb 2022

Hello Guido, You can make the template a C# function so that it can reside in one common place and you can call on it from anywhere you need, here is a basic example of a similar approach: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-dynamic-column-template.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-dynamic-column-template.) This is not even specific to the Telerik components, you can use this approach for any Blazor RenderFragment (template). Regards, Marin Bratanov Progress Telerik

### Response

**Pondres** commented on 18 Feb 2022

Hi Marin, Thanks for the info. It's almost where I need it to be but I can't get it to work 100%. I want a TelerikCheckbox in the Header of the column, and I've defined the control as follows. public partial class SelectableGridColumn: GridColumn {
[ Parameter ] public EventCallback<SelectableGridColumn> SelectionChanged { get; set; } public bool IsSelected { get; private set; } private async Task CheckChangedAsync ( bool isSelected ) {
IsSelected=isSelected; await SelectionChanged.InvokeAsync( this );
} protected override void OnParametersSet ( ) { base.OnParametersSet();
HeaderTemplate=GetHeaderTemplate();
} public RenderFragment GetHeaderTemplate ( ) {
RenderFragment headerTemplate=builder=>
{
builder.OpenElement( 1, "label" );
builder.AddAttribute( 1, "class", "k-checkbox-label" );
builder.OpenElement( 2, "TelerikCheckBox" );
builder.AddAttribute( 2, "ValueChanged", EventCallback.Factory.Create<bool>( this, CheckChangedAsync));
builder.CloseElement();
builder.AddContent( 3, Title);
builder.CloseElement();
}; return headerTemplate;
}
} This will create a column, but without the checkbox in the header: Do you have any idea what I might be doing wrong? Thanks again!

### Response

**Pondres** commented on 18 Feb 2022

Moved my comment
