# right alignment

## Question

**Ran** asked on 30 Oct 2019

Is there a way to right align the text in both edit and display modes? Thanks ... Ed

## Answer

**Marin Bratanov** answered on 30 Oct 2019

Hello Ed, Have you tried something like this: [https://stackoverflow.com/questions/12114570/how-to-align-texts-inside-of-an-input?](https://stackoverflow.com/questions/12114570/how-to-align-texts-inside-of-an-input?) Here's an example that did that for me (screenshot attached after the code): <style>
.rightAlign input {
text-align: right;
}
</style>

@DateTime.Now

<br />

@someVal.ToString( "C" )

<TelerikNumericTextBox @bind-Value="@someVal" Class="rightAlign"></TelerikNumericTextBox>

@code{ double someVal=1234.56789;
} public static void Main ( string [] args ) { //this no longer works //System.Threading.Thread.CurrentThread.CurrentCulture=new System.Globalization.CultureInfo("en-US"); //you have to set defaults now var culture=new System.Globalization.CultureInfo( "en-US" );
System.Globalization.CultureInfo.DefaultThreadCurrentCulture=culture;
System.Globalization.CultureInfo.DefaultThreadCurrentUICulture=culture;

CreateHostBuilder(args).Build().Run();
} Regards, Marin Bratanov

### Response

**Doug** answered on 26 Mar 2020

Marin, Will you please shed some more light on the styling for me? Text alignment seems to work ok but I've had trouble with other properties. Hopefully this code demonstrates my confusion around the inconsistencies. I can get the properties to work in the numeric text box using !important (which confuses me but I'm not a css expert) but more specifically how would I get these (and other) properties set in the regular text box? <TelerikNumericTextBox Id="onlyAlignmentGetsSet" @bind-Value="@d" Class="myClass"></TelerikNumericTextBox> <TelerikNumericTextBox Id="colorAndAlignmentGetSet" @bind-Value="@d" Class="myClass1"></TelerikNumericTextBox> <TelerikTextBox Id="neitherPropertyGetsSet" @bind-Value="@s" Class="myClass1"></TelerikTextBox> <style> .myClass input { background-color: aquamarine; text-align: right; } .myClass1 input { background-color: aquamarine !important; text-align: right !important; } </style> @code { public decimal d=123.45m; public string s="test"; }

### Response

**Marin Bratanov** answered on 27 Mar 2020

Hello Doug, The following blog post can help you review the rendered HTML through the browser dev tools so you can see what CSS rules apply to it and how to devise overrides: [https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.](https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.) The key difference (not an inconsistency, though) is that the numeric textbox has more elements than the "standard" textbox. Here's a modified example I made for you: <style> /*numeric textbox. See [https://feedback.telerik.com/blazor/1458547-class-does-not-render-on-the-main-wrapping-element](https://feedback.telerik.com/blazor/1458547-class-does-not-render-on-the-main-wrapping-element) as it will change where the custom class goes in the selector*/.k-numerictextbox.k-numeric-wrap.myClass1.k-input, /*textbox */.myClass1.k-textbox { background-color: aquamarine; text-align: right;
}
</style>

<TelerikNumericTextBox Id=" colorAndAlignmentGetSet " @bind-Value=" @d " Class="myClass1"></TelerikNumericTextBox>
<TelerikTextBox Id="neitherPropertyGetsSet" @bind-Value="@s" Class="myClass1"></TelerikTextBox>

@code
{ public decimal d=123.45m; public string s=" test ";
} Regards, Marin Bratanov
