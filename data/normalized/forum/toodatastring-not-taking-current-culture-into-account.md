# ToODataString not taking current culture into account

## Question

**Ger** asked on 21 Apr 2022

I've been struggling with this behaviour for a while now: - In my Blazor app 've set the culture to nl-NL (which at the moment is UTC+2) - Converting a normal datetime to UTC gives me the result i expect. IE. var test=new DateTime(1978, 9, 4).ToUniversalTime(); Results in test being '1978-9-3 22:00:00Z' Now when i use the Grid component with a default filter row i handle the 'OnRead' event of the grid and use the ToODataString() to get the formatted filter: var filter=args.Request.ToODataString(); No matter what i try, the filter returned always formats the dates i filter incorrect. Filtering on '1978-09-04' is formatted as '1978-09-04 00:00:00Z' while i expect it to be '1978-09-03 22:00:00Z'. Am i missing something trivial here or is this a bug in the ToODataString method? Regards, Gerrit

### Response

**Marin Bratanov** commented on 23 Apr 2022

Hi Gerrit, are you using a DateTime filter in the grid? It has to be selected explicitly (see the docs here ) and without that the grid defaults to a Date picker, so it should be expected that it sets the time to midnight (00:00:00 hours). If upgrading to 3.1.0 (the first release with the the feature that lets you add a time component to the filtering) and using the DateTime picker does not help, please post a small sample in Blazor repl that we can take a look at.

### Response

**Gerrit** commented on 25 Apr 2022

