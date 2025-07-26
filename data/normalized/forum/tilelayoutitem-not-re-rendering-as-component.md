# TileLayoutItem not re-rendering as component

## Question

**Ric** asked on 21 Dec 2023

Hi there! I have created a component (Component) that is a TileLayoutItem. It renders fine for the first time but it doesn't re-render after its properties changes (OnClickHandler). Am I doing something wrong? The exact same code works if added directly on Main. Running example: [https://blazorrepl.telerik.com/mnbQmvlX24maslQE52](https://blazorrepl.telerik.com/mnbQmvlX24maslQE52) Component <TileLayoutItem>
<HeaderTemplate>
<a href="#">Component<span class="k-icon k-i-caret-alt-right widget-title-icon"></span></a>
</HeaderTemplate>
<Content>
@test
<TelerikButton OnClick="@OnClickHandler">Click me!</TelerikButton>
</Content>
</TileLayoutItem>
@code { private string test="Button was not clicked yet"; private void OnClickHandler ( MouseEventArgs args ) {
test="Button was clicked at: " + DateTime.Now.ToString();
}
} Main <TelerikTileLayout Columns="1">
<TileLayoutItems>
<Component></Component>
<Component></Component>
<TileLayoutItem>
<HeaderTemplate>
<a href="#">TileLayoutItem<span class="k-icon k-i-caret-alt-right widget-title-icon"></span></a>
</HeaderTemplate>
<Content>
@test
<TelerikButton OnClick="@OnClickHandler">Click me!</TelerikButton>
</Content>
</TileLayoutItem>
</TileLayoutItems>
</TelerikTileLayout>
@code { private string test="Button was not clicked yet"; private void OnClickHandler ( MouseEventArgs args ) {
test="Button was clicked at: " + DateTime.Now.ToString();
}
}

## Answer

**Radko** answered on 25 Dec 2023

Hi Ricardo, The event callback is executed in a different location than the one where the TileLayout is, thus is not aware it should re-render. In other words, the TileLayout is not a descendant of the Component (in fact its the other way around). To workaround this, pass a handler, which when invoked, either re-renders the component the TileLayout is rendered in, or the page. I have modified your snippet to demonstrate this: [https://blazorrepl.telerik.com/wHlmwfPQ49ldGZCn55.](https://blazorrepl.telerik.com/wHlmwfPQ49ldGZCn55.) For more info, I recommend checking when to call StateHasChanged, and more specifically when rendering a component outside the subtree that's rerendered by a particular event. Regards, Radko Progress Telerik
