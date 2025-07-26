# Percentage Format

## Question

**kha** asked on 06 Sep 2020

Hello, I had a problem with percentage format. whenever i use percentage and input 1 to the numeric text box it shows 100% when i input 0.10 it shows 10% is there a way to fix this ? like inputing 1 will show 1% and inputing 10 will show 10%

## Answer

**Marin Bratanov** answered on 07 Sep 2020

Hi Khashayar, This behavior is expected, because values between [0, 1] correspond to perecentage formatting between [0%, 100%]. I made the following KB article to explain the situation in more detail and to provide examples of substituting a different value for your user: [https://docs.telerik.com/blazor-ui/knowledge-base/numerictextbox-percentage-range.](https://docs.telerik.com/blazor-ui/knowledge-base/numerictextbox-percentage-range.) Regards, Marin Bratanov

### Response

**BlueOcean** answered on 11 Mar 2021

Hi Marin, In this case, is there any way to display the % value rather than the actual value when the user clicks to edit? As in right now we managed to do all of the above as per the example, but when the users clicks on the control to edit the value 50% now turns into 0.5 Is there any neat way to both display and edit with the same format? Cheers, Mark

### Response

**Marin Bratanov** answered on 11 Mar 2021

Hi Mark, Perhaps the masked textbox will serve you better. The only downside is that it is a text input, so you have to parse the value when you need to store or use it. Here's an example that also uses the current culture to put a proper decimal separator in the mask, and a sample way of parsing the data. as string: @TheStringValue
<br /> as double: @PercentageZeroToHundred
<br />
<TelerikMaskedTextBox Mask="@TheMask" IncludeLiterals="true" @bind-Value="@TheStringValue" Label="Percentage:">
</TelerikMaskedTextBox>

@code{ string TheMask { get; set; }=string.Format( "00{0}00%", System.Globalization.CultureInfo.CurrentCulture.NumberFormat.NumberDecimalSeparator); string TheStringValue { get; set; } double PercentageZeroToHundred=> ParseDouble(TheStringValue); double ParseDouble ( string stringVersion ) { if ( string.IsNullOrEmpty(stringVersion))
{ return 0 d;
} double val;
stringVersion=stringVersion.Replace( "%", "" ); if (Double.TryParse(stringVersion, out val))
{ return val;
} return 0 d;
}
} Regards, Marin Bratanov

### Response

**BlueOcean** answered on 12 Apr 2021

Hi Marin, My apologies I had forgotten to reply to this, thanks. Mark
