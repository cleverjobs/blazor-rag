# How do I change the title of "Start" or "End" on the TelerikDateRangePicker

## Question

**Ric** asked on 28 Jun 2024

The DateRangeSelector does not offer any properties that allows us to change the Label for start or end date on the TelerikDateRangePicker. Are there any other options beside using JavaScript? What I am thinking at the moment is using the following properties: Then OnAfterRenderAsync, calling into JavaScript with the Id for each and pass in the new display value. In my case: "Check-In Date" and "Check-Out Date"

## Answer

**Tsvetomir** answered on 03 Jul 2024

Hello Rick, Thank you for the clear explanation of the result you are looking for. There are two possible ways to change the DateRangePicker label text. Let me show them below: Use Localization Use our built-in localization. The keys to modify in the. resx file are: DateRangePicker_Start DateRangePicker_End Use CSS Apply the StartId and EndId parameters to control the textbox id attributes, and use custom <label> tags outside the component. If you prefer this approach, make sure to hide the built-in labels of the DateRangePicker. Here is an example of this approach and keep in mind that you may need to adjust the layout and spacing, according to your preferences. <div style="display: flex; gap: 8px;"> <label for="my-start" style="display: inline-block; width: 10em; padding: .2em 0;"> Check-In Date </label> <label for="my-end" style="display: inline-block; width: 10em; padding: .2em 0;"> Check-Out Date </label> </div> <TelerikDateRangePicker @bind-StartValue="@StartDate" @bind-EndValue="@EndDate" StartId="my-start" EndId="my-end" Class="no-labels" /> <style> /* remove reserved space for labels */.no-labels.k-floating-label-container { padding-top: 0;
} /* hide default labels */.no-labels.k-floating-label { display: none;
} </style> @code {
DateTime StartDate { get; set; }
DateTime EndDate { get; set; }
} Regards, Tsvetomir Progress Telerik

### Response

**Greg** commented on 07 Sep 2024

Thank you for the response, this worked for me, however, having a bit of trouble getting the second label to line up with the related box. This is a lot of code for something simple that should be better supported by the control directly. how do we add this to request for feature improvement? I suspect this is super easy to add and makes the control more appropriate for all contexts of date range selection.

### Response

**Rick** commented on 07 Sep 2024

I ultimately ended up using JavaScript to correct the localization. In my opinion, the labels should be properties that we could assign. While JavaScript is not by any means a perfect solution, it does mean I am not hacking through their Css and trying to get it to work. Just my two cents

### Response

**Tsvetomir** commented on 11 Sep 2024

Hello Greg and Rick, Thank you for the provided feedback about the shared approaches. I can inform you that we have a feature request in our
