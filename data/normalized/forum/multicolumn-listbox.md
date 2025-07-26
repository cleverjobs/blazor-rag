# MultiColumn Listbox

## Question

**Ara** asked on 13 Feb 2025

Hi, Do you have any plan to implement MultiColumnListBox? It seems that you have already done that inside MultiColumnComboBox when it opens up.

## Answer

**Tsvetomir** answered on 17 Feb 2025

Hello Arash, A feature request for such a multi-column select component is logged in our public feedback portal: Add the MultiColumnMultiSelect component. I've voted on your behalf to raise its priority. Also, you can subscribe to it to get email notifications for any status changes. In the meantime, a possible alternative to achieve a similar layout is to use the existing ListBox component with an ItemTempate to display multiple columns within each item. Here's a basic example: <TelerikListBox Data="@items" Width="400px" Height="300px"> <ItemTemplate> <div style="display: flex;"> <div style="width: 200px;"> @((context as YourDataType).Column1) </div> <div style="width: 200px;"> @((context as YourDataType).Column2) </div> </div> </ItemTemplate> </TelerikListBox> @code {
List <YourDataType> items=new List <YourDataType> {
new YourDataType { Column1="Item 1", Column2="Description 1" },
new YourDataType { Column1="Item 2", Column2="Description 2" }
// Add more items as needed
};

public class YourDataType
{
public string Column1 { get; set; }
public string Column2 { get; set; }
} I hope you find well the provided information. Regards, Tsvetomir Progress Telerik

### Response

**RandiI** answered on 11 Apr 2025

MultiColumnComboBox already has most of the functionality baked in, so it feels like a natural step to expose that as a standalone MultiColumnListBox component.
