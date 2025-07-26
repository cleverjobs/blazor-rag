# MultiSelect OnBlur

## Question

**Ada** asked on 09 Mar 2021

I have a requirement to be able to select multiple values. I have filtering enabled, but I only want the user to be able to select valid values and not enter custom data. My approach would be to clear any invalid data when the control loses focus. The documentation says the OnBlur event should be available but I only have OnChange and OnRead. I believe the functionality I want to mimic is similar to the ComboBox control AllowCustom="false" option. I'm using the latest version of the controls.

## Answer

**Nadezhda Tacheva** answered on 12 Mar 2021

Hi Adam, Since the Multiselect by nature is an input and a dropdown with available options, the user is able to type in the input, however whatever is entered in the input will not be included in the Value of the Multiselect (we even have an open feature request for Adding AllowCustom feature in Multiselect in case you need that at some point). On the point of available options to proceed with in case like yours, I consider the approach you suggested very useful for the your scenario and in general. The current behavior of the Multiselect is to not clear the input after it looses focus (as it is for example in the ComboBox ) and therefore I logged a bug report for Clearing MultiSelect input when it looses focus. As I logged it on your behalf, you are subscribed to receive email notifications when its status changes (this is the best way to know when a bug is fixed). I also added your vote to keep proper track of the requests. In the meantime, a possible workaround (see the below snippet) could be to use a JavaScript function to clear the input and call it through JS Interop in the OnBlur event (you've mentioned that you don't have OnBlur event, it is available as of release 2.22.0 and should be visible in the intellisense. However, after testing the workaround any difficulties appear, please let us know, so we can assist). @inject IJSRuntime JsInterop

<TelerikMultiSelect Filterable="true" Data="@Countries" @bind-Value="@Values" Placeholder="Enter Balkan country, e.g., Bulgaria" Width="350px" ClearButton="true" AutoClose="false" OnBlur="@OnBlurHandler">
</TelerikMultiSelect>

@if (Values.Count> 0 )
{
<ul>
@foreach ( var item in Values)
{
<li>@item</li>
}
</ul>
}

@code {
List<string> Countries { get; set; }=new List<string>();
List<string> Values { get; set; }=new List<string>(); async Task OnBlurHandler ( ) { await JsInterop.InvokeVoidAsync( "clearMultiselectInput" );
} protected override void OnInitialized ( ) {
Countries.Add( "Albania" );
Countries.Add( "Bosnia & Herzegovina" );
Countries.Add( "Bulgaria" );
Countries.Add( "Croatia" );
Countries.Add( "Kosovo" );
Countries.Add( "North Macedonia" );
Countries.Add( "Montenegro" );
Countries.Add( "Serbia" );
Countries.Add( "Slovenia" ); base.OnInitialized();
}
} <script> function clearMultiselectInput ( ) { var inputs=document.querySelectorAll( ".k-multiselect-wrap .k-searchbar input" );
inputs.forEach(e=> e. value="" )
}
</script> Another good thing you might consider is to use the Placeholder parameter to provide hint to the user - for example "Select option from the list, custom options are not supported". Regards, Nadezhda Tacheva
