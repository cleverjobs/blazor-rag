# DropDownList DefaultText is empty

## Question

**Art** asked on 04 Aug 2020

Hi, I created a DropDownList in my blazor app. With defaultText property. When DropDownList is rendered it does not show any text Unfortunately I can't paste the print screen. Labrary: Telerik.UI.for.Blazor 2.15.0 Thanks, Artem Code <TelerikDropDownList Data="@Activities" @bind-Value="@SelectedActivitiesIds" TextField="@nameof(Activity.ActivityId)" ValueField="@nameof(Activity.Code)" DefaultText="Select Activity" Width="200px" Id="ddlActivity"> </TelerikDropDownList>

## Answer

**Marin Bratanov** answered on 05 Aug 2020

Hello Artem, The DefaultText is shown only when the Value (SelectedActivitiesIds) has the default value of its type (such as 0 for an integer, null for a string). You need to make sure that it does not match the value of an existing item in the data source. You can see how this works in the very first example here. Another thing to consider is what happens when the value of the Value field is not contained in the data source - if the view-model populates it so, the dropdown list cannot make a decision what to do, so it will show up blank. You can read more about this and other considerations you should keep in mind here. That said, I also made an example that works fine for me so you can compare against it: <TelerikDropDownList Data="@Activities" @bind-Value="@SelectedActivitiesIds" TextField="@nameof(Activity.ActivityId)" ValueField="@nameof(Activity.Code)" DefaultText="Select Activity" Width="200px" Id="ddlActivity">
</TelerikDropDownList>

@code { public class Activity { public int Code { get; set; } public string ActivityId { get; set; }
}

IEnumerable<Activity> Activities=Enumerable.Range( 1, 20 ).Select(x=> new Activity { ActivityId="item " + x, Code=x }); int SelectedActivitiesIds { get; set; }=0; // the default for an int is 0, so this will show the default text. I could have simply avoided setting it as well } Regards, Marin Bratanov

### Response

**Artem** answered on 05 Aug 2020

Hi Marin, thanks for your quick reply yes your example works for me, it was my mistake to define selected value as a list, but for DropDownList is only one selected value at the time. Thanks, Artem
