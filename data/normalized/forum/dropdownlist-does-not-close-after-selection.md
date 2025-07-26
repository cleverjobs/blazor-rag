# Dropdownlist does not close after selection

## Question

**And** asked on 11 Feb 2021

The dropdownlist does not close after selecting a value from the list. It will close once it has lost focus. I tested this is chrome and firefox and there no JavaScript errors in the thrown <label class="ic-Label" for="RoomTypes">Room Type:</label> <TelerikDropDownList Id="RoomTypes" Width="230px" Data="@RoomTypes" TextField="Text" ValueField="Value" @bind-Value="_appData.RoomSearchData.RoomType"></TelerikDropDownList> does anyone have an idea?

## Answer

**Eric R | Senior Technical Support Engineer** answered on 12 Feb 2021

Hi Andrew, Thank you for providing the component markup. I suspect the behavior is because the selectedValue data type is of a different type than the ValueField object. Let me explain more with a sample below. Sample In the following component, notice the selectedValue is a string data type and the MyValueField is an int. This is an invalid scenario that can cause similar issues. This is one possible (invalid) implementation to cause the behavior where the dropdown only closes after it has lost focus even though the selection does change. <span> You Selected Value: @selectedValue </span> <br /> <br /> <label for="Items"> Items: </label> <TelerikDropDownList Id="Items" Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" @bind-Value="selectedValue"> </TelerikDropDownList> @code {
public class MyDdlModel
{ public int MyValueField { get; set; } public string MyTextField { get; set; }
} string selectedValue { get; set; } IEnumerable <MyDdlModel> myDdlData=Enumerable.Range(1, 20).Select(x=> new MyDdlModel { MyTextField=$"item{x}", MyValueField=x });
} Potential Fix <span> You Selected Value: @selectedValue </span> <br /> <br /> <label for="Items"> Items: </label> <TelerikDropDownList Id="Items" Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" @bind-Value="selectedValue"> </TelerikDropDownList> @code {
public class MyDdlModel
{ public int MyValueField { get; set; } public string MyTextField { get; set; }
} int selectedValue { get; set; } IEnumerable <MyDdlModel> myDdlData=Enumerable.Range(1, 20).Select(x=> new MyDdlModel { MyTextField=$"item{x}", MyValueField=x });
} Wrapping Up Understandably, the above implementation and potential fix may not apply to your scenario. If your implementaiton is different, I ask that you provide more information about your data model and data collection for the DropDownList. In the meantime, please let me know if you need any additional information. Thank you. Regards, Eric R | Senior Technical Support Engineer

### Response

**Andrew** answered on 12 Feb 2021

Thanks that worked, but I do find it weird that is will still bind the selected value and work except that the ui does not update. If there is an internal error then maybe there is away to display bring that forward to the developer or just ignore it.

### Response

**Jesse** commented on 13 Jun 2024

I'm still having the issue that the OP had, even after making sure the data types match, and the data type is a Value type (in this case it is a struct - DateOnly). <FormItem Field="@nameof(HpuDonation.HpuScheduledPickupDate)">
<Template>
<TelerikDropDownList Width="150px" ValueField="@nameof(PickupDateTargetCapacity.PickupDate)" Data="@PickupDates" @bind-Value="@Donation.HpuScheduledPickupDate">
<ValueTemplate>
@((context as PickupDateTargetCapacity).PickupDate.ToString( "MMMM d" ))
</ValueTemplate>
<ItemTemplate>
@((context as PickupDateTargetCapacity).PickupDate.ToString( "MMMM d" ))
</ItemTemplate>
</TelerikDropDownList>
</Template>
</FormItem>

@code { public IEnumerable<PickupDateTargetCapacity> PickupDates { get; set; }=new List<PickupDateTargetCapacityDto>(); public HpuDonation Donation { get; set; } public class HpuDonation { public DateOnly HpuScheduledPickupDate { get; set; } // other fields } public class PickupDateTargetCapacity { public DateOnly PickupDate { get; set; } // other fields }
} Where am I making the error?

### Response

**Andrew** commented on 14 Jun 2024

I was just wondering does it work if you make HpuDonation.HpuScheduledPickupDate of type object or of type ' PickupDateTargetCapacity'? Do you think the issue could be that you are binding a list of objects that are of type 'PickupDateTargetCapacity' and trying set the selected value into a property of type 'DateOnly'

### Response

**Hristian Stefanov** commented on 18 Jun 2024

Hello Jesse, Andrew, I already addressed this question as there is a public item duplicate for the same scenario: TelerikDropDownList doesn't close after selection. Kind Regards, Hristian
