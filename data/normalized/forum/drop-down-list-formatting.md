# Drop-Down List Formatting

## Question

**aeh** asked on 20 Aug 2024

I'm creating a drop-down list control that can accept different style sheets to control the font sizes in the control. I have everything working except the drop-down list items. This control could appear on a page more than once, and the controls could be defined with different classes. The styles need to be limited to the scope of the defined CSS. This is how it looks. So, the display is working. HOWEVER, I can't seem to limit the styling of the drop-down. Here is the example of one of the style: <style> /* reduce default 14px font-size */ .k-button.ReportSelectionText08, .k-input.ReportSelectionText08, .k-input.ReportSelectionText08 .k-input-inner.ReportSelectionText08, .k-picker.ReportSelectionText08, .k-picker.ReportSelectionText08 .k-input-inner.ReportSelectionText08 { font-size: 8px; } /* reduce default 4px/8px paddings */ .k-button.ReportSelectionText08, .k-picker.ReportSelectionText08 .k-input-inner.ReportSelectionText08, .k-input.ReportSelectionText08 .k-input-inner.ReportSelectionText08, .k-button.k-input-button.ReportSelectionText08 { padding: 2px 4px; } /* remove default 20px min-height */ .k-button.k-input-button.ReportSelectionText08 .k-button-icon.ReportSelectionText08 { min-height: initial; } /* styles for the dropdown items */ .k-animation-container .k-list .k-list-item { font-size: 8px; padding: 2px 4px; } </style> The problem is this line: /* styles for the dropdown items */ .k-animation-container .k-list .k-list-item { font-size: 8px; padding: 2px 4px; } This seems to control every control on the page, all of the drop-down item lists will be font size 8. If I try to limit it, like the other example like this : /* styles for the dropdown items */ .k-animation-container.ReportSelectionText08 .k-list.ReportSelectionText08 .k-list-item.ReportSelectionText08 { font-size: 8px; padding: 2px 4px; } It doesn't work. How can I limit the formatting of the drop-down items to be non-global?

## Answer

**Tsvetomir** answered on 22 Aug 2024

Hello Andy, Thank you for the detailed explanation of your scenario. To limit the scope of the defined CSS: Use Item Template. Set a custom CSS class to the HTML tag in the template(e.g., <span class="custom-item">@itemValue</span> ). Apply the desired styles. For your convenience, I've prepared an example with two DropDownList components to see the result of the above approach: Selected value: @selectedValue <br /> <div style="display:flex"> <TelerikDropDownList Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" @bind-Value="selectedValue" DefaultText="Modifed Font Size" Width="300px"> <ItemTemplate> <span class="custom-item"> @context.MyTextField </span> </ItemTemplate> </TelerikDropDownList> <TelerikDropDownList Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" @bind-Value="selectedValue" DefaultText="Default Font Size" Width="300px" /> </div> <style>.custom-item { font-size: 8px;
} </style> @code {
public class MyDdlModel
{
public int MyValueField { get; set; }
public string MyTextField { get; set; }
}

private int selectedValue { get; set; }

private IEnumerable <MyDdlModel> myDdlData=Enumerable.Range(1, 20).Select(x=> new MyDdlModel { MyTextField="item " + x, MyValueField=x });
} Regards, Tsvetomir
