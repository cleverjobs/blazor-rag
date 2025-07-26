# HeaderTemplate's component events

## Question

**Iva** asked on 19 Dec 2020

Hello! Place TelerikNumericTextBox component in TileLayoutItem's HeaderTemplate. The up/down buttons will not trigger and cause for tile's reordering event. <TileLayoutItem ColSpan="4" RowSpan="7"> <HeaderTemplate> <span>Title</span> <TelerikNumericTextBox Value="@interval" ValueChanged="@ChangeInterval" Step="1" T="int" Min="0" Max="50" /> </HeaderTemplate> <TileLayoutItem />

## Answer

**Marin Bratanov** answered on 21 Dec 2020

Hi Ivan, After I fixed the markup (I assume it was a copy-paste issue), this seems to work fine for me with 2.20.0. I am attaching below a short video from one of my tests so you can confirm if I am missing something. If you can reproduce a problem with this, could you modify the snippet and point out what I am missing? <TelerikTileLayout Columns="5" RowHeight="100px">
<TileLayoutItems>
<TileLayoutItem ColSpan="4" RowSpan="7">
<HeaderTemplate>
<span>Title</span>
<TelerikNumericTextBox Value="@interval" ValueChanged="@( (int v)=> ChangeInterval(v) )" Step="1" T="int" Min="0" Max="50" />
</HeaderTemplate>
<Content>The tile</Content>
</TileLayoutItem>
<TileLayoutItem HeaderText="Second">
<Content>Another tile</Content>
</TileLayoutItem>
<TileLayoutItem HeaderText="Three">
<Content>Third tile</Content>
</TileLayoutItem>
</TileLayoutItems>
</TelerikTileLayout>

@code{ int interval { get; set; } void ChangeInterval ( int v ) {
interval=v;
}
} Regards, Marin Bratanov

### Response

**Ivan** answered on 22 Dec 2020

Hello Martin! You need to set Reorderable property of TelerikTileLayout to "true" and problem is reprodused in your sample too.

### Response

**Marin Bratanov** answered on 22 Dec 2020

Hi Ivan, When Reorderable is true, the tile layout captures the mouse events on the header to allow for dragging. That's why you wouldn't be able to focus the input or use other elements with the mouse. If you use Tab to get in the numeric textbox, you will be able to change its value with the keyboard, it's the mouse events that can't get there. I've added a note about this in the docs ( commit link ). Regards, Marin Bratanov

### Response

**Ivan** answered on 22 Dec 2020

Thank you! Рad to place a numeric box field outside the header.

### Response

**Greg** answered on 04 Jan 2021

Perhaps in a future release you can incorporate a button or container for buttons that would allow hiding, minimizing, etc. in the top right of the header by default. So it could be used almost like an accordian.

### Response

**Marin Bratanov** answered on 05 Jan 2021

Hello Greg, The column menu already allows the user to do these things - there is a column chooser so they can hide columns, they can filter, sort, pin columns. You can see it in action here: [https://demos.telerik.com/blazor-ui/grid/column-menu.](https://demos.telerik.com/blazor-ui/grid/column-menu.) In case that's not enough for your case, using the template and adding the desired code is the way to go. You can apply any CSS and popups you require, and you can also use the grid's parameters to bind to fields in the view-model so you can control it, or you can use its state. With all those capabilities already in place, I do not find it likely that a highly specific button container would be created in the grid. Nevertheless, you could open a public feature request in our Feedback Portal to explain the goals, how those features are not enough and what exactly you expect from such a feature. This will let the community vote and comment on such a feature so we can see if there is interest in it. Regards, Marin Bratanov

### Response

**Greg** answered on 05 Jan 2021

Hi Marin. Thanks for the quick reply! However, I am not talking about the grid component - I am talking about the TileLayout and having a header template button added to the TileLayoutItem header.

### Response

**Marin Bratanov** answered on 05 Jan 2021

Hi Greg, My apologies for the mistake, I have no idea why I thought this is about the grid. Maybe because most questions are :) The situation with the tile layout is similar - you should add your own buttons and if they need to change the tile layout settings - you can use parameters and its state and put buttons in its header template. Minimizing is not a feature of the component because it aims at creating a layout on the page, the Window can be minimized. Hiding is something you can do with conditional markup (an if-block around the desired tile) but keep in mind that this can cause issues with the state - the state is loaded sequentially tile by tile, so if it is not applied to the same collection of tiles you can get unexpected sizes and positions. That said, if features like hiding/closing and minimizing ever become available in the tile layout - it is highly likely that there will be some sort of built-in action bar/buttons for that. Regards, Marin Bratanov
