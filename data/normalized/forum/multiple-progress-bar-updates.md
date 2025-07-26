# Multiple Progress Bar updates

## Question

**Ton** asked on 20 Dec 2022

Hello, I have a scenario where I have a Telerik Notification with a Telerik progress bar embedded. I am looking to update the progress bar of multiple instances of the notification independently based in separate threads. Would this be possible? Thanks, Tony

### Response

**Yanislav** commented on 23 Dec 2022

Hello Tony, Generally speaking, the ProgressBar is a fairly simple component with a few configurations. It is designed to be bound to a property from where it gets its value. Based on the description, I understand that it is inside a notification by using the Template configuration of the Telerik Notification. This means when a notification pops a new instance of the ProgressBar is rendered, however, it is bound to the same property. Updating the property to which the ProgressBars are bound will update all instances. In order to update the ProgressBars independently, they have to be bound to different properties. With that being said, if the count of notifications is dynamic, I'm not sure if this requirement is achievable. In theory, it should be possible, but it means at runtime creating properties and binding the ProgressBar to the newly created field. Note that the complexity of such an implementation would be high and the final result might be fragile and unreliable. On the other hand, if you know the exact count of the notifications and the progress bars you can declare different Notification instances, and based on the case display the respective one with the proper ProgressBar and update the value of the property to which the ProgressBar is bound. Note that if you decide to continue with this approach, the different instances of notification won't stack. So, you may apply some custom CSS to add spacing between the different Notification instances, so they do not appear on top of each other and all are visible. Here is a simple example: [https://blazorrepl.telerik.com/mmFwQHlF39n4PcqS03.](https://blazorrepl.telerik.com/mmFwQHlF39n4PcqS03.) I hope this information helps.
