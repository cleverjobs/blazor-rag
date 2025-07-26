# Add Icon to Selected Item

## Question

**Ila** asked on 07 Mar 2021

I would like to add an Icon next to the selected item text as shown in the attached image. Is it possible?

## Answer

**Marin Bratanov** answered on 08 Mar 2021

Hello Ilan, You can use the ValueTemplate to add custom content to the main element of the dropdownlist. You can also see how to use Telerik Font Icons in the Icons article. If you want to select dates (judging by the icon), I can suggest you use the DatePicker component instead of the DropDownList component. Here is an example I made for you: <TelerikDropDownList Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" Value="1"> <ValueTemplate> <TelerikIcon Icon="calendar" /> &nbsp; <strong> @((context as MyDdlModel).ExtraField) </strong> </ValueTemplate> </TelerikDropDownList> @code {
public class MyDdlModel
{
public int MyValueField { get; set; }
public string MyTextField { get; set; }
public string ExtraField { get; set; }
}

IEnumerable <MyDdlModel> myDdlData=Enumerable.Range(1, 20).Select(x=>
new MyDdlModel
{
MyTextField="item " + x,
MyValueField=x,
ExtraField="more item info " + x
}
);
} Regards, Marin Bratanov
