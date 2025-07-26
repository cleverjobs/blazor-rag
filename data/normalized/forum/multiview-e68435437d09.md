# Multiview

## Question

**Dav** asked on 14 Nov 2019

I've modified the calendar with a bit of js, months now above each calendar.

## Answer

**David Rhodes** answered on 14 Nov 2019

JS window.blazorFunctions={ moveTelerikCalendarHeader: function (id) { var calendar=$(id); var header=calendar.find( ".k-calendar-header" ); var monthView=calendar.find( ".k-calendar-monthview" ); // move the header to underneathe the month views $(header).detach().insertAfter(monthView); // the header should be hidden in CSS so need to redisplay it header.css( "display", "flex" ); }, // sets the month names on the Telerik Blazor Calendar setTelerikCalendarMonthNames: function (id, startMonth, year) { const monthNames=[ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]; var calendar=$(id); var monthView=calendar.find( ".k-calendar-monthview" ); monthView.children().each( function () { var thead=$( this ).find( "thead" ); var rowId="MonthNames"; var monthNameRow=$(thead).find( "#" + rowId); // display eg November 2019 var monthDisplay=monthNames[startMonth] + ' ' + year; // if the row has already been added then update the existing value if (monthNameRow.length !==0) { monthNameRow.find( "th" ).text(monthDisplay); } else { thead.prepend( '<tr id="' + rowId + '"><th colspan="7">' + monthDisplay + '</th></tr>' ); } // increase the month startMonth +=1; if (startMonth> 11) { year +=1; startMonth=startMonth - 12; } }); } }; Razor protected override async Task OnAfterRenderAsync( bool firstRender) { if (firstRender) { await JSRuntime.InvokeAsync<object>( "blazorFunctions.setTelerikCalendarMonthNames", "#daysOffCalendar .k-calendar", (DateTime.Today.Month - 1), DateTime.Today.Year); await JSRuntime.InvokeAsync<object>( "blazorFunctions.moveTelerikCalendarHeader", "#daysOffCalendar .k-calendar" ); } } async Task DateChangedHandler(DateTime firstDateOfNewRange) { int month=firstDateOfNewRange.Month - 1; await JSRuntime.InvokeAsync<object>( "blazorFunctions.setTelerikCalendarMonthNames", "#daysOffCalendar .k-calendar", month, firstDateOfNewRange.Year); }

### Response

**David Rhodes** answered on 14 Nov 2019

a bit off css too .k-calendar { padding-top: 10px; .k-today, .k-title { display: none; } /* initially hide the header to avoid FOUC, it is moved to bottom using js */ .k-calendar-header { display: none; justify- content: flex-end; } }

### Response

**Marin Bratanov** answered on 18 Nov 2019

Hello David, Thank you for sharing your code with the community. Perhaps it would get better visibility if you post a sample (or at least a link) from your original request: [https://feedback.telerik.com/blazor/1434620-calendar-labeling-on-multi-month-view-month-names-to-be-above-each-month](https://feedback.telerik.com/blazor/1434620-calendar-labeling-on-multi-month-view-month-names-to-be-above-each-month) (I'd rather you do it instead of me because all credit should go to you). If you like you can even open a pull request with a sample under a new calendar folder in this repo: [https://github.com/telerik/blazor-ui.](https://github.com/telerik/blazor-ui.) Regards, Marin Bratanov
