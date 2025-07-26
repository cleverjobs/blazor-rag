# TimePicker does not support null values

## Question

**Rol** asked on 31 Aug 2020

<TelerikTimePicker Value="(DateTime?)null" Format="t" /> is showing the null DateTime as "t", not as an empty string. How do I prevent this?

## Answer

**Marin Bratanov** answered on 31 Aug 2020

Hi Roland, You can Follow the implementation of a different placeholder for the date pickers here: [https://feedback.telerik.com/blazor/1452940-placeholder-for-datepicker-and-the-other-date-inputs.](https://feedback.telerik.com/blazor/1452940-placeholder-for-datepicker-and-the-other-date-inputs.) At the moment, the design is that they show the Format when empty. I've added your Vote to that idea so it can raise its priority and in the thread you can find two ideas that can help you improve the UX. Regards, Marin Bratanov

### Response

**Roland** answered on 31 Aug 2020

My workaround would be: <TelerikTimePicker @bind-Value="@startAt" Format="@System.Globalization.CultureInfo.CurrentCulture.DateTimeFormat.ShortTimePattern"> but this is something that the component should do. Instead of using the "t" or "d" shortcut, retrieve the actual format.

### Response

**Marin Bratanov** answered on 01 Sep 2020

Hi Roland, I believe that a dedicated placeholder feature would be a better approach to solving this, because it will not have the component alter what the developer has set. Altering the Format is sometihng I think the input should not do, even if it is "just" to expand it to a longer representation. Besides altering the developer's choice, there is an issue with the mapping itself - DateTimeFormatInfo.GetAllDateTimePatterns(Char) method does not return a single option, but an array, and it is unclear which one is to be used. When you multiply this by the myriad of predefined shorthand format strings, the maintenance cost of this diminishes the benefits. Regards, Marin Bratanov

### Response

**Stefano** answered on 14 Dec 2020

I find the correction of this problem pretty urgent. My app is localized for italian language and, if in english "d" may suggest "day", in italian it is meaningless and even misleading.

### Response

**Marin Bratanov** answered on 15 Dec 2020

Hello Stefano, I see that you have voted for the placeholder feature about a month ago, and we take that into account when determining priorities and our roadmap. Clicking the Follow button is the best way to know when something new happens or when we know which release it will be in. For the time being, the best suggestion I can offer is setting a default value for the field. You could later compare against that value instead of against null to determine if the user chose something. Regards, Marin Bratanov
