# Floating Textbox - how to

## Question

**Jon** asked on 04 Apr 2020

Hi.. I can't seem to get the 'floating textbox' like in the demos to work. Also how a can I apply Material to just this component? In _Host.chtml I have <script src="_content/telerik.ui.for.blazor/js/telerik-blazor.js" defer></script> <link href="favicon.ico" rel="icon" type="image/x-icon" /> <link href="telerik-themes/bootstrap/dist/all.css" rel="stylesheet" / In startup.cs I have services.AddTelerikBlazor(); My component looks like this @page "/NameAddress" <span class="TitleBlue"> Name + Address</span> <div class="box-content"> <h4>Company Name</h4> <TelerikTextBox Label="Company Name"></TelerikTextBox> </div> @code { } Any ideas? Thx in advance

## Answer

**Svetoslav Dimitrov** answered on 08 Apr 2020

Hello Jonathan, Thank you for participating in our Blazor community! I suspect that by Floating Textbox you mean the floating label for the Textbox component. We have that behavior out-of-the-box. In your _Host.cshtml file you should have something like that (for a server-side app, read more on the ways to reference our styles in our Themes article ): <link rel="stylesheet" href="[https://unpkg.com/@@progress/kendo-theme-default@@latest/dist/all.css"](https://unpkg.com/@@progress/kendo-theme-default@@latest/dist/all.css") /> In that CSS file is the definition for the floating label and if this is missing you might experience difficulties in adding it. The styles are also present in our other two themes (inspired by material and bootstrap). In your case I see a custom theme being loaded and it might somehow be missing those styles. You could try with the built-in ones we provide to compare. Having said that, there might be some CSS rules in your project that, in some way, contradict with the ones we have set. For example, those might be some rules for the span tag, since the class we are adding to make it floating is to a span and is: k-floating-label-container. It is also important to make sure you are using our latest version (2.10.0 at the moment). As for the Material design for a single component. I suspect this is regarding the floating label as well since this, we might say, is practice in the Material design. However, we do not offer such stylistic combinations, but provide themes that cover all components. This is done so for consistency reasons. Regards, Svetoslav Dimitrov

### Response

**Jonathan** answered on 08 Apr 2020

thx again!

### Response

**Svetoslav Dimitrov** answered on 09 Apr 2020

Hello Jonathan, I am glad this explanation helped you solve your problem. Regards, Svetoslav Dimitrov

### Response

**David** answered on 04 May 2020

In the demo, how did you get the textboxes to stack up horizontally? I am using the exact same code as the source in the demo and mine render side by side.

### Response

**Svetoslav Dimitrov** answered on 05 May 2020

Hello David, What we do in the demo is that we use header <h4> tag. In essence this is a block element which breaks the page into different sections. A div element, p, ul or ol will have similar effect in breaking the page in that way. Regards, Svetoslav Dimitrov
