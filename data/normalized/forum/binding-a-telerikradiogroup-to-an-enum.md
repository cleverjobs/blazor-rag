# Binding a TelerikRadioGroup to an enum

## Question

**che** asked on 29 Jul 2021

Hello, I tried to implement a TelerikRadioGroup bound to an enum by following Marin's example code posted here, but I'm doing something wrong. I have attached my Razor component as a TXT file. The result when I run the code is this: Thanks again for your support. Francis

## Answer

**Marin Bratanov** answered on 29 Jul 2021

Hello, The issue in this sample is that the data collection uses one model that correctly has a field of the type of the enum, but the TextField and ValueField names of the RadioGroup were set to the field names of a different class that has 1) no data associated with it and 2) no field of the type of the enum to match the actual data. So, here's the fixed code with highlights on the changes: @SelectedMode
<br />
@* in this case the value is the enum type *@@SelectedMode.GetType()
<br />
<TelerikRadioGroup Data="@UpdateModeData" @bind-Value="@SelectedMode" TextField="@nameof( EnumUpdateModeModel.UpdateModeTextField )" ValueField="@nameof( EnumUpdateModeModel.UpdateModeValueField )">
</TelerikRadioGroup>

@code {
UpdateMode SelectedMode { get; set; } protected override async Task OnInitializedAsync ( ) { //prepare instances of the model from the list of enum values and a desired string representation for the user foreach (UpdateMode item in Enum.GetValues( typeof (UpdateMode)))
{
UpdateModeData.Add( new EnumUpdateModeModel { UpdateModeTextField=item.ToString(), UpdateModeValueField=item });
}

SelectedMode=UpdateMode.ByIndividualDate; base.OnInitialized();
} public enum UpdateMode
{
ByIndividualDate=1,
AllDates=2 } // This class is not used in the code - the Data collection is populated from EnumUpdateModeModel // so that is the class you should use for the field settings of the radio group //public class UpdateModeModel //{ // public UpdateMode UpdateModeId { get; set; } // public string UpdateModeText { get; set; } //} public class EnumUpdateModeModel { public UpdateMode UpdateModeValueField { get; set; } public string UpdateModeTextField { get; set; }
}

List<EnumUpdateModeModel> UpdateModeData { get; set; }=new List<EnumUpdateModeModel>();

} Regards, Marin Bratanov

### Response

**chesk345** commented on 29 Jul 2021

Sakes alive - I'm a little embarrassed. Thanks once again, Marin. I need to buy you a few drinks, dude!

### Response

**Marin Bratanov** commented on 29 Jul 2021

You're welcome, glad I could help :)