Hi Martin, I've tried using the solution you suggested but that doesn't make a difference. I feel that even if it's a date and it defaults to midnight (in the current culture, IE 'nl-NL') the value formatted in UTC should take the timezones into acount. I've made a little snippet here: [https://blazorrepl.telerik.com/mGkycpkB43TAy26v34](https://blazorrepl.telerik.com/mGkycpkB43TAy26v34)

### Response

**Marin Bratanov** commented on 25 Apr 2022

Hi Gerrit, Adding the filter type to a DateTimePicker and choosing the time (which defaults to the current time, or you can use the NOW button), puts the current time in the odata string on my end: [https://blazorrepl.telerik.com/cmOowfPD1451Iw6V35](https://blazorrepl.telerik.com/cmOowfPD1451Iw6V35) The default DatePicker is supposed to set midnight to the DateTime object it produces. If you want to change that, you can copy the DataSourceRequest object, i terate its filters, find the DateTime ones and choose whether to alter them in any way before calling .ToODataString() - here lies the heuristic part - how would you know if the user intends midnight by explicit action, or they simply picked nothing - and this is why the grid does not do anything further with it unless there is an explicit time picker involved which produces and explicit user action. The grid should not do any other manipulations on the time portions, this is something that the application needs to take care of - the grid can't know what format you use, what time zones you use, what data the endpoints expect and whose responsibility is to do the conversion (that, for example, ranges from a fat client, to the backend service, to the actual database server). So if we do it, we can irreparably break application logic, while letting the application handle that allows for flexibility.

### Response

**Gerrit** commented on 28 Apr 2022

Hi Martin, I've tried the sulution you suggested by modifying the filter values before calling the ToODataString(). This results in a proper ODataString being formatted. However, it leads to the filter value changing and being a day earlier. foreach(FilterDescriptor gridFilter in args.Request.Filters) { if(gridFilter.MemberType==typeof(DateTime)) { gridFilter.Value=((DateTime)gridFilter.Value).ToUniversalTime(); } } Still i don't see why this shoulsd be solve in such a way. The grid (and filtering values) are entered by the user taking into account to users current regional settings. (i my case UTC +2). I doesn't matter if the user intended to pick 'midnight' or any other specific time. Whatever time is selected, it's always the time specific for the users region. The ToODataString method however formats these dates and times as being UTC (ending with Z) and does not take the current users regional settings into account. From my point of view, the ToODataString() method should not format the date and/or time as if it were UTC or it should do it properly, ajusting the formatted value to real UTC coming from the users specific timezome.

### Response

**Nadezhda Tacheva** commented on 03 May 2022

Hi Gerrit, I am stepping in the discussion as my colleague, Marin is currently out of office. I suppose the result you are getting is due to using DatePicker (at least I hit the same when testing). When using DatePicker, the time portion is not really a factor and, as Marin mentioned, it is set to midnight (00:00:00 hours). Then, when you are converting the filter values ToUniversalTime(), you are actually setting them to UTC which is a couple hours behind your current time zone and probably this is why things get mixed up. If you want to have the time portion in the filter value, you should use DateTimePicker as a filter operator. Testing on my end using your approach seems to work as expected - [https://blazorrepl.telerik.com/cQazERug17rkij5U53.](https://blazorrepl.telerik.com/cQazERug17rkij5U53.) To be honest, I got a bit lost on the exact desired scenario. The ToUniversalTime() converts the DateTime object to UTC and in the beginning of the thread I was left with the impression that you want to get the current time according to your local time zone (UTC +2) and not UTC (zero offset). That said, it will be useful if you can confirm the result you want to achieve to make sure we are on the same page. For example, if you are converting the filters ToUniversalTime(), when the user selects time from the dropdown it will be automatically converted a couple hours back to match the UTC zero offset. ToODataString() returns string representation of the selected DateTime, but the object value needs to be correct prior to calling this method. Ability to control the format of the ToODataString() is one thing and taking the current culture into account is another. That said, you may take a look at this feature request for the DateTimePicker - Time zone for NOW and TODAY button (or function to be called). Thus, clicking the Now button will give you the current local time based on the culture and then the string conversion will take that into account. By design, the ToODataString() method is configured to use DateTimeKind.Utc for DateTime objects which are then converted to string the round-trip ("O", "o") format specifier. Here comes the "Z" in the string (see the second bullet in the linked section when DateTimeKind.Utc is used).

### Response

**Gerrit** commented on 06 May 2022

Hi Nadezhda, I've modified the snippet to hopefully make clear what my problem is. [https://blazorrepl.telerik.com/ccOpkUkh36KOP3B354](https://blazorrepl.telerik.com/ccOpkUkh36KOP3B354) I,ve got a frontend and backend both using the Dutch timezone (UTC+2 atm). So i need a date (with or without time for that matter) to be passed between those two without messing it up. Now when i enter 1978-09-04 00:00:00 in the filter of the grid, the ToODataString formats this value as being UTC without first properly converting it to UTC. So the produced filter contains 1978-09-04 00:00:00Z. The backend however converts this value back into the Dutch locale again causing me to filter on 1978-09-04 02:00:00. In the above situation i need the ToODataString to produce 1978-09-03 22:00:00Z as that is the proper value for the entered date in UTZ taking the +2 offset of the Dutch timezone into account. The only way to work around this atm is to first convert alle filters in the grid to UTC, call ToODataString an the convert all dates back into local (Dutch) timezone again. If i don't do this last thing, the grid will show me i'm filtering on 1978-09-03 rather than 1978-09-04. This in my opinion is not a proper solution for this and hopefully shows that there (imho) is a bug in the ToODataFilter method. Besides the issue with the formatting of date values, i'm now also running into a similar issue when filtering on decimal values. These seem to be formatted using the local decimal seperator (which in my case is a comma rather then a dot). Resulting in an invalid OData filter: $filter=(value eq 10,15) instead of the expected $filter=(value 10.15). Regards, Gerrit

### Response

**Marin Bratanov** commented on 07 May 2022

Hi Gerrit, The .ToODataString() method works on the current machine that executes the code, and uses the current data and localization settings. If your backend has specific requirements, perhaps it will be best for you to make a deep copy of the DataSourceRequest object the grid will give you, and transform it per your needs - change dates, for example, in the way your backend wants them. Ultimately, you can consider making the string yourself to satisfy the backend. Or, you could expose a new endpoint that can take the DataSourceRequest as it is, and directly work with it in .NET rather than go through several conversions, see these examples: [https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server.](https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server.)

### Response

**Gerrit** commented on 09 May 2022

Hi Martin, I'm well aware of the fact the .ToODataString() works on the current machine. For that reason we've made sure of frond and backend use the the same cultuer and timezone (nl-NL). The backend does not have any special requirements, but only requires a proper formatted OData query. At which the ToODataString currently is failing. To only format a date coming from the current culture as being UTC doesn't cut it. The data hase to be first converter to UTC taime to deal with the timezone difference. As for the formatting of the decimal value, it accorrding to the OData specs required a dot as a decimal seperator and not the comma wich in this case comes with the Dutch language setting. For this also see the specification for Edm.Decimal in the specifications. I really how you guys can make this method work as it should and be in line with the OData specifications. Regards, Gerrit

### Response

**Marin Bratanov** commented on 09 May 2022

Hi Gerrit, my name is Marin, without the "t". I must also iterate once more that our components will not and should not convert between time zones, this is a job for the application. I also get a dot in the odata string coming from the grid in this example: [https://blazorrepl.telerik.com/cGOputPJ31XUsMbt50.](https://blazorrepl.telerik.com/cGOputPJ31XUsMbt50.)

## Answer

**Gerrit** answered on 09 May 2022

Hi Marin, Sorry for getting your name wrong. I just had a look at the excampje to added with the numeric filter. That still gives me a comma in the produced OData filter. I can't even type a dot in the input control as that is not my decimal seperator character. I'm not saying the controls should convert between timezones, i'm saying the ToODataString should keep in mind that the DateTime it's serializing into a UTC format might not be in UTC and should first be converted to that. That's not converting between timezones but rather providing the correct value for that datatime in the format it's being specified in. It's really strikes me noone ran into this until now as i doubt i'm the only one not living in a plain UTC timezone :-) Regards, Gerrit
