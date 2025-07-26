# Time zone for NOW button

## Question

**Dou** asked on 19 Nov 2020

With Blazor server, clicking the NOW button (obviously) sets the time to the time on the server since that's where the code is running. Is there a way to trap the NOW button click or somehow give it an offset or define the value that NOW means so NOW will mean the time that the user is sitting in?

## Answer

**Marin Bratanov** answered on 20 Nov 2020

Hello Doug, I made the following feature request for your to Follow: [https://feedback.telerik.com/blazor/1496094-time-zone-for-now-button.](https://feedback.telerik.com/blazor/1496094-time-zone-for-now-button.) At the moment, I don't think I can offer a feasible solution (apart from maybe hiding that button with CSS if it's an issue for you). The NOW button will trigger the ValueChanged event an then OnChange, but those can be triggered by the user typing or selecting things, and those scenarios are quite different - when they type/choose from the spinners you can apply the offset you know they have (say, because they have set a time zone in their accounts). Regards, Marin Bratanov

### Response

**Doug** answered on 08 Feb 2021

Hi Marin, I've had to revisit this issue. We've decided that it would be an acceptable solution to remove the NOW button from the datetime picker as you suggest. I'm not an expert with CSS (especially when it comes to applying it to Telerik controls) so would you mind providing me the CSS to hide the NOW button? Thanks.

### Response

**Marin Bratanov** answered on 08 Feb 2021

Hi Doug, This blog post can help you create such CSS overrides yourself. Here is also an example I made for you: <style>. no-now-button.k-time-now { display: none;
} </style>

Selected time: @selectedTime
<br /> <TelerikDateTimePicker PopupClass=" no-now-button " Min="@Min" Max="@Max" @bind-Value="@selectedTime" Format="dd MMM yyyy HH:mm:ss" Width="250px"> </TelerikDateTimePicker> @code {
private DateTime? selectedTime=DateTime.Now;
public DateTime Min=new DateTime( 1990, 1, 1, 8, 15, 0 );
public DateTime Max=new DateTime( 2025, 1, 1, 19, 30, 45 );
} Regards, Marin Bratanov

### Response

**Doug** answered on 08 Feb 2021

Marin, That works perfectly! Thanks for the quick response!
