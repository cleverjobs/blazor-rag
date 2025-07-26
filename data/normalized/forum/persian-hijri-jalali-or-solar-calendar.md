# Persian , Hijri , Jalali or solar Calendar

## Question

**Moh** asked on 09 Jan 2025

Hello I need a DatePicker with solar or Jalali or hijri or Persian calendar. Please help me. Thanks

## Answer

**Mohamad Javad** answered on 15 Jan 2025

Hello, according to the guidance of the Telerik team, I was able to create a solar or Persian calendar. I will share my code with you in several steps. With this method, Arabic, Hebrew, etc. calendars can also be created. 1- I used .NET 8 2- Add the following code to the Program.cs project: using System.Globalization;

CultureInfo.DefaultThreadCurrentCulture=CultureInfo.DefaultThreadCurrentUICulture=PersianDateExtensio nMethods.GetPersianCulture(); 3- Create a class named Persian Date Extension Methods.cs with the following contents: using System; using System.Globalization; using System.Reflection; using System.Runtime.Serialization; namespace System { public static class PersianDateExtensionMethods { private static CultureInfo _Culture; public static CultureInfo GetPersianCulture () { if (_Culture==null )
{
_Culture=new CultureInfo( "fa-IR" );
DateTimeFormatInfo formatInfo=_Culture.DateTimeFormat;
formatInfo.AbbreviatedDayNames=new [] { "ی", "د", "س", "چ", "پ", "ج", "ش" };
formatInfo.MonthNames=new [] { "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "" };
formatInfo.MonthGenitiveNames=new [] { "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "" };
formatInfo.AbbreviatedMonthNames=new [] { "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "" };
formatInfo.AbbreviatedMonthGenitiveNames=new [] { "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "" };
formatInfo.AbbreviatedDayNames=new string [] { "ی", "د", "س", "چ", "پ", "ج", "ش" };
formatInfo.ShortestDayNames=new string [] { "ی", "د", "س", "چ", "پ", "ج", "ش" };
formatInfo.DayNames=new string [] { "یکشنبه", "دوشنبه", "سهشنبه", "چهارشنبه", "پنجشنبه", "جمعه", "شنبه" };
formatInfo.AMDesignator="ق.ظ";
formatInfo.PMDesignator="ب.ظ";
formatInfo.ShortTimePattern="HH:mm"; /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// / formatInfo.DateSeparator="/";

formatInfo.FullDateTimePattern="dd/MM/yyyy HH:mm"; /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// / formatInfo.FirstDayOfWeek=DayOfWeek.Saturday; // DateTimeFormat.ShortDatePattern /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// /// // formatInfo.ShortDatePattern="dd/MM/yyyy";

formatInfo.LongDatePattern="dd/MM/yyyy HH:mm";
formatInfo.SetAllDateTimePatterns( new [] { "dd/MM/yyyy" }, 'd' );
formatInfo.SetAllDateTimePatterns( new [] { "dddd, dd MMMM yyyy" }, 'D' );

formatInfo.SetAllDateTimePatterns( new [] { "yyyy MMMM" }, 'y' );
formatInfo.SetAllDateTimePatterns( new [] { "yyyy MMMM" }, 'Y' );

formatInfo.FirstDayOfWeek=DayOfWeek.Saturday;
System.Globalization.Calendar cal=new PersianCalendar();

FieldInfo fieldInfo=_Culture.GetType().GetField( "calendar", BindingFlags.NonPublic | BindingFlags.Instance); if (fieldInfo !=null )
fieldInfo.SetValue(_Culture, cal);

FieldInfo info=formatInfo.GetType().GetField( "calendar", BindingFlags.NonPublic | BindingFlags.Instance); if (info !=null )
info.SetValue(formatInfo, cal);

_Culture.NumberFormat.NumberDecimalSeparator="/";
_Culture.NumberFormat.DigitSubstitution=DigitShapes.NativeNational;
_Culture.NumberFormat.NumberNegativePattern=0;
} return _Culture;
} public static string ToPersianDateString ( this DateTime date, string format="yyyy/MM/dd" ) { return date.ToString(format, GetPersianCulture());
}
}
} 4- 4-Add a DatePicker to one of the project pages, like the code below: <TelerikDatePicker @bind-Value="@D2_DateTime">
</TelerikDatePicker>

@code { private DateTime D1_DateTime { get; set; }=DateTime.Today;
{ By running the project, you will see that the months and years of the calendar have been converted to Persian so far, but there are two problems: A-The days of the calendar are in the Gregorian calendar B-After selecting a day, the calendar number written in the DatePicker box is also in the Gregorian calendar. 5-These problems can be solved using CSS and a few commands. Now replace the DataPicker code above with the following code: <TelerikDatePicker @bind-Value="@D1_DateTime" OnClose="@DatePicker1_OnCloseHandler" Format="@DatePickerFormat1" Max="@MaxDatePicker" OnCalendarCellRender="@DatePicker1_OnCalendarCellRenderHandler"> </TelerikDatePicker> @code { private DateTime D1_DateTime { get; set; }=DateTime.Today; private DateTime MaxDatePicker=DateTime.Today; private string? DatePickerFormat1; private async Task DatePicker1_OnCloseHandler () {
DatePickerFormat1=D1_DateTime.ToShortDateString();

} private void DatePicker1_OnCalendarCellRenderHandler ( DatePickerCalendarCellRenderEventArgs args ) { if (args.View==CalendarView.Month)
{
args.Class="CssDatePersian_" + _Pc.GetDayOfMonth(args.Date).ToString();
}
}

} 6-Also add this CSS to this page or App.razor to fix the problem of incorrect display of calendar day numbers: .CssDatePersian_1 { color: black;
}.CssDatePersian_1 span::before { color: black; content: '1'; visibility: visible;
}.k-selected.CssDatePersian_1 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_1 span { content: '1'!important; visibility: hidden;
}.CssDatePersian_2 { color: black;
}.CssDatePersian_2 span::before { color: black; content: '2'; visibility: visible;
}.k-selected.CssDatePersian_2 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_2 span { content: '2'!important; visibility: hidden;
}.CssDatePersian_3 { color: black;
}.CssDatePersian_3 span::before { color: black; content: '3'; visibility: visible;
}.k-selected.CssDatePersian_3 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_3 span { content: '3'!important; visibility: hidden;
}.CssDatePersian_4 { color: black;
}.CssDatePersian_4 span::before { color: black; content: '4'; visibility: visible;
}.k-selected.CssDatePersian_4 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_4 span { content: '4'!important; visibility: hidden;
}.CssDatePersian_5 { color: black;
}.CssDatePersian_5 span::before { color: black; content: '5'; visibility: visible;
}.k-selected.CssDatePersian_5 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_5 span { content: '5'!important; visibility: hidden;
}.CssDatePersian_6 { color: black;
}.CssDatePersian_6 span::before { color: black; content: '6'; visibility: visible;
}.k-selected.CssDatePersian_6 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_6 span { content: '6'!important; visibility: hidden;
}.CssDatePersian_7 { color: black;
}.CssDatePersian_7 span::before { color: black; content: '7'; visibility: visible;
}.k-selected.CssDatePersian_7 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_7 span { content: '7'!important; visibility: hidden;
}.CssDatePersian_8 { color: black;
}.CssDatePersian_8 span::before { color: black; content: '8'; visibility: visible;
}.k-selected.CssDatePersian_8 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_8 span { content: '8'!important; visibility: hidden;
}.CssDatePersian_9 { color: black;
}.CssDatePersian_9 span::before { color: black; content: '9'; visibility: visible;
}.k-selected.CssDatePersian_9 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_9 span { content: '9'!important; visibility: hidden;
}.CssDatePersian_10 { color: black;
}.CssDatePersian_10 span::before { color: black; content: '10'; visibility: visible;
}.k-selected.CssDatePersian_10 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_10 span { content: '10'!important; visibility: hidden;
}.CssDatePersian_11 { color: black;
}.CssDatePersian_11 span::before { color: black; content: '11'; visibility: visible;
}.k-selected.CssDatePersian_11 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_11 span { content: '11'!important; visibility: hidden;
}.CssDatePersian_12 { color: black;
}.CssDatePersian_12 span::before { color: black; content: '12'; visibility: visible;
}.k-selected.CssDatePersian_12 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_12 span { content: '12'!important; visibility: hidden;
}.CssDatePersian_13 { color: black;
}.CssDatePersian_13 span::before { color: black; content: '13'; visibility: visible;
}.k-selected.CssDatePersian_13 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_13 span { content: '13'!important; visibility: hidden;
}.CssDatePersian_14 { color: black;
}.CssDatePersian_14 span::before { color: black; content: '14'; visibility: visible;
}.k-selected.CssDatePersian_14 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_14 span { content: '14'!important; visibility: hidden;
}.CssDatePersian_15 { color: black;
}.CssDatePersian_15 span::before { color: black; content: '15'; visibility: visible;
}.k-selected.CssDatePersian_15 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_15 span { content: '15'!important; visibility: hidden;
}.CssDatePersian_16 { color: black;
}.CssDatePersian_16 span::before { color: black; content: '16'; visibility: visible;
}.k-selected.CssDatePersian_16 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_16 span { content: '16'!important; visibility: hidden;
}.CssDatePersian_17 { color: black;
}.CssDatePersian_17 span::before { color: black; content: '17'; visibility: visible;
}.k-selected.CssDatePersian_17 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_17 span { content: '17'!important; visibility: hidden;
}.CssDatePersian_18 { color: black;
}.CssDatePersian_18 span::before { color: black; content: '18'; visibility: visible;
}.k-selected.CssDatePersian_18 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_18 span { content: '18'!important; visibility: hidden;
}.CssDatePersian_19 { color: black;
}.CssDatePersian_19 span::before { color: black; content: '19'; visibility: visible;
}.k-selected.CssDatePersian_19 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_19 span { content: '19'!important; visibility: hidden;
}.CssDatePersian_20 { color: black;
}.CssDatePersian_20 span::before { color: black; content: '20'; visibility: visible;
}.k-selected.CssDatePersian_20 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_20 span { content: '20'!important; visibility: hidden;
}.CssDatePersian_21 { color: black;
}.CssDatePersian_21 span::before { color: black; content: '21'; visibility: visible;
}.k-selected.CssDatePersian_21 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_21 span { content: '21'!important; visibility: hidden;
}.CssDatePersian_22 { color: black;
}.CssDatePersian_22 span::before { color: black; content: '22'; visibility: visible;
}.k-selected.CssDatePersian_22 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_22 span { content: '22'!important; visibility: hidden;
}.CssDatePersian_23 { color: black;
}.CssDatePersian_23 span::before { color: black; content: '23'; visibility: visible;
}.k-selected.CssDatePersian_23 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_23 span { content: '23'!important; visibility: hidden;
}.CssDatePersian_24 { color: black;
}.CssDatePersian_24 span::before { color: black; content: '24'; visibility: visible;
}.k-selected.CssDatePersian_24 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_24 span { content: '24'!important; visibility: hidden;
}.CssDatePersian_25 { color: black;
}.CssDatePersian_25 span::before { color: black; content: '25'; visibility: visible;
}.k-selected.CssDatePersian_25 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_25 span { content: '25'!important; visibility: hidden;
}.CssDatePersian_26 { color: black;
}.CssDatePersian_26 span::before { color: black; content: '26'; visibility: visible;
}.k-selected.CssDatePersian_26 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_26 span { content: '26'!important; visibility: hidden;
}.CssDatePersian_27 { color: black;
}.CssDatePersian_27 span::before { color: black; content: '27'; visibility: visible;
}.k-selected.CssDatePersian_27 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_27 span { content: '27'!important; visibility: hidden;
}.CssDatePersian_28 { color: black;
}.CssDatePersian_28 span::before { color: black; content: '28'; visibility: visible;
}.k-selected.CssDatePersian_28 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_28 span { content: '28'!important; visibility: hidden;
}.CssDatePersian_29 { color: black;
}.CssDatePersian_29 span::before { color: black; content: '29'; visibility: visible;
}.k-selected.CssDatePersian_29 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_29 span { content: '29'!important; visibility: hidden;
}.CssDatePersian_30 { color: gray;
}.CssDatePersian_30 span::before { color: black; content: '30'; visibility: visible;
}.k-selected.CssDatePersian_30 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_30 span { content: '30'!important; visibility: hidden;
}.CssDatePersian_31 { color: black;
}.CssDatePersian_31 span::before { color: black; content: '31'; visibility: visible;
}.k-selected.CssDatePersian_31 span::before { color: white; font-weight: bold; background-color: rgb ( 2, 119, 189 ); border-radius: 50%; height: 1.5rem; width: 1.5rem;
}.CssDatePersian_31 span { content: '31'!important; visibility: hidden;
} 7-Now everything is ready. Run the project and enjoy. The result is shown in the attached image. The only problem is that the numbers in the right box of the DataPicker are slightly protruding from the screen. Please advise how to solve this problem? Thanks

### Response

**Tsvetomir** commented on 20 Jan 2025

Hello Mohamad, Thank you for coming back with an alternative solution. Based on the provided screenshots, it seems that the additional CSS styles are the root cause of the issue. With that in mind, I recommend revising and adjusting the applied CSS styles. If you still face difficulties, please attach a runnable project with the Calendar modification. This will allow me to see the behavior on my side and troubleshoot it further. Regards, Tsvetomir

### Response

**Tsvetomir** answered on 10 Jan 2025

Hello Mohamad, Currently, the Telerik UI for Blazor date components, such as the DatePicker, only supports the Gregorian calendar. I noticed that you have already voted for the relevant feature request: Provide support for the Hijri calendar. Also, you can subscribe to the item to receive email notifications for any status changes. In the meantime, if any alternative approach appears we will share it in the item. Regards, Tsvetomir Progress Telerik
