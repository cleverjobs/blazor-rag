# Is there any way to limit the scheduler to a minimum date?

## Question

**Rol** asked on 22 Jan 2022

I want to prevent the user browsing back to previous days

## Answer

**Nadezhda Tacheva** answered on 26 Jan 2022

Hi Roland, With the current setup of the Scheduler, you can limit it to a minimum date by disabling the "previous" navigation button if the currently selected date matches your desired minimum date, so that the user cannot navigate more backwards. You can do that with some conditional CSS. You can handle the DateChanged event of the Scheduler to check if the currently selected date matches you desired min date, so you can toggle a flag based on which the styles will be applied. You can also perform that check when the component initializes in case your predefined selected date matches the minimum. The tricky part will be the calendar popup as even if you disable the previous button, the user will still be able to select from the calendar and there is no way to currently restrict the minimum date there. In future, the Scheduler will expose a Toolbar template where you can define your custom content - for example declare your DatePicker component where you can have control over the min date. If interested, you may vote for the request to increase its popularity as we are prioritizing the feature requests implementation based on community interest and demand. You can also follow it to receive email notifications on status changes. At this stage, you can disable the calendar, so that you don't allow the user to open it and thus ensure they cannot select earlier date than your desired minimum. You can achieve that with CSS as well by removing the pointer events from the element that opens the Calendar. As a result, you will still have the current date displayed but it will not be clickable. I have prepared a basic example to demonstrate how you can achieve this. I am sharing it via Telerik REPL for Blazor, so you can directly run and test it in the browser - [https://blazorrepl.telerik.com/cQkbQKbg52dExdbK26.](https://blazorrepl.telerik.com/cQkbQKbg52dExdbK26.) I hope you will find the above information useful to move forward with your application. If any further questions appear, please let us know. Regards, Nadezhda Tacheva

### Response

**Roland** commented on 26 Jan 2022

Thanks. I already had a brute force workaround, but now I can fine tune my code a bit, resulting in more visual feedback for the user.

### Response

**Nadezhda Tacheva** commented on 28 Jan 2022

Hi Roland, I am glad that the proposed solution will suffice to cover your desired result. In the meantime, I raised a discussion with our development team for the possibility to expose Min and Max parameters for the Scheduler to allow even easier control in such scenarios. We agreed that this is a valid feature, so I opened a request on your behalf. You can find it in our public
