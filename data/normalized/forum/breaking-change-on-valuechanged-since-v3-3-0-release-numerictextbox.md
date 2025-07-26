# Breaking change on ValueChanged since v3.3.0 release? (NumericTextBox)

## Question

**Eco** asked on 28 Jun 2022

Hello, Here is the issue we encoure since version 3.3.0 of Telerik for Blazor. Everything worked fine in version 3.2.0. We have a simple Input model, and a classic form. The behavior that we want is "when Value1 changes, Value2 must change with custom logic". Here is our code: <p> Value1 : @Person.Value1 </p> <p> Value2 : @Person.Value2 </p> <TelerikForm Model="@Person"> <FormValidation> <DataAnnotationsValidator> </DataAnnotationsValidator> </FormValidation> <FormItems> <FormItem Field="@(nameof(Person.Value1))"> <Template> <label class="k-label k-form-label"> Value 1 </label> <div class="k-form-field-wrap"> <TelerikNumericTextBox Decimals="2" Format="C" Min="0" Step="0.01m" ValueChanged="@((decimal? v)=> Value1ChangedHandler(v))" Value="@Person.Value1" ValueExpression="@(()=> Person.Value1)"> </TelerikNumericTextBox> <TelerikValidationMessage For="@(()=> Person.Value1)"> </TelerikValidationMessage> </div> </Template> </FormItem> <FormItem Field="@(nameof(Person.Value2))"> </FormItem> </FormItems> </TelerikForm> public partial class Example { private Input Person { get; set; }=new (); protected override void OnInitialized ( ) {
Person=new ()
{
Value1=1000,
Value2=2000,
}; base.OnInitialized();
} private void Value1ChangedHandler ( decimal? newValue1 ) { this.Person.Value1=newValue1; this.Person.Value2=newValue1 * 2; // We tried to add StateHasChanged(), but not working as well
}
} public class Input { public decimal? Value1 { get; set; } public decimal? Value2 { get; set; }
} I attach two GIF recordings, the first is version 3.2.0 (working as expected), the second is version 3.3.0, you will see that the behavior is very odd. Thanks a lot in advance. // Dylan

## Answer

**Radko** answered on 01 Jul 2022

Hello Emmanuel, I used the provided code snippet to test the behavior in both a local server-side project using 3.4.0(our latest release), as well as older versions. I also tested it in REPL. In all my tests the component behaved as expected(as shown in V3.2.0.gif). I am wondering if it could be something due to the update, like a cache issue for example - clearing it might help. I am also attaching a gif of the observed behavior. In the meantime, could you please have a look here: [https://blazorrepl.telerik.com/GmaVEFOJ51bfIkBu29,](https://blazorrepl.telerik.com/GmaVEFOJ51bfIkBu29,) and let me know if this works for you? The REPL is running our latest version (3.4.0). Thanks! Regards, Radko Stanev

### Response

**Ecofip** commented on 04 Jul 2022

Hello @Radko, Thanks a lot for your answer, and you were right, it was a cache issue. We fell sorry for that but maybe it could help someone in future! Thanks again, /// Dylan
