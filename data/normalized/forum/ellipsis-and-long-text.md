# Ellipsis and long text

## Question

**Kie** asked on 07 Jan 2021

Hi, In my Blazor grid, I have a column which can have long text in it. I need to use ellipsis on this column e.g put ellipsis after say 50 characters, with the full content then displayed in a tooltip when you hover on the ellipsis. I know this was possible with your other grids, how can I do this with your blazor grid? Thanks,

## Answer

**Svetoslav Dimitrov** answered on 07 Jan 2021

Hello Kieran, We have a Knowledge Base article that explains how to achieve the desired behavior. You can see it from this link. Also, you can tweak the CSS so that it fits the needs of your application. Regards, Svetoslav Dimitrov

### Response

**Kieran** answered on 07 Jan 2021

Thanks Svetoslav I had missed that article.

### Response

**Leland** answered on 04 Apr 2024

I used the code from the referenced knowledge base articles in many places throughout my project, so I ended up creating a self-contained component to handle this. It can be used like this: <GridColumn Field="@nameof(DataModel.Notes)" Title="Notes" Width="150px"> <Template> @{ var dataItem=(DataModel)context; } <OverflowTooltip Text="@dataItem.Notes" /> </Template> </GridColumn> You'll need to have the TelerikTooltip set up somewhere in your project: <TelerikTooltip TargetSelector=".tooltip-target" /> It uses the ellipsis and a tooltip to show the full text. I even added JavaScript so that the tooltip is only displayed when the overflow is active. Here's the code: OverflowTooltip.razor: <div @ref="DivRef" class="custom-ellipsis"> @Text </div> OverflowTooltip.razor.css: div.custom-ellipsis { overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
} OverflowTooltip.razor.cs: using Microsoft.AspNetCore.Components; using Microsoft.JSInterop; namespace ProjectName.Components; public partial class OverflowTooltip {
[ Parameter ] public string? Text { get; set; } private ElementReference DivRef { get; set; }

[ Inject ] private IJSRuntime JSRuntime { get; set; }=default!; private static IJSObjectReference? JSModule { get; set; } protected override async Task OnAfterRenderAsync ( bool firstRender ) { if (JSModule is null )
{ var path="./Components/OverflowTooltip.razor.js";
JSModule=await JSRuntime.InvokeAsync<IJSObjectReference>( "import", path);
} await JSModule.InvokeVoidAsync( "initializeTooltipCheck", DivRef);
}
} OverflowTooltip.razor.js: export function initializeTooltipCheck ( element ) { let isOverflowing=false; function checkOverflow ( ) {
isOverflowing=handleOverflowCheck (isOverflowing, element);
} checkOverflow (); const resizeObserver=new ResizeObserver (checkOverflow);
resizeObserver. observe (element);

element. addEventListener ( 'DOMNodeRemoved', ()=> {
resizeObserver. disconnect ();
});
} function handleOverflowCheck ( isOverflowing, element ) { const currentOverflowing=element. offsetWidth <element. scrollWidth; if (currentOverflowing !==isOverflowing) { if (currentOverflowing) {
element. classList. add ( "tooltip-target" );
element. setAttribute ( "title", element. textContent );
} else {
element. classList. remove ( "tooltip-target" );
element. removeAttribute ( "title" );
}
} return currentOverflowing;
}
