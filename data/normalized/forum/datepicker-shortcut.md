# DatePicker ShortCut

## Question

**JoeJoe** asked on 14 Oct 2019

I want to create character shortcuts and be able to default the date based on the shortcut. This would be similar to how quicken does it within quickbooks. In other words, I want the user to be able to type the letter 'T' for today's date. M for the first day of the month, and so on. I check the OnValueChangedHandler but it doesn't seem to fire for non-numeric characters. Any help would be appreciated, Joe

## Answer

**Marin Bratanov** answered on 15 Oct 2019

Hi Joe, The ValueChanged handler fires as the user enters valid keystrokes, which depend on the format, and they are usually numbers. If the format allows for text input (e.g., contains a segment like MMMM), the user will be able to enter (some) alphabetic characters too, but that does not guarantee the ValueChanged event as it needs a valid value. This means that there is no provision for such a feature in the component. How would you envision such a feature to be exposed? Would you rather have an OnInput event, or a JS element reference to the input, or some highly specific feature for such shortcuts (which would reduce the likelihood of it getting implemented)? What I can suggest in the meantime is that you try using JS Interop to hook to an event like oninput or onkeydown on the <input> element of the picker to execute your own code by obtaining the letter from the JS code. Then, fire up a C# method to set the desired value through two-way binding and setting the value of the field. I cannot guarantee how this would work, though, as the Blazor component may get disposed and re-rendered on various events and that may cause the handler attached with JS Interop to go missing. It is also important to note that Blazor is not designed for such hacks and we do not support such implementations. Regards, Marin Bratanov

### Response

**Joe** answered on 15 Oct 2019

In angular you can do the following: <input type='text' (keydown.enter)="doSubmit()"/> How could you expose the same functionality within a Blazor app? <TelerikDatePicker Enabled="@Enabled" Format="@Format" Value="@Value" OnChange="@(()=> OnChangeHandler())" ValueChanged="@((DateTime d)=> OnValueChangedHandler(d))" keydown.enter="@(()=> doSubmit())"> </TelerikDatePicker> It would be nice if the keydown could be replaced with any other javascript event (keydown, keyup, keypress, input, etc.)

### Response

**Marin Bratanov** answered on 16 Oct 2019

Hi Joe, There's another approach - use the event propagation and capture the keydown event on a parent element of the date picker: <div @onkeydown="@KeyDownHandler">
<TelerikDatePicker Min="@Min" Max="@Max" @bind-Value="@selectedDate"></TelerikDatePicker>
</div>
<div class="pt-4">The selected date is: @selectedDate?.ToShortDateString()</div>

@code { public DateTime Max=new DateTime( 2050, 12, 31 ); public DateTime Min=new DateTime( 1950, 1, 1 ); private DateTime? selectedDate; async Task KeyDownHandler ( KeyboardEventArgs e ) { if (e.Type.ToLowerInvariant()=="keydown" )
{ if (e.Key.ToLowerInvariant()=="t" )
{ await Task.Delay( 50 ); // you may need to tweak this timeout selectedDate=DateTime.Now;
}
}
}
} Since that's quite a peculiar case, would you be OK if I moved this thread to the public forums so other people can see your use case and evaluate this solution? Regards, Marin Bratanov

### Response

**Joe** answered on 16 Oct 2019

Sure! Feel free to share and thank you. Looks like a good solution. Joe

### Response

**Joe** answered on 16 Oct 2019

It looks like the routine will only process the keystroke one time. I also use the + sign to increment the date. It works the 1st time but additional + do not work. Any ideas? Thanks, Joe

### Response

**Joe** answered on 16 Oct 2019

Disregard last remark. It was user error. :-) Thanks, Joe

### Response

**Marin Bratanov** answered on 17 Oct 2019

Thank you for sharing this with the community, Joe, it is now public at [https://www.telerik.com/forums/datepicker-shortcut](https://www.telerik.com/forums/datepicker-shortcut) Regards, Marin Bratanov

### Response

**Nikul** answered on 16 Jan 2020

Hi Marin, I was trying to implement the similar approach on a blazor inputcomponent to have a functionality to press Enter key to switch to next textbox (<input/>) however, I am not able to figure out how do I increase tab index or send the focus to the next component with specified tab index. <input class="my-component form-control" @onkeypress="MyCoolTextBox_OnKeyPress"/> @code { async Task MyCoolTextBox_OnKeyPress(KeyboardEventArgs e) { if(e.Type.ToLowerInvariant()=="keypress") { if (e.Key.ToLowerInvariant()=="Enter") { // Increase the tab index and send focus to next component... } } } } Any ideas how do I achieve this?

### Response

**Marin Bratanov** answered on 17 Jan 2020

Hello Nikul, Focusing an element requires JS Interop at this point: [https://github.com/dotnet/aspnetcore/issues/10521.](https://github.com/dotnet/aspnetcore/issues/10521.) You could use the same JS function to adjust the tab indexes on the page. Or, you could bind them all to variables in your view model and perform the calculations with C#, so Blazor will re-render everything (make sure to call the focus from the JS Interop after that, because otherwise re-rendering may blur the desired element). Or, you could define the desired tab order statically and if something needs to be unavailable you can either remove it altoghether from the DOM, or set its disabled attribute. There is no silver bullet on how to implement accessibility and especially a roving tab index can be especially tricky. Regards, Marin Bratanov
