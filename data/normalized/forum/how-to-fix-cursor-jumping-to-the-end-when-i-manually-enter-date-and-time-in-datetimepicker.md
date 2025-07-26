# How to fix cursor jumping to the end when I manually enter date and time in DateTimePicker

## Question

**Ale** asked on 24 Jan 2025

I use TelerikDateTimePicker and clients of my application send me a lot of issues with TelerikDateTimePicker. 1). If user types in values ( date and time ) quickly, user will be redirected to the end of input field e.g. type in year 2023 as fast as possible -> only one or two first digits will be filled, other digits will be typed in the end of the field 2) After user manually enters month, year is not selected automatically. Users want the same behaviour as we have with day, year, hours, minutes: 3) After user finishes entering all valid values Date & Time and clicks outside the input field ( TelerikDateTimePicker ), all entered will be removed. I use code like: <label for="selected-date"> TelerikDateTimePicker for enter Date and Time </label> <TelerikDateTimePicker @bind-Value="@SelectedTime" Min="@Min" Max="@Max" Format="dd MMM yyyy HH:mm 'Z' (UTC)" Placeholder="dd MMM yyyy HH:mm 'Z' (UTC)" Id="selected-date" /> @code {
DateTime? SelectedTime=null;
DateTime Min { get; set; }=new(1900, 1, 1, 0, 0, 0);
public DateTime Max { get; set; }=new(2099, 12, 31, 23, 59, 59);
} I also tried to use some combinations of TelerikDateTimePicker properties: AllowCaretMode="true"
AutoCorrectParts="true"
AutoSwitchParts="true" but this only made the behaviour worse

### Response

**Oleksandr** commented on 27 Jan 2025

I have the same issue; after the user faces any strange behavior with the date picker(not a valid date, wrong cursor position, etc.), the component becomes unresponsive - all data is gone, and errors in the console

### Response

**Hristian Stefanov** commented on 27 Jan 2025

Hi all, Two of the issues you mentioned have already been reported on our public

### Response

**Perry** commented on 19 Mar 2025

Same issue of dates jumping around...really annoying. If I type the 4 digit year really fast it does not capture the year properly.
