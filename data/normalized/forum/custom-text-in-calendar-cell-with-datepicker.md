# Custom Text In Calendar Cell With DatePicker

## Question

**Moh** asked on 08 Jan 2025

Hello I want to write a desired text instead of calendar numbers. For example, as specified in the attached file, I want to write the desired text (8 day of month) instead of the number 8. I tried through the event: OnCalendarCellRender="@OnCalendarCellRenderHandler" but I did not get the result. Please help me.

## Answer

**Hristian Stefanov** answered on 08 Jan 2025

Hi Mohamad, I can confirm that the OnCalendarCellRender event allows you to apply a custom CSS class to the calendar cells. You can then use this class to add text before or after the date using CSS. Below is an example I’ve prepared for you. However, please note that with this amount of text, you may need to increase the popup width for better display. <TelerikDatePicker @bind-Value="@DatePickerValue" OnCalendarCellRender="@OnCalendarCellRenderHandler" Width="295px"> </TelerikDatePicker> <style>.special { color: white; background-color: greenyellow; font-weight: bold;
}.special span::after { content: ' day of month';
} </style> @code {
private DateTime? DatePickerValue { get; set; }=DateTime.Today;

private void OnCalendarCellRenderHandler(DatePickerCalendarCellRenderEventArgs args)
{
args.Class="special";
}
} Regards, Hristian Stefanov Progress Telerik

### Response

**Mohamad Javad** commented on 08 Jan 2025

Hello Thank you for your advice. I need to add or replace text dynamically. So that for example 1- I can replace the number of each day with another int value. For example, instead of 8, I can write 20, instead of 9, I can write 21, and so on. 2- In addition to replacing a specific value for each day, I can also assign a specific text to each day. That is, instead of 8, I can replace 20 is Tooday, 9 replaces 21 tomorrow, and so on. Thanks

### Response

**Hristian Stefanov** commented on 09 Jan 2025

Hi Mohamad, If you need to replace a specific date number with another, you can still achieve this by using CSS to hide the cell’s original content. Below is an enhanced version of the example I shared earlier, now updated to include cell value replacement functionality. Depending on your business requirements, you can use this as a starting point, adding more conditions to the OnCellRender handler and further customizations as needed. <TelerikDatePicker @bind-Value="@DatePickerValue" OnCalendarCellRender="@OnCalendarCellRenderHandler" Width="295px"> </TelerikDatePicker> <style>.special { color: black; font-weight: bold;
}.special span::after { content: '8.5 day of month'; visibility: visible;
}.special span { visibility: hidden;
} </style> @code {
private DateTime? DatePickerValue { get; set; }=DateTime.Today;

private void OnCalendarCellRenderHandler(DatePickerCalendarCellRenderEventArgs args)
{ if (args.Date.Day==8)
{ args.Class="special"; } }
} Kind Regards, Hristian

### Response

**Mohamad Javad** commented on 09 Jan 2025

Hello Thank you very much My problem is solved. There is only one problem, that after selecting the desired text in DatePicker, and closing it, when I open DatePicker again, instead of selecting the selected text, an empty area is seen. Like the attached image. I also need to change the Today text in DatePicker. I would appreciate your advice. Thanks

### Response

**Hristian Stefanov** commented on 10 Jan 2025

Hi Mohamad, I apologize for not noticing earlier that the value goes blank when selected. To resolve this, update the CSS by adding the following styles. Here’s an enhanced version of the sample: <TelerikDatePicker @bind-Value="@DatePickerValue" OnCalendarCellRender="@OnCalendarCellRenderHandler" Width="295px"> </TelerikDatePicker> <style>.special { color: black; font-weight: bold;
}.special span::after { content: '8.5 day of month'; visibility: visible; color: black; }.k-selected.special span::after { background-color: #ff6358;
}.special span { visibility: hidden;
} </style> @code {
private DateTime? DatePickerValue { get; set; }=DateTime.Today;

private void OnCalendarCellRenderHandler(DatePickerCalendarCellRenderEventArgs args)
{
if (args.Date.Day==8)
{
args.Class="special";
}
}
} For customizing the "Today" text, use localization. Kind Regards, Hristian

