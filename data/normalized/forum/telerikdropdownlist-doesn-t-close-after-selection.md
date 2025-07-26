# TelerikDropDownList doesn't close after selection

## Question

**Jes** asked on 13 Jun 2024

I have a telerik dropdownlist that isn't closing after selection. I've looked at the answer posted here: Dropdownlist does not close after selection in UI for Blazor | Telerik Forums, but that doesn't solve my issue. My value fields match (I am using DateOnly), and the value is a Value type (struct). <FormItem Field="@nameof(HpuDonation.HpuScheduledPickupDate)">
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

## Answer

**Hristian Stefanov** answered on 18 Jun 2024

Hi Jesse, Thank you for explaining in such detail what you are experiencing. The problematic behavior stems from the current data binding configuration of the DropDownList in the provided code snippet. The component's Value parameter is set to a property of type DateOnly. However, the Value parameter needs to be either a string or a value type (such as int, decimal, bool, or Enum ). Alternatively, you can bind it to a model. In that case, the TextField and ValueField parameters should point to properties of string or value type. It's essential that the Value parameter type matches the type of the ValueField property. I modified the provided code to demonstrate the needed change: @using System.ComponentModel.DataAnnotations <TelerikForm Model="@Donation"> <FormValidation> <DataAnnotationsValidator> </DataAnnotationsValidator> </FormValidation> <FormItems> <FormItem LabelText="Scheduled Pickup Date" Field="@nameof(HpuDonation.HpuScheduledPickupDate)"> <Template> <TelerikDropDownList Width="150px" ValueField="@nameof(PickupDateTargetCapacity.PickupDate)" TextField="@nameof(PickupDateTargetCapacity.DisplayDate)" Data="@PickupDates" @bind-Value="@Donation.HpuScheduledPickupDate" /> </Template> </FormItem> </FormItems> </TelerikForm> @code {
public IEnumerable <PickupDateTargetCapacity> PickupDates { get; set; }=new List <PickupDateTargetCapacity> ();
public HpuDonation Donation { get; set; }=new HpuDonation();

protected override void OnInitialized()
{
PickupDates=new List <PickupDateTargetCapacity> {
new PickupDateTargetCapacity { PickupDate="2023-06-14", DisplayDate="June 14, 2023" },
new PickupDateTargetCapacity { PickupDate="2023-06-15", DisplayDate="June 15, 2023" },
new PickupDateTargetCapacity { PickupDate="2023-06-16", DisplayDate="June 16, 2023" },
new PickupDateTargetCapacity { PickupDate="2023-06-17", DisplayDate="June 17, 2023" },
new PickupDateTargetCapacity { PickupDate="2023-06-18", DisplayDate="June 18, 2023" }
};
}

public class HpuDonation
{
public string HpuScheduledPickupDate { get; set; }
// other fields
}

public class PickupDateTargetCapacity
{
public string PickupDate { get; set; }
public string DisplayDate { get; set; }
// other fields
}
} Regards, Hristian Stefanov Progress Telerik

### Response

**Jesse** commented on 18 Jun 2024

Hi Hristian, Thanks for your response. DateOnly is a struct, which, unless I am mistaken, structs are value types in c#, so I'm still not sure why my original code doesn't work. Your example works as a workaround for now though.

### Response

**Hristian Stefanov** commented on 20 Jun 2024

Hi Jesse, Thank you for getting back to me. I'm glad to see that the modified sample works for you. Regarding the use of the DropDownList with the DateOnly type directly, could you please clarify your specific use case? Generally, the DropDownList component is designed to work with value types such as int, decimal, bool, and Enum. This is because we have dedicated components for handling dates, such as the DatePicker. If you could provide more details on the specific requirement you have for using DateOnly with the DropDownList, it would help us understand your needs better and consider possible enhancements to the component. Kind Regards, Hristian

### Response

**Jesse** commented on 27 Jun 2024

We have a use case where we have generated a list of specific dates that span a few months (basically 6 dates over 3 months) that we need the user to select from. In this case it doesn't make sense to the use the datepicker and have the user hunt down the few active dates on a calendar. Whether that is worth a feature enhancement, I'm not sure, but for now I'm using the workaround you proposed.

### Response

**Hristian Stefanov** commented on 02 Jul 2024

Hi Jesse, I highly appreciate your feedback and I'm glad to hear that the approach I proposed is working for you. If you encounter any difficulties in the future, please let me know so we can revisit the idea for a feature enhancement. Kind Regards, Hristian
