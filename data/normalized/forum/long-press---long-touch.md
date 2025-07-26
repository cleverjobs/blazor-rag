# Long press - Long touch

## Question

**Nik** asked on 11 Nov 2021

Is it possible to run another method, if the user presses and holds on a series for lets say 2 or 3 seconds? Like in WPF: [https://www.telerik.com/forums/long-press-on-a-button-c1515a65de7e](https://www.telerik.com/forums/long-press-on-a-button-c1515a65de7e) If this makes sense. Regards, Nikolas

### Response

**Hristian Stefanov** commented on 16 Nov 2021

Hi Nikolas, Such an event for holding isn't provided out of the box. However, there might be a possible approach to achieve such functionality in the Blazor framework. As part of my research, I found this StackOverflow article that shows more details for a workaround with the js function. One thing to mention is that the approach is not tested, but using js functions is the way of replacing such events in the framework. You can try and see if it suits your application. In the meantime, you can share with us possible use cases of an event for holding after clicking. Thank you, and I look forward to your feedback on how things turned out. Regards, Hristian Stefanov
