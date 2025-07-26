# Combobox popup width adjust to content

## Question

**Kee** asked on 23 Sep 2022

Is it possible to adjust the width of the popup to the length of the items only if it exceeds the width of the control? Thus default it has the same width as the control, unless there are longer items, then it expands to the right. The problem I have now is that when using Virtual Scrolling you have to specify an item height. Text that doesn't fit in de dropdown width is wrapped to a new line, overlapping the next line. I would like instead of wrapping the test the popup to adjust its width to accommodate these texts. I tried it with MinWidth, but don't know what value to specify, 100% doesn't work because it is rendered at a different place in the DOM. Kind regards, Kees Alderliesten

## Answer

**Kees** answered on 28 Sep 2022

Hello Svetoslav, I tried something like that, but I have 100% as width for the control and can't use that for the dropdown (it's located somewhere else in the DOM, thus with different 'parents'). I have to somehow copy the actual width of the control to the width of the div containing the dropdown... Kind regards, Kees Alderliesten

### Response

**Svetoslav Dimitrov** commented on 03 Oct 2022

Hello Kees, Copying the actual width of the component can be achieved by using JavaScript. As this might not be the best approach for a Blazor application I would suggest you hardcode a MinWidth for the popup of the DropDownList that matches the exact width of the component. You can inspect the rendered application and see the width like that. If you will have a dynamic rendering based on the browser dimensions (mobile devices/computer screen) you can use the MediaQuery component to apply different MinWidth based on the screen size.

### Response

**Kees** commented on 03 Oct 2022

Your last suggestion isn't really feasable, the will result in every control in a column perfectly scaling to the width of that colum and the Combobox having a different width based on the mediaquery (unless I make queries for every pixelwidth..) The element containing the dropdown part gets its width in pixels set, so I assume that the control's JS-code is responsible for that. Maybe I should make a feature request that MinWith="auto" (or MinWidth="*" or something) will result in een MinWidth instead of Width with the same pixel amount.

### Response

**Svetoslav Dimitrov** commented on 06 Oct 2022

Hello Kees, Can you send me the markup definition of the ComboBox that does not work for you so that I can suggest any further solutions? Also, you can provide some feedback on what you have tested so far that does not help you achieve the desired behavior. Have you tried my suggestions from the first post?

### Response

**Svetoslav Dimitrov** answered on 28 Sep 2022

Hello Kees, You can achieve the desired behavior by using a combination of MinWidth, MaxWidth, and Width parameters. To make sure that the dropdown is as wide as the input of the ComboBox you can set the MinWidth to the same value as the Width of the ComboBox. The popup Width can be set to auto so that it automatically stretches enough to accommodate the width of the items. The MaxWidth can be set the 100vw (this is 100 viewport width) so that it goes as wide as the viewport. I have prepared a basic example that you can see below: <TelerikComboBox Data="@myComboData" TextField="MyTextField" ValueField="MyValueField" @bind-Value="selectedValue" Placeholder="Select an item..." ClearButton="true" Filterable="true" Width="300px"> <ComboBoxSettings> <ComboBoxPopupSettings Width="auto" MinWidth="300px" MaxWidth="100vw " /> </ComboBoxSettings> </TelerikComboBox> @code {
IEnumerable <MyDdlModel> myComboData=Enumerable.Range(1, 20).Select(x=>
new MyDdlModel
{
MyTextField="item " + x,
MyValueField=x
});

int selectedValue { get; set; }

public class MyDdlModel
{
public int MyValueField { get; set; }
public string MyTextField { get; set; }
}
} Regards, Svetoslav Dimitrov Progress Telerik
