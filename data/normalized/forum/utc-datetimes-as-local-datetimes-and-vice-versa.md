# UTC DateTimes as local DateTimes, and vice versa

## Question

**Mic** asked on 20 Apr 2020

Hi, I have a question regarding the handling of UTC DateTime values in the Grid and DateTime Picker components. In our C# code and database, all date and time data is in UTC. Is it currently possible to: Have UTC DateTime values displayed in the Telerik Grid according to the the user's local culture? Have values selected by the user via DateTime Picker be converted to UTC? Two examples: A Grid column binded to a UTC DateTime value 2020/20/04 15:00 will display as 20/04/2020 16:00 for users in the UK If 16:00 is selected in the DateTime Picker by a UK user during daylight saving time, 15:00 is the time that is actually stored Thanks in advance!

## Answer

**Marin Bratanov** answered on 23 Apr 2020

Hello Michael, Such conversions are up to the application and the view-model. Our components display what the app provides to them. For example, using a DateTime.Now in a WebAssembly app will have different results than using it in a server-side Blazor app. This is not something we can control or should control. We use the default .Kind of the DateTime object and we don't alter it additionally, so that we don't break the application that already takes care of that. Regards, Marin Bratanov

### Response

**Michael** answered on 24 Apr 2020

Hi Marin, Apologies, I was shortsighted with this query. After posting it I did some thinking and realised that, as you said, these concerns were more up to the application itself, and implemented code to do the conversions between the timezones as the data was being sent and received to/from the DB. Kind regards, Michael

### Response

**Marin Bratanov** answered on 24 Apr 2020

Hi Michael, It is a perfectly valid question, and I am glad this information is now available in the public forums, so everyone can find it. Thank you for bringing it up. Regards, Marin Bratanov
