# Drop down shows values followed by white space

## Question

**Vis** asked on 23 Nov 2020

Hello, I want to remove white space in drop down values in blazor. Please see the image below. Could please suggest on this

## Answer

**Vishnu** answered on 22 Jan 2021

Could you please help on this. Thanks Vishnu Vardhanan

### Response

**Nadezhda Tacheva** answered on 25 Jan 2021

Hi Vishnu, The DropDownList has a PopupHeight parameter which controls the height of the expanded dropdown list element. If you set its value to "auto", the Popup will have the necessary height to display its items properly without the white space (see the below snippet for reference). <TelerikDropDownList Data="@myDdlData" PopupHeight="auto" TextField="MyTextField" ValueField="MyValueField" @bind-Value="selectedValue" DefaultText="Select item">
</TelerikDropDownList>

@code { //in a real case, the model is usually in a separate file //the model type and value field type must be provided to the dropdpownlist public class MyDdlModel { public int MyValueField { get; set; } public string MyTextField { get; set; }
} int selectedValue { get; set; }

IEnumerable<MyDdlModel> myDdlData=Enumerable.Range( 1, 3 ).Select(x=> new MyDdlModel { MyTextField="item " + x, MyValueField=x });
} This feature will work just fine if you are providing a small data list to the DropDownList. In case you want to display a large portion of options in the DropDownList, the Popup container might expand beyond the page as there is no MaxPopupHeight set. We have an opened feature request for MaxPopupHeight in our public

### Response

**Vishnu** answered on 28 Jan 2021

Thank Nadezhda...It's working fine.

### Response

**W. Bryant** answered on 06 Jun 2022

If you're looking at this post now it seems as if the accepted answer no longer works. Go to the documentation here: [https://docs.telerik.com/blazor-ui/components/dropdownlist/overview](https://docs.telerik.com/blazor-ui/components/dropdownlist/overview) Scroll for the section on popup settings and you'll get what you're looking for.

### Response

**Nadezhda Tacheva** answered on 09 Jun 2022

Hi W. Bryant, Thank you for pointing this out! Indeed, as of Telerik UI for Blazor 3.0.0, we've extracted the popup configuration in a dedicated Popup settings tag including multiple options. The height of the popup should now be set as follows: <TelerikDropDownList> <DropDownListSettings> <DropDownListPopupSettings Height="..." /> </DropDownListSettings> </TelerikDropDownList> Regards, Nadezhda Tacheva Progress Telerik

### Response

**Ted** commented on 08 Feb 2023

This doesn't really help. Specifying "auto" should fit the popup BOTH minimum height and maximum height so that the popup does not extend below the bottom of its parent container. Currently if there are many items in the popup, setting "auto" for the height extends the popup below the bottom of its container so that items are not visible and also there is no scroll bar, so the popup is totally unusable!! If there are a few items in the popup and "auto" is specified, a bunch of empty rows are placed at the bottom of the popup for some reason?! This is UX 101, so please put a fix in for this!

### Response

**Dimo** commented on 13 Feb 2023

Duplicate discussion. More information at How to set max popup height

### Response

**Joseph** commented on 18 Jan 2024

Please remove this comment. Thanks.

### Response

**Dimo** commented on 18 Jan 2024

@Joseph - our Width and Height parameters are normally strings, because they accept all valid CSS values. The same applies for the Height in DropDownListPopupSettings. A value of "auto" means that the dropdown will expand, according to the number of items inside. You can control the minimum and maximum height with the other available parameters MinHeight and MaxHeight.
