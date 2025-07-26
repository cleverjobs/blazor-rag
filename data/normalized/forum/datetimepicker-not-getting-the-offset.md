# DateTimePicker not getting the offset

## Question

**kha** asked on 16 Apr 2020

Hello, this is my code ` <TelerikDateTimePicker Format="dd MMM yyyy HH:mm:ss" @bind-Value="DatePickerValue"></TelerikDateTimePicker> DateTimeOffset DatePickerValue { get; set; }=DateTimeOffset.Now; ` and the odd thing is its just giving me the time without offset like it's giving me 14:50 while it's 19:20

## Answer

**Marin Bratanov** answered on 17 Apr 2020

Hello Khashayar, As we discussed a couple of times with you before ( here and here ), you must use a DateTime object. A TimeSpan or DateTimeOffset object is different and is not suitable for this binding. Regards, Marin Bratanov

### Response

**Robert** answered on 05 Oct 2020

Hello! Is there a reason that this component does not support DateTimeOffsets? The OData protocol requires dates going over the wire to be DateTimeOffsets, so this lack of functionality is a HUGE problem for us. Thanks!

### Response

**Marin Bratanov** answered on 05 Oct 2020

Hi Robert, Yes, there is a major reason - the DateTimePicker must provide a set point in time for both a date, and a time of day that is meaningful to the end user. This means that these points need to be relative to something well known (like the Gregorian Calendar) and to be able to match the current time for the usre, while a DateTimeOffset does not, at leas not without extra logic. It is also more susceptible to the user location and settings, which is, again, something the component cannot provide as that's specific to the app. There are many caveats to such a format that must be left to the application requirements (such as time zones). So, I advise that you write a simple field in the view-model whose getter uses the DateTime field from the DateTimePicker component to calculate the desired DateTimeOffset based on the required business logic, and then use that field everywhere you need a DateTimeOffset value instead of a DateTime value. If you don't need special conversions, DateTime can be implicitly cast to a DateTimeOffset. Regards, Marin Bratanov

### Response

**Robert** answered on 05 Oct 2020

I'm sorry, but that reasoning does not make much sense. What the DateTimePicker MUST do is handle the data types coming over the wire, and be able to process them. Letting the visual part of the component pick the timezone is only a *potential* requirement of the app... if my application requirements (or someone else's API requirements) say that all of the times are UTC, the control doesn't HAVE to do anything different...the default assumes UTC. So instead of saying "oh, it's too hard, we can't do it" and forcing people to use undocumented workarounds and waste both their and your time, why not either a) make the component do those conversions internally, or b) support it natively and just tell people if they want their end users to pick the timezone, they need to add their own UI?

### Response

**Marin Bratanov** answered on 06 Oct 2020

Hello Robert, I feel like I am not explaining things right, my apologies. I will try to start from the bottom and summarize things: You can use a DateTimeOffset type with the date inputs/pickers we have. We use the .DateTime field of that DateTimeOffset object and so it is up to the app to determine the offset, timezone and any other needs. We do not offer UI for choosing those timezones or offsets and that's not supported out-of-the-box, because that will vary too greatly between one app and the next. I've also summarized this information in an article: [https://docs.telerik.com/blazor-ui/knowledge-base/date-input-picker-datetimeoffset](https://docs.telerik.com/blazor-ui/knowledge-base/date-input-picker-datetimeoffset) Here's an example that seems to work fine for me and showcases how this operates, and I am attaching a screenshot below that shows how it works for me: @if(TheValue !=null )
{
<p>UTC: @TheValue.UtcDateTime.ToString( "dd MMM yyyy, HH:mm:ss" )</p>
<p>Local: @TheValue.LocalDateTime.ToString( "dd MMM yyyy, HH:mm:ss" )</p>
<p>DateTime (used by Telerik components): @TheValue.DateTime.ToString( "dd MMM yyyy, HH:mm:ss" )</p>
<p>Offset (hours): @TheValue.Offset.Hours</p>
}

<TelerikDateInput @bind-Value="@TheValue" Format="F" Width="400px" />

<br /><br />

<TelerikDateTimePicker @bind-Value="@TheValue" Format="F" Width="400px" />

@code{
DateTimeOffset TheValue { get; set; } protected override void OnInitialized ( ) {
TheValue=new DateTimeOffset(DateTime.Now, new TimeSpan( 3, 0, 0 )); base.OnInitialized();
}
} With that said, if you cannot add the necessary business logic in the initialization of the view-model to take into account the desired offsets and time zones, you may still need to add some fields to calculate that dynamically. The exact way this is done will depend on the business requirements. If you see any issues in such a setup, let's discuss them with concrete examples. Regards, Marin Bratanov
