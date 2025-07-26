# Allow Selecting AM/PM by pressing A or B on keyboard

## Question

**And** asked on 12 Feb 2021

When typing in time in the timepicker (enter hours,enter mins, arrow up/down for AM/PM) it would be nice if I could select AM or PM by pressing A or P on the keyboard also. Is there anyway this can be added?

## Answer

**Marin Bratanov** answered on 13 Feb 2021

Hello Andrew, While A and P might be very common symbols, there are many other symbols that might be used in different countries and cultures. Thus, the component cannot track all such possible combinations, and it exposes the Up and Down Arrows as options to change the time segments, including the AM/PM indicator. Regards, Marin Bratanov

### Response

**Andrew** answered on 13 Feb 2021

Even it is was just a starting with filter or free entry for that field Is there anyway for me to add some type of feature using a keypress even? The issue I am having is some people who just type in the time do not like using the arrow keys

### Response

**Marin Bratanov** answered on 13 Feb 2021

Hello Andrew, You can get input events such as keydown as described in this KB article: Capture input keyboard events. So, if you detect an A or P key you could change the Value as desired (e.g., add or subtract 12 hours depending on the current hours). Regards, Marin Bratanov

### Response

**Andrew** answered on 16 Feb 2021

Is does not look like the timepicker has these events available I tried onkeydown and onkeypress and got an error for both

### Response

**Marin Bratanov** answered on 16 Feb 2021

Hi Andrew, They are not built-in, because exposing so many events like that will be a major performance hit for a small percentage of people who need them. Thus, you must capture them as they bubble up the DOM in a parent element, as described in the article I linked: [https://docs.telerik.com/blazor-ui/knowledge-base/inputs-handle-keyboard-events.](https://docs.telerik.com/blazor-ui/knowledge-base/inputs-handle-keyboard-events.) Here's an example I made for you so you can use as base for further development: @TheTime <span @onkeydown="@OnKeyDownHandler"> <TelerikTimePicker Format="hh:mm:ss tt" @bind-Value="@TheTime"></TelerikTimePicker>
</span>
@code{
DateTime TheTime { get; set; }=DateTime.Now; async Task OnKeyDownHandler ( KeyboardEventArgs e ) { if (e.Key.ToLowerInvariant()=="p" && TheTime.Hour <12 )
{ await Task.Delay( 20 );
TheTime=TheTime.AddHours( 12 );
} if (e.Key.ToLowerInvariant()=="a" && TheTime.Hour> 12 )
{ await Task.Delay( 20 );
TheTime=TheTime.AddHours( -12 );
}
}
} Regards, Marin Bratanov
