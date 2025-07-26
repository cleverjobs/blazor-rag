# Combobox Value not populate on load

## Question

**Jas** asked on 01 May 2021

I have a simple combobox where the value is not populated on load: <TelerikComboBox Value="@SelectedValue" Data="@SourceColumns" AllowCustom="true" Width="100%" /> @SelecteValue is a string @SourceColumns is an ObservableCollection<String> If I switch it to a drop down list, the item is selected, however I need to be able to have custom values. This seems pretty straight forward, and I am thinking I am missing something minor?

## Answer

**Marin Bratanov** answered on 01 May 2021

Hi Jason, There are two bugs in the combo box in 2.23.0 that will be fixed in the upcoming 2.24.0 (planned for mid-May) that I think might be relevant to your case: about preselected value not showing up see here about selected value not showing text when data is fetched asynchronously see here If you recognize your scenario in one of these - you will get a fix for it when 2.24.0 is available. If you don't, please post a more comprehensive sample to showcase the problem so I can take a look. Regards, Marin Bratanov Progress Telerik

### Response

**Jason** commented on 01 May 2021

That was exactly what was happening. I did find a workaround since it was a custom component, I added parameter attributes to the underlying model that contain the list data and that seems to have fixed the issue.

### Response

**Marin Bratanov** commented on 02 May 2021

Happy to see you have found a solution. Make sure to upgrade to 2.24.0 when it comes out in a couple of weeks, though, it should alleviate that and also bring in a ton of new stuff.
