# Event Spamming from Controls

## Question

**Joe** asked on 22 May 2025

I have a custom grid filter where I use an animation container to show/hide. When a value changes, I want to close the animation container similar to how the filter automatically closes on your control filters (treelist). So, I have a button that toggles the filter state (ExpandCollapse). Then, when a value changes in my filter (textbox in example) I call a method that should close the filter and refresh my data. I find the OnChange event is called once a value is changed (textbox) but then also when the DatePicker closes and when the DropDownList closes and when the animation container is closed. The result is the toggle kinda goes nuts. Its open/closed/opened at times where it shouldn't. How do I get around this? <div class="gsi-background-color-light" style="height: 41px; display:flex;justify-content:space-between;"> <div class="align-self-center gsi-font-kendo gsi-margin-0"> Patient Filters </div> <TelerikButton Id="filterChevronButton" FillMode="Clear" Class="gsi-border-width-0 gsi-border-color-white gsi-padding-8" Icon="@( FilterVisible? Telerik.SvgIcons.SvgIcon.Filter : Telerik.SvgIcons.SvgIcon.Filter)" OnClick="@(()=> ExpandCollapse())" /> </div> <TelerikAnimationContainer @ref="@AnimContainer" Class="gsi-background-color-light gsi-margin-5 k-rounded-0" Width="100%" Height="100vm"> <TelerikStackLayout Spacing="1px" Class="gsi-margin-5"> <TelerikCard Width="25vh"> <CardBody> <div class="form-group-short"> <label class="col-form-label" for="firstName"> First Name </label> <br /> <TelerikTextBox @bind-Value="@FirstNameFilter" Name="firstName" Placeholder="-No Filter-" OnChange="@(x=> OnFilterChanged(nameof(FirstNameFilter), x))"> </TelerikTextBox> </div> private async Task OnFilterChanged(string propertyName, object newValue)
{
await GetPatients();
ExpandCollapse(false);
} I tried to compare the existing value with the new value after removing the binding but, no success. private async Task OnFilterChanged(string propertyName, object newValue)
{
object existingValue=this.GetPropertyValue(propertyName);
if (newValue !=existingValue)
{
this.SetPropertyValue(propertyName, newValue);

await GetPatients();
ExpandCollapse(false);
}
} Toggle public async void ExpandCollapse(bool? filterVisible=null)
{
if (filterVisible.HasValue)
{
await AnimContainer.ToggleAsync();
FilterVisible=filterVisible.Value;
}
else
{
await AnimContainer.ToggleAsync();
FilterVisible=!FilterVisible;
}
}

### Response

**Nadezhda Tacheva** commented on 27 May 2025

Hi Joel, To look further into this scenario, please provide an isolated runnable sample that replicates your exact configuration and reproduces the exact behavior you are experiencing.

### Response

**Joel** commented on 27 May 2025

Yea... I don't have time for that. I added a button press to apply the filter instead of doing it after a value change from all of my controls. Hopefully, my product manager will be okay with this. If not, I'll come back to it.

### Response

**Nadezhda Tacheva** commented on 29 May 2025

Thank you for the update, Joel! I am glad you found a solution that works for the time being and in case you need additional assistance with the case, please do not hesitate to reach out.