### Response

**Mohamad Javad** answered on 13 Jan 2025

Hello Thanks for your tips. Using .special span::after or .special span::Before The numbers on the right or left of the DatetPicker are protruding from the box. Is it possible to make the number box larger? And also the color of the selected day does not exactly surround the number, it is a little higher or lower. I even converted it to a circle with the following CSS code, but it still did not change: color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem; My C# code and CSS file: private void DatePicker1_OnCalendarCellRenderHandler ( DatePickerCalendarCellRenderEventArgs args ) { if (args.View==CalendarView.Month)

{

args.Class="special_" + _Pc.GetDayOfMonth(args.Date).ToString();

}

} .special_1 { color: black;
}.special_1 span::before { color: black; content: '1'; visibility: visible;
}.k-selected.special_1 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_1 span { content: '1'!important; visibility: hidden;
}.special_2 { color: black;
}.special_2 span::before { color: black; content: '2'; visibility: visible;
}.k-selected.special_2 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_2 span { content: '2'!important; visibility: hidden;
}.special_3 { color: black;
}.special_3 span::before { color: black; content: '3'; visibility: visible;
}.k-selected.special_3 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_3 span { content: '3'!important; visibility: hidden;
}.special_4 { color: black;
}.special_4 span::before { color: black; content: '4'; visibility: visible;
}.k-selected.special_4 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_4 span { content: '4'!important; visibility: hidden;
}.special_5 { color: black;
}.special_5 span::before { color: black; content: '5'; visibility: visible;
}.k-selected.special_5 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_5 span { content: '5'!important; visibility: hidden;
}.special_6 { color: black;
}.special_6 span::before { color: black; content: '6'; visibility: visible;
}.k-selected.special_6 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_6 span { content: '6'!important; visibility: hidden;
}.special_7 { color: black;
}.special_7 span::before { color: black; content: '7'; visibility: visible;
}.k-selected.special_7 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_7 span { content: '7'!important; visibility: hidden;
}.special_8 { color: black;
}.special_8 span::before { color: black; content: '8'; visibility: visible;
}.k-selected.special_8 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_8 span { content: '8'!important; visibility: hidden;
}.special_9 { color: black;
}.special_9 span::before { color: black; content: '9'; visibility: visible;
}.k-selected.special_9 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_9 span { content: '9'!important; visibility: hidden;
}.special_10 { color: black;
}.special_10 span::before { color: black; content: '10'; visibility: visible;
}.k-selected.special_10 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_10 span { content: '10'!important; visibility: hidden;
}.special_11 { color: black;
}.special_11 span::before { color: black; content: '11'; visibility: visible;
}.k-selected.special_11 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_11 span { content: '11'!important; visibility: hidden;
}.special_12 { color: black;
}.special_12 span::before { color: black; content: '12'; visibility: visible;
}.k-selected.special_12 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_12 span { content: '12'!important; visibility: hidden;
}.special_13 { color: black;
}.special_13 span::before { color: black; content: '13'; visibility: visible;
}.k-selected.special_13 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_13 span { content: '13'!important; visibility: hidden;
}.special_14 { color: black;
}.special_14 span::before { color: black; content: '14'; visibility: visible;
}.k-selected.special_14 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_14 span { content: '14'!important; visibility: hidden;
}.special_15 { color: black;
}.special_15 span::before { color: black; content: '15'; visibility: visible;
}.k-selected.special_15 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_15 span { content: '15'!important; visibility: hidden;
}.special_16 { color: black;
}.special_16 span::before { color: black; content: '16'; visibility: visible;
}.k-selected.special_16 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_16 span { content: '16'!important; visibility: hidden;
}.special_17 { color: black;
}.special_17 span::before { color: black; content: '17'; visibility: visible;
}.k-selected.special_17 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_17 span { content: '17'!important; visibility: hidden;
}.special_18 { color: black;
}.special_18 span::before { color: black; content: '18'; visibility: visible;
}.k-selected.special_18 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_18 span { content: '18'!important; visibility: hidden;
}.special_19 { color: black;
}.special_19 span::before { color: black; content: '19'; visibility: visible;
}.k-selected.special_19 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_19 span { content: '19'!important; visibility: hidden;
}.special_20 { color: black;
}.special_20 span::before { color: black; content: '20'; visibility: visible;
}.k-selected.special_20 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_20 span { content: '20'!important; visibility: hidden;
}.special_21 { color: black;
}.special_21 span::before { color: black; content: '21'; visibility: visible;
}.k-selected.special_21 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_21 span { content: '21'!important; visibility: hidden;
}.special_22 { color: black;
}.special_22 span::before { color: black; content: '22'; visibility: visible;
}.k-selected.special_22 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_22 span { content: '22'!important; visibility: hidden;
}.special_23 { color: black;
}.special_23 span::before { color: black; content: '23'; visibility: visible;
}.k-selected.special_23 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_23 span { content: '23'!important; visibility: hidden;
}.special_24 { color: black;
}.special_24 span::before { color: black; content: '24'; visibility: visible;
}.k-selected.special_24 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_24 span { content: '24'!important; visibility: hidden;
}.special_25 { color: black;
}.special_25 span::before { color: black; content: '25'; visibility: visible;
}.k-selected.special_25 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_25 span { content: '25'!important; visibility: hidden;
}.special_26 { color: black;
}.special_26 span::before { color: black; content: '26'; visibility: visible;
}.k-selected.special_26 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_26 span { content: '26'!important; visibility: hidden;
}.special_27 { color: black;
}.special_27 span::before { color: black; content: '27'; visibility: visible;
}.k-selected.special_27 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_27 span { content: '27'!important; visibility: hidden;
}.special_28 { color: black;
}.special_28 span::before { color: black; content: '28'; visibility: visible;
}.k-selected.special_28 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_28 span { content: '28'!important; visibility: hidden;
}.special_29 { color: black;
}.special_29 span::before { color: black; content: '29'; visibility: visible;
}.k-selected.special_29 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_29 span { content: '29'!important; visibility: hidden;
}.special_30 { color: gray;
}.special_30 span::before { color: black; content: '30'; visibility: visible;
}.k-selected.special_30 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_30 span { content: '30'!important; visibility: hidden;
}.special_31 { color: black;
}.special_31 span::before { color: black; content: '31'; visibility: visible;
}.k-selected.special_31 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.special_31 span { content: '31'!important; visibility: hidden;
} Please give me some advice. Thanks

### Response

**Hristian Stefanov** commented on 14 Jan 2025

Hi Mohamad, To make the desired styling adjustments and customizations, use your browser's developer tools to inspect the rendered HTML. This will allow you to identify the necessary CSS selectors, such as the number box or selected day, and apply the appropriate styles. Kind Regards, Hristian

### Response

**Mohamad Javad** commented on 15 Jan 2025

Hello Thanks for your guidance. With your guidance, I was able to create a Persian Calendar and DatePicker or any other calendar. I am sharing my codes in the topic named: Persian, Hijri, Jalali or solar Calendar and the link: [https://www.telerik.com/forums/persian-hijri-jalali-or-solar-calendar](https://www.telerik.com/forums/persian-hijri-jalali-or-solar-calendar) . I hope you will help me in that topic to finalize this work and solve the remaining small problems. Thanks

### Response

**Hristian Stefanov** commented on 16 Jan 2025

Hi Mohamad, Thank you for giving me an update. Regarding the other public post, I can confirm that a colleague has already been assigned to address it. Please continue monitoring that item there for any updates or progress Kind Regards, Hristian
